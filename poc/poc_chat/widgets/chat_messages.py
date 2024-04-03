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
            new_message = Message()
            self.query_one("#messages").mount(new_message)
            new_message.scroll_visible()  # TODO scroll_visible is not working ? use VerticalScroll?
            # TODO use Log instead of extra components ?

    def compose(self) -> ComposeResult:
        """Content of the Chat Messages widget."""
        yield Column(id="messages")
        input_container = Horizontal(
            UserInput(id="input_place", placeholder="What do you want to say?"),
            SendButton("Send", id="send", variant="success")
        )
        input_container.height = 5  # not working TODO use styles
        yield input_container

    def on_mount(self) -> None:
        self.query_one(SendButton).tooltip = "Send the message to the chat"


class Column(ScrollableContainer):  # VerticalScroll):  # TODO will it fix scroll_visible?
    def compose(self) -> ComposeResult:
        for i in range(1, 3):
            yield Message(id=f"Message{i}")


class UserInput(Input):
    DEFAULT_CSS = """
    UserInput {
        height: 3;
        width: 80%;
        border: solid white;
    }
    """


class Message(Label):
    """Representation of the message in the chat."""
    DEFAULT_CSS = """
    Message {
        border: solid;
    }
    """

    def on_mount(self) -> None:
        self.update(str(self.id))


class SendButton(Button):
    """Button for sending the message to the chat."""

    DEFAULT_CSS = """
    SendButton {
        width: 10;
        height: 3;
    }
    """
