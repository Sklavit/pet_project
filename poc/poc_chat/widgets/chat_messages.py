#  Copyright (c) 2024. Sergii Nechuiviter

from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Placeholder, Button, Input, Label


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
            new_message = Utterance()
            self.query_one("#messages").mount(new_message)
            new_message.scroll_visible()  # scroll_visible is not working

            # (self.get_child_by_id("messages")
            # .compose_add_child(  # TODO use something else
            #     Utterance()
            # ))

    def compose(self) -> ComposeResult:
        yield Column(id="messages")
        # with Horizontal():
        #     yield UserInput(id="input_place")
        #     yield SendButton("Send", id="send", variant="success")
        input_container = Horizontal(
            UserInput(id="input_place", placeholder="What do you want to say?"),
            SendButton("Send", id="send", variant="success")
        )
        input_container.height = 5
        yield input_container

    def on_mount(self) -> None:
        self.query_one(SendButton).tooltip = "Send the message to the chat"


class Column(ScrollableContainer):  # VerticalScroll):
    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 2):
            yield Utterance(id=f"Utterance{tweet_no}")


class UserInput(Input):
    DEFAULT_CSS = """
    UserInput {
        height: 3;
        width: 80%;
        border: solid white;
    }
    """


class Utterance(Label):
    DEFAULT_CSS = """
    Utterance {
        border: solid;
    }
    """

    def on_mount(self) -> None:
        self.update(str(self.id))


class SendButton(Button):
    DEFAULT_CSS = """
    SendButton {
        width: 10;
        height: 3;
    }
    """
