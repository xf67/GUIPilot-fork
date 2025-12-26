import numpy as np

from guipilot.entities.constants import Bbox
from guipilot.entities.process import Process
from guipilot.entities.screen import Screen
from guipilot.entities.widget import Widget, WidgetType


def test_add_screen():
    process = Process()
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    bbox = Bbox(10, 10, 50, 50)
    widget = Widget(type=WidgetType.TEXT_BUTTON, bbox=bbox)

    widgets = {0: widget}

    screen = Screen(image=image, widgets=widgets)

    process.add(screen)

    assert len(process.screens) == 1  # 确保 screens 列表中有一个元素
    assert process.screens[0] is screen  # 确保添加的元素是我们创建的 screen 实例
