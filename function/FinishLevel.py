from standard.entity import GameRoundEntity
from function import ExecuteFinishProcess
import pygetwindow as gw
import time


def start():
    # # 获取窗口
    # game_window = gw.getWindowsWithTitle('HeavenBurnsRed')[0]
    # # 激活并将窗口切换到前台
    # game_window.activate()

    # 执行游戏脚本
    ExecuteFinishProcess.start()

    # 等待加载时间
    time.sleep(15)

class FinishLevel:
    pass