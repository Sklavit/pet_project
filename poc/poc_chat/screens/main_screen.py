#  Copyright (c) 2024. Sergii Nechuiviter

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer

from widgets.chats_list import ChatsList
from widgets.chat_messages import ChatMessages


class MainScreen(Screen):
    """Main screen of the Chat app with chats."""

    BINDINGS = [
        ("c", "clear_chat", "Clear chat"),
    ]

    def action_clear_chat(self) -> None:
        """Clear chat from all messages."""
        # TODO this is just example
        # TODO rename all messages to utterances
        utterance = self.query("Message")
        if utterance:
            utterance.remove()

    def compose(self) -> ComposeResult:
        """Content of the main screen."""
        yield ChatsList(id="Chats_list")
        yield ChatMessages(id="Chat_messages")
        yield Footer()
