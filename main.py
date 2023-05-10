import sys
from PyQt5.QtWidgets import (QApplication, QDialog)

from LoginPage import LoginDialog
from LibraryPage import LibraryPage


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_dialog = LoginDialog()

    if login_dialog.exec_() == QDialog.Accepted:
        library = LibraryPage()
        library.show()
        sys.exit(app.exec_())

