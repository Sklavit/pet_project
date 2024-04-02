#  Copyright (c) 2024. Sergii Nechuiviter

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer

from widgets.chats_list import ChatsList
from widgets.chat_messages import ChatMessages


class MainScreen(Screen):
    BINDINGS = [
        ("c", "clear_chat", "Clear chat"),
    ]

    def action_clear_chat(self) -> None:
        """Called clear chat from all messages."""
        # TODO this is just example
        # TODO rename all messages to utterances
        utterance = self.query("Utterance")
        if utterance:
            utterance.remove()

    def compose(self) -> ComposeResult:
        yield ChatsList(id="Chats_list")
        yield ChatMessages(id="Chat_messages")
        yield Footer()
