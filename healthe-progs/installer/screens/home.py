from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button

class HomeScreen(Screen):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "to-settings":
            self.app.push_screen("settings")