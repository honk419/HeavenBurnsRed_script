import pygetwindow as gw
import pynput.mouse as mouse
import pynput.keyboard as keyboard
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


def execute_round_process(game_round_entity):
    # # 获取窗口
    # game_window = gw.getWindowsWithTitle('HeavenBurnsRed')[0]
    #
    # # 激活并将窗口切换到前台
    # game_window.activate()

    time.sleep(1)

    # 模拟点击
    # mouse_controller.click(100, 100)

    # 模拟按键
    # keyboard_controller.press('w')
    # keyboard_controller.release('w')
    # keyboard_controller.tap('w')

    print(f"Executing {game_round_entity} immediately!")

    # position = 0 什么也不做，直接结束本回合
    if game_round_entity.position == 0:
        # 操作-结束本回合
        tap_key_with_delay(Key.enter)
        return

    # 操作-选中该角色
    tap_key_with_delay(str(game_round_entity.position))

    # swap_flag = True 转换角色
    print(f"swap_flag:{game_round_entity.swap_flag}")
    if game_round_entity.swap_flag:
        # 操作-交换位置
        tap_key_with_delay(str(int(game_round_entity.skill_swap_sequence)))
    # swap_flag = False 释放技能
    else:
        # 循环 game_round_entity.skill_swap_sequence 次
        print(f"skill_swap_sequence:{game_round_entity.skill_swap_sequence}")
        for _ in range(int(game_round_entity.skill_swap_sequence)):  # 执行 skill_swap_sequence 次循环
            # 操作-选中技能
            tap_key_with_delay(Key.down)

        # 操作-确认技能
        tap_key_with_delay(Key.enter)

        # 判断是否需要指定己方角色
        if 1 <= game_round_entity.skill_target_position <= 6:
            # 操作-指定角色
            tap_key_with_delay(str(int(game_round_entity.skill_target_position)))

    # 判断是否结束本回合
    if game_round_entity.execute:
        # 操作-结束本回合
        tap_key_with_delay(Key.enter)
    # 等待时间
    time.sleep(game_round_entity.wait_time_seconds)


class ExecuteRoundProcess:
    # game_round_entity = GameRoundEntity.GameRoundEntity(2, 2, True, 4, 1, False, 0.5)
    # execute_round_process(game_round_entity)
    pass
