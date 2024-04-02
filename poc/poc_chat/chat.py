# Copyright 2024 Sergii Nechuiviter

from textual.app import App, ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Placeholder, Button, Footer


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
        width: 80%;
        border: solid white;
    }
    """


class Column(ScrollableContainer):  # VerticalScroll):
    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 2):
            yield Tweet(id=f"Tweet{tweet_no}")


class SendButton(Button):
    DEFAULT_CSS = """
    SendButton {
        width: 10;
        height: 3;
    }
    """


class ChatMessages(Placeholder):
    DEFAULT_CSS = """
    ChatMessages {
        width: 75vw;
        dock: right;
        border: solid white;
    }
    """

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "send":
            new_message = Tweet()
            self.query_one("#messages").mount(new_message)
            new_message.scroll_visible()  # scroll_visible is not working

            # (self.get_child_by_id("messages")
            # .compose_add_child(  # TODO use something else
            #     Tweet()
            # ))

    def compose(self) -> ComposeResult:
        yield Column(id="messages")
        # with Horizontal():
        #     yield UserInput(id="input_place")
        #     yield SendButton("Send", id="send", variant="success")
        input_container = Horizontal(
            UserInput(id="input_place"),
            SendButton("Send", id="send", variant="success")
        )
        input_container.height = 5
        yield input_container


class MainScreen(Screen):
    BINDINGS = [
        ("c", "clear_chat", "Clear chat"),
    ]

    def on_mount(self) -> None:
        self.log.debug("Logged via TextualHandler")

    def action_clear_chat(self) -> None:
        """Called to remove a timer."""
        timers = self.query("Tweet")
        if timers:
            timers.remove()

    def compose(self) -> ComposeResult:
        yield ChatsList(id="Chats_list")
        yield ChatMessages(id="Chat_messages")
        yield Footer()


class ChatApp(App):
    """A working 'desktop' calculator."""

    # CSS_PATH = "chat.tcss"

    # BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    #
    # def compose(self) -> ComposeResult:
    #     """Create child widgets for the app."""
    #     yield Header()
    #     yield Footer()
    #
    # def action_toggle_dark(self) -> None:
    #     """An action to toggle dark mode."""
    #     self.dark = not self.dark

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


if __name__ == "__main__":
    # entrance point of cli application
    app = ChatApp()
    app.run()
