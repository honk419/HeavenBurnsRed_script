import time
import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import os

def get_game_screenshot(dx,dy,dHidth,dHeight):
    """ 截取游戏窗口的屏幕截图 """
    game_window = gw.getWindowsWithTitle('HeavenBurnsRed')[0]
    if not game_window:
        print("❌ 未找到游戏窗口")
        return None

    game_window.activate()  # 获取窗口
    x, y, width, height = game_window.left + dx, game_window.top+dy, dHidth, dHeight

    time.sleep(1)

    # 使用 pyautogui 截图
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)  # 转换为 OpenCV 格式
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换为 BGR 格式

    return screenshot

def find_target_on_screen( dx, dy, d_width, d_height):
    """ 在游戏窗口截图中查找目标图片 """
    screenshot = get_game_screenshot(dx, dy, d_width, d_height)
    if screenshot is None:
        return False

    # 读取目标图片
    target = cv2.imread("statics/matchPics/startActionButton.png", cv2.IMREAD_COLOR)

    if target is None:
        print("❌ 无法加载目标图片")
        return False

    # 使用 OpenCV 模板匹配
    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果匹配度大于阈值，返回坐标
    if max_val >= 0.8:
        target_x, target_y = max_loc
        print(f"✅ 找到目标图片，位置: ({target_x}, {target_y})")
        return True
    else:
        print("❌ 未找到目标图片")
        return False
