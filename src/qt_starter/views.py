import PySide6
import PySide6.QtCore
import PySide6.QtWidgets


"""
classes PascalCase
functions snake_case
constants SNAKE_CASE_UPPER
private _starts_with_underscore
"""


class MainWindow(PySide6.QtWidgets.QFrame):
    def __init__(self) -> None:
        super().__init__(parent=None)

        self._init_ui()

    def _init_ui(self) -> None:

        self.setFixedSize(512, 256)
        self.setWindowTitle("Qt Starter")

        self._label = PySide6.QtWidgets.QLabel("Click a button!")
        self._label.setAlignment(PySide6.QtCore.Qt.AlignCenter)

        button_a = PySide6.QtWidgets.QPushButton("Button A")
        button_a.clicked.connect(lambda: self._on_button_clicked("A"))
        button_a.click

        button_b = PySide6.QtWidgets.QPushButton("Button B")
        button_b.clicked.connect(lambda: self._on_button_clicked("B"))

        layout_buttons = PySide6.QtWidgets.QHBoxLayout()
        layout_buttons.addWidget(button_a)
        layout_buttons.addWidget(button_b)

        layout = PySide6.QtWidgets.QVBoxLayout()
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
                font-size: 24pt;
            }
        """
        )

        self.setLayout(layout)

    def _on_button_clicked(self, string):
        self._label.setText(f"Clicked button {string}!")
