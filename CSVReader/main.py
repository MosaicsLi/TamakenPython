import sys
from PyQt6 import QtWidgets
from Logic.Logic import MainWindowLogic

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowLogic()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()