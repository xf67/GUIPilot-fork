from guipilot.entities.process import Process
from guipilot.entities.screen import Screen  # 假设 Screen 类在这个路径下


def test_add_screen():
    process = Process()
    screen = Screen()  # 创建一个 Screen 实例

    process.add(screen)  # 调用 add 方法

    assert len(process.screens) == 1  # 确保 screens 列表中有一个元素
    assert process.screens[0] is screen  # 确保添加的元素是我们创建的 screen 实例
