#  Copyright (c) 2024. Sergii Nechuiviter

from textual.app import App

from screens.main_screen import MainScreen
from screens.quit_screen import QuitScreen


class ChatApp(App):
    """A pet chat application."""

    BINDINGS = [("q", "request_quit", "Quit")]

    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""

        def quit_screen_callback(result: bool) -> None:
            """Called when QuitScreen is dismissed."""
            if result:
                self.exit()

        self.push_screen(QuitScreen(), quit_screen_callback)


if __name__ == "__main__":
    # entrance point of terminal application, so you can pass params here
    app = ChatApp()
    app.run()
