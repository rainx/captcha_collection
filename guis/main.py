import sys
import os

cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(cur_path)
sys.path.insert(0, cur_path)

from guis.MainWindowUIExt import MainWindowUIExt
from PySide import QtGui
import sys


def cli():
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowUIExt({})
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    cli();