#  Copyright (c) 2024. Sergii Nechuiviter

from textual.app import App

from screens.main_screen import MainScreen
from screens.quit_screen import QuitScreen


class ChatApp(App):
    """A pet chat application."""

    # CSS_PATH = "chat.tcss"

    BINDINGS = [("q", "request_quit", "Quit")]

    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""

        def check_quit(quit: bool) -> None:
            """Called when QuitScreen is dismissed."""
            if quit:
                self.exit()

        self.push_screen(QuitScreen(), check_quit)


if __name__ == "__main__":
    # entrance point of terminal application, so you can pass params here
    app = ChatApp()
    app.run()
