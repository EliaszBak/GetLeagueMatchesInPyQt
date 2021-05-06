from PySide6 import QtWidgets
from Gui import UI
from controller import Controller


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI()
    ui.setupUi(MainWindow)
    Controller(view=ui)
    MainWindow.show()
    sys.exit(app.exec_())

