import sys

import PySide2
import PySide2.QtWidgets

from qt_starter import views


if __name__ == "__main__":

    app = PySide2.QtWidgets.QApplication([])

    main = views.MainWindow()
    main.show()

    sys.exit(app.exec_())
