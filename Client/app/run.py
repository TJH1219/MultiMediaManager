import sys
from PySide6.QtWidgets import QApplication

from Managers.AppManager import AppManager

def main():
    app = QApplication(sys.argv)

    window = AppManager()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()