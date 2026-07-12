from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Input

class Prompt (ModalScreen [str | None]) :
    BINDINGS = [Binding ("escape", "cancel", "Cancel")]

    def __init__ (self, message : str) -> None :
        super ().__init__ ()
        self.message = message

    def compose (self) -> ComposeResult :
        with Vertical (id = "dialog") :
            yield Input (placeholder = self.message, id = "input")

    def on_input_submitted (self, event : Input.Submitted) -> None :
        self.dismiss (event.value)

    def action_cancel (self) -> None :
        self.dismiss (None)