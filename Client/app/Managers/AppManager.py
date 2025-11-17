from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QStackedWidget

# WindowManager no longer needed here:
# from Client.app.Managers.WindowManager import WindowManager
from Client.app.Pages.DisplayPage import DisplayPage
from Client.app.Pages.DashBoard import DashBoard
from Client.app.Pages.SettingsPage import SettingsPage


class AppManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_pages()
        self._switch_page("main")  # start on main

    def _setup_window(self):
        """Configure main window properties"""
        self.setWindowTitle("MultiMediaManager")
        self.setMinimumSize(QSize(800,600))
        self.resize(1024, 768)

        #Create containers for pages
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

    def _setup_pages(self):
        #Create pages
        self.dashboard_page = DashBoard()
        self.display_page = DisplayPage()
        self.settings_page = SettingsPage()

        #Add pages to stack
        self.stack.addWidget(self.dashboard_page)    # index 0
        self.stack.addWidget(self.display_page) # index 1
        self.stack.addWidget(self.settings_page)# index 2

        # --- connect signals from page navigation ---
        # From MainPage: open DisplayPage for a given item
        self.dashboard_page.display_item_selected.connect(self._open_display_for_item)

        # (optional) if you still want generic navigate_to usage:
        self.dashboard_page.navigate_to.connect(self._switch_page)

        # Go back from DisplayPage / SettingsPage -> main
        self.display_page.navigate_to.connect(self._switch_page)
        self.settings_page.navigate_to.connect(self._switch_page)

    def _open_display_for_item(self, item_id: str):
        self.display_page.set_content(item_id)
        self._switch_page("display")

    def _switch_page(self, page_name: str):
        # Map page names to widgets
        if page_name == "dashboard":
            self.stack.setCurrentWidget(self.dashboard_page)
        elif page_name == "display":
            self.stack.setCurrentWidget(self.display_page)
        elif page_name == "settings":
            self.stack.setCurrentWidget(self.settings_page)
        else:
            raise ValueError(f"Unknown page: {page_name}")

    def close_event(self, event):
        # you can still call cleanup() on pages if you add logic there
        for page in (self.dashboard_page, self.display_page, self.settings_page):
            page.cleanup()
        event.accept()

    def resizeEvent(self, event):
        super().resizeEvent(event)