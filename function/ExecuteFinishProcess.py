import pygetwindow as gw
import pynput.mouse as mouse
import pynput.keyboard as keyboard
from pynput.mouse import Button

from pynput.keyboard import Key
from standard.entity import GameRoundEntity
import time


# 模拟输入
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()


def tap_key_with_delay(tap_key):
    keyboard_controller.tap(tap_key)
    # 等待 0.5 秒
    time.sleep(0.5)


def start():
    print(f"Executing ExecuteFinishProcess immediately!")

    game_window = gw.getWindowsWithTitle('HeavenBurnsRed')[0]

    x, y = game_window.left, game_window.top  # 左上角坐标
    width, height = game_window.width, game_window.height  # 窗口大小

    center_x = x + width // 2
    center_y = y + height // 2

    mouse_controller.position = (center_x, center_y)

    # 操作-跳过升级页面
    for _ in range(10):
        mouse_controller.click(Button.left,1)
        time.sleep(0.3)

    time.sleep(1)

    # 操作-再战
    tap_key_with_delay(Key.enter)

    time.sleep(1)

    # 操作加生命石
    for _ in range(4):
        tap_key_with_delay(Key.right)
        time.sleep(0.2)

    # 操作-确认
    tap_key_with_delay(Key.enter)

    time.sleep(1)

    # 消耗预备生命石
    for _ in range(2):
        tap_key_with_delay(Key.right)
        time.sleep(1)

    # 操作-确认
    tap_key_with_delay(Key.enter)

    time.sleep(1)

    # 操作-确认
    tap_key_with_delay(Key.enter)

    time.sleep(1)

    # 操作-确认
    tap_key_with_delay(Key.enter)

class ExecuteFinishProcess:
    # game_round_entity = GameRoundEntity.GameRoundEntity(2, 2, True, 4, 1, False, 0.5)
    # execute_round_process(game_round_entity)
    pass
