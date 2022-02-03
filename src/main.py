import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, size: QtCore.QSize, title: str, icon: QtGui.QIcon,
                 parent: QtWidgets.QWidget | None = None):
        super().__init__(parent=parent)

        self.resize(size)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)

        self.setup_shortcuts()
        self.setup_ui()

    def setup_shortcuts(self):
        """Add shortcuts to the program"""

    def setup_ui(self):
        """Add graphical elements to the program"""


def main():
    app = QtWidgets.QApplication(sys.argv)

    size = QtCore.QSize(1920, 1080)
    title = "Test Window"
    icon = QtGui.QIcon("")

    window = MainWindow(size, title, icon)
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
