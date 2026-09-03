import config
from textual.app import App
from screens.home import HomeScreen

class HealthyHyprInstaller(App):
    CSS_PATH = "style.tcss"
    ENABLE_COMMAND_PALETTE = config.ENABLE_COMMAND_PALETTE

    SCREENS = {
        "home": HomeScreen,
    }

    BINDINGS = [ ("ctrl+c", "noop") ]

    def on_mount(self) -> None:
        self.push_screen("home")

if __name__ == "__main__":
    app = HealthyHyprInstaller()
    app.run()