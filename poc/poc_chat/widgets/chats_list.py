#  Copyright (c) 2024. Sergii Nechuiviter

from textual.widgets import Placeholder


class ChatsList(Placeholder):
    DEFAULT_CSS = """
    ChatsList {
        width: 25vw;
        dock: left;
        border: solid white;
    }
    """
