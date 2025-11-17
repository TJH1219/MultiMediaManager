from typing import Protocol, Optional

class PageWidget(Protocol):

    def show(self) -> None:
        ...

    def hide(self) -> None:
        ...

    def cleanup(self) -> None:
        ...