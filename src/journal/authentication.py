from pathlib import Path

from argon2.low_level import Type, hash_secret_raw
from Crypto.Cipher import AES

journal_file = Path.home () / "journal.bin"


def unlock_journal (password : str) -> str :
    if not journal_file.exists () :
        return "No file found"
    data = journal_file.read_bytes ()

    salt = data [:16]
    key = hash_secret_raw (
        secret = password.encode (), salt = salt, time_cost = 3,
        memory_cost = 65536, parallelism = 4, hash_len = 32,
        type = Type.ID)

    return decrypt_journal (key)

def decrypt_journal (key : bytes) -> str :
    data = journal_file.read_bytes ()

    nonce = data [16:32]
    tag = data [32:48]
    ciphertext = data [48:]

    cipher = AES.new (key, AES.MODE_EAX, nonce = nonce)

    try :
        plaintext = cipher.decrypt_and_verify (ciphertext, tag)
        return plaintext.decode ()
    except ValueError :
        return ""