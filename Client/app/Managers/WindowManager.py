from typing import Optional

from Client.app.Pages.PageWidget import PageWidget
"""
Currently not being used however it is still in the project incase page navigation or management get more complicated 
and a dedicated manager is needed
"""

class WindowManager:
    def __init__(self):
        self._pages: dict[str, PageWidget] = {}
        self._current_page: Optional[str] = None

    def register_page(self, name: str, page: PageWidget):
        """Register a new page with the window manager"""
        self._pages[name] = page

    def switch_to(self, page_name: str) -> None:
        """Switch to a different page"""
        if page_name not in self._pages:
            raise ValueError(f"Page '{page_name}' not found")

        """Hide the currently displayed page"""
        if self._current_page in self._pages:
            self._pages[self._current_page].hide()

        """Display the new page and set it to the current page"""
        self._pages[page_name].show()
        self._current_page = page_name

    def get_current_page(self) -> Optional[str]:
        """Get the name of the currently displayed page"""
        return self._current_page

    def remove_page(self, page_name: str) -> None:
        """Remove a page from the window manager"""
        if page_name not in self._pages:
            raise ValueError(f"Page '{page_name}' not found")

        """Hide the page"""
        self._pages[page_name].hide()

        """Remove the page from the window manager"""
        del self._pages[page_name]