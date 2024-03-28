# Copyright 2024 Sergii Nechuiviter

from textual.app import App


class ChatApp(App):
    """A working 'desktop' calculator."""

    CSS_PATH = "chat.tcss"


if __name__ == "__main__":
    # entrance point of cli application
    app = ChatApp()
    app.run()
