# Copyright 2024 Sergii Nechuiviter

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder


class ChatsList(Placeholder):
    DEFAULT_CSS = """
    ChatsList {
        width: 25vw;
        dock: left;
        border: solid white;
    }
    """


class Tweet(Placeholder):
    DEFAULT_CSS = """
    Tweet {
        margin: 2 0;
    }
    """


class UserInput(Placeholder):
    DEFAULT_CSS = """
    UserInput {
        height: 3;
        # dock: right;
        border: solid white;
    }
    """


class Column(VerticalScroll):
    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")


class ChatMessages(Placeholder):
    DEFAULT_CSS = """
    ChatMessages {
        width: 75vw;
        dock: right;
        border: solid white;
    }
    """

    def compose(self) -> ComposeResult:
        yield Column(id="messages")
        yield UserInput(id="input_place")


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield ChatsList(id="Chats_list")
        yield ChatMessages(id="Chat_messages")


class ChatApp(App):
    """A working 'desktop' calculator."""

    # CSS_PATH = "chat.tcss"

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


if __name__ == "__main__":
    # entrance point of cli application
    app = ChatApp()
    app.run()
