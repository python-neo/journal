from textual.widgets import Header, TextArea
from textual.app import App
from pathlib import Path
from textual.binding import Binding

BASE_DIR = Path (__file__).resolve ().parent

class Journal (App) :
    CSS = (BASE_DIR / "styles.tss").read_text ()
    BINDINGS = [Binding ("Ctrl+Q", "quit", "Quit.")]
    
    def compose (self) :
        yield Header (id = "header", show_clock = True)
        yield TextArea (id = "main")

    def action_quit (self) :
        self.exit ()

def main () :
    journal = Journal ()
    journal.run ()

if __name__ == "__main__" :
    main ()