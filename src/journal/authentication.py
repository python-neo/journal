from pathlib import Path
from secrets import token_bytes

from argon2.low_level import Type, hash_secret_raw
from Crypto.Cipher import AES

journal_file = Path.home () / "journal.bin"

def generate_key (password : str) -> bytes :
    if not journal_file.exists () :
        journal_file.write_bytes (token_bytes (16))

    data = journal_file.read_bytes ()

    salt = data [:16]
    key = hash_secret_raw (
        secret = password.encode (), salt = salt, time_cost = 3,
        memory_cost = 65536, parallelism = 4, hash_len = 32,
        type = Type.ID)
    return key

def decrypt_journal (key : bytes) -> str :
    data = journal_file.read_bytes ()
    if len (data) == 16 :
        return ""

    nonce = data [16:32]
    tag = data [32:48]
    ciphertext = data [48:]

    cipher = AES.new (key, AES.MODE_EAX, nonce = nonce)
    
    plaintext = cipher.decrypt_and_verify (ciphertext, tag)
    return plaintext.decode ()

def encrypt_journal (journal : str, key : bytes) -> None :
    data = journal_file.read_bytes ()
    salt = data [:16]

    cipher = AES.new (key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest (journal.encode ())

    journal_file.write_bytes (salt + cipher.nonce + tag + ciphertext)

def verify_journal () -> bool :
    if not journal_file.exists () :
        return False

    data = journal_file.read_bytes ()
    return len (data) == 16 or len (data) >= 48