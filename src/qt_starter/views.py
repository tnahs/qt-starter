import PySide2
import PySide2.QtCore
import PySide2.QtWidgets


"""
classes PascalCase
functions snake_case
constants SNAKE_CASE_UPPER
private _starts_with_underscore
"""


class MainWindow(PySide2.QtWidgets.QFrame):
    def __init__(self) -> None:
        super().__init__(parent=None)

        self._init_ui()

    def _init_ui(self) -> None:

        # self.setFixedSize(512, 256)
        self.setWindowTitle("Qt Starter")

        self._label = PySide2.QtWidgets.QLabel("Click a button!")
        self._label.setAlignment(PySide2.QtCore.Qt.AlignCenter)

        self._button_a = PySide2.QtWidgets.QPushButton("Button A")
        self._button_a.clicked.connect(lambda: self._on_button_clicked("A"))

        self._button_b = PySide2.QtWidgets.QPushButton("Button B")
        self._button_b.clicked.connect(lambda: self._on_button_clicked("B"))

        layout_buttons = PySide2.QtWidgets.QHBoxLayout()
        layout_buttons.addWidget(self._button_a)
        layout_buttons.addWidget(self._button_b)

        layout = PySide2.QtWidgets.QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(10)
        layout.addSpacing(10)
        layout.addWidget(self._label)
        layout.addLayout(layout_buttons)

        self.setStyleSheet(
            """
            QPushButton {
                font-size: 12pt;
            }
            QLabel {
                font-size: 12pt;
            }
        """
        )

        self.setLayout(layout)

    def _on_button_clicked(self, string):
        self._label.setText(f"{string} Clicked!")
