from PySide6.QtWidgets import QWidget
from ui.widget_3WaySlider_ui import Ui_ThreeWaySlider


class ThreeWaySlider(QWidget, Ui_ThreeWaySlider):
    def __init__(self) -> None:
        super(ThreeWaySlider, self).__init__()
        self.setupUi(self)
