import sys

import PySide6
import PySide6.QtWidgets

from qt_starter import views


if __name__ == "__main__":

    app = PySide6.QtWidgets.QApplication([])

    main = views.MainWindow()
    main.show()

    sys.exit(app.exec())
