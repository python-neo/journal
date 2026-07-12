from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, TextArea

from .authentication import unlock_journal
from .prompt import Prompt

BASE_DIR = Path (__file__).resolve ().parent

class Journal (App) :
    CSS = (BASE_DIR / "styles.tss").read_text ()
    BINDINGS = [Binding ("ctrl+q", "quit", "Quit.")]

    def compose (self) -> ComposeResult :
        yield Header (id = "header", show_clock = True)
        yield TextArea (id = "main")

    def on_mount (self) -> None :
        self.push_screen (Prompt ("Enter master password :-"), self.password_entered)

    def password_entered (self, password : str | None) -> None :
        if password is None :
            self.exit ()
            return

        journal = unlock_journal (password)

        if journal == "" :
            self.notify ("Incorrect password.", severity = "error")
            self.push_screen (Prompt ("Enter master password :-"), self.password_entered)
            return

        self.query_one (TextArea).text = journal
        self.notify ("Journal unlocked.", severity = "information")

    def action_quit (self) -> None :
        self.exit ()

def main () -> None :
    journal = Journal ()
    journal.run ()

if __name__ == "__main__" :
    main ()