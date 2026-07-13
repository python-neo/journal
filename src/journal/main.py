from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea

from .authentication import (decrypt_journal, encrypt_journal, generate_key,
                             verify_journal)
from .prompt import Prompt


BASE_DIR = Path (__file__).resolve ().parent

class Journal (App) :
    CSS = (BASE_DIR / "styles.tss").read_text ()
    BINDINGS = [Binding ("ctrl+q", "quit", "Quit.", priority = True),
                Binding ("ctrl+s", "save", "Save")]

    def compose (self) -> ComposeResult :
        yield Header (id = "header", show_clock = True)
        yield TextArea (id = "main")

    def on_mount (self) -> None :
        if not verify_journal () :
            self.notify ("This will create a new journal file.\n"
                         "Choose a strong password, preferably a collection "
                         "of random words and numbers such as:\n"
                         "henry lukas moon weird sisters 25",
                         severity = "information")
        self.push_screen (Prompt ("Enter master password :-"), self.password_entered)

    def password_entered (self, password : str | None) -> None :
        if password is None :
            self.exit ()
            return

        self.key = generate_key (password)

        try :
            journal = decrypt_journal (self.key)
        except ValueError :
            self.notify ("Incorrect password.", severity = "error")
            self.push_screen (Prompt ("Enter master password :-"), self.password_entered)
            return

        if journal == "" :
            self.notify ("Created a new journal.", severity = "information")
        else :
            self.notify ("Journal unlocked.", severity = "information")

        self.query_one (TextArea).text = journal

    def action_quit (self) -> None :
        self.action_save (quitting = True)
        self.exit ()

    def action_save (self, quitting = False) -> None :
        if not hasattr (self, "key") :
            return

        encrypt_journal (self.query_one (TextArea).text, self.key)

        if not quitting :
            self.notify ("Saved journal.")

def main () -> None :
    journal = Journal ()
    journal.run ()

if __name__ == "__main__" :
    main ()