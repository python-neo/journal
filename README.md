# Journal

A secure, encrypted journal for the terminal, written in Python and powered by
Textual.

Journal provides a clean terminal interface for writing and managing private
journal entries. Journal contents are encrypted using AES in EAX mode, with
encryption keys derived from your master password using Argon2id. Only the
encrypted journal is stored on disk.

## Features

* 🔒 Master password authentication
* 🔐 AES-EAX authenticated encryption
* 🔑 Argon2id key derivation
* 📝 Create and edit journal entries
* 💾 Save journal with `Ctrl+S`
* 🚪 Save and quit with `Ctrl+Q`
* 💻 Modern terminal interface powered by Textual

## Installation

```bash
git clone https://github.com/python-neo/journal.git
cd journal

python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # macOS / Linux
python -m pip install -e .
python -m pip install -e .[dev] # For ruff
```

## Running

```bash
journal
```

On first launch, Journal prompts you to create a master password and initializes
an encrypted journal. On subsequent launches, the same password is required to
unlock the journal.

## Project Structure

```text
journal/
├── journal/
│   ├── authentication.py
│   ├── main.py
│   ├── prompt.py
│   ├── styles.tss
│   └── __init__.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── pyproject.toml
```

## How It Works

* A random salt is generated when the journal is created.
* Argon2id derives a 256-bit encryption key from your master password.
* The journal is encrypted using AES in EAX mode, providing both
  confidentiality and integrity.
* The journal file stores:

```text
salt (16 bytes)
nonce (16 bytes)
authentication tag (16 bytes)
ciphertext
```

## Requirements

* Python 3.12 or later

## Dependencies

* Textual
* pycryptodome
* argon2-cffi

## License

This project is licensed under the GNU General Public License v3.0. See the
`LICENSE` file for details.
