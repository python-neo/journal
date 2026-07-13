# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-07-13

### Added

- `encrypt_journal` to save your changes.
- A new `Ctrl + S` shortcut to save.
- Automatic save upon quitting.
- Better new file and password error support.
- Binaries in `make` folder.

### Removed

- `File not found` message loading into the editor.

### Changed

- Refactored earlier `authentication.py` with clean functions.

## [0.1.0] - 2026-07-12

### Added

- Startup password prompt.
- AES-EAX journal decryption.
- Argon2-based key derivation for unlocking the journal.
- Initial journal unlock flow.

### Changed

- Improved the application structure in preparation for encrypted journal storage.

## [0.0.1] - 2026-07-12

### Added

- Documentation for the project.
- A basic `Textual` app.
- License (GNU General Public License v3.0).

[Unreleased]: https://github.com/python-neo/journal/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/python-neo/journal/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/python-neo/journal/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/python-neo/journal/releases/tag/v0.0.1
