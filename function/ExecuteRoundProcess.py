import pygetwindow as gw
import pynput.mouse as mouse
import pynput.keyboard as keyboard
from pynput.keyboard import Key
from standard.utils import ComparePicUtil
import time

# 模拟输入
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()


def tap_key_with_delay(tap_key):
    keyboard_controller.tap(tap_key)
    # 等待 0.5 秒
    time.sleep(0.5)


def start(game_round_entity):
    time.sleep(1)
    print(f"Executing {game_round_entity} immediately!")

    # position = 0 什么也不做，直接结束本回合
    if game_round_entity.position == 0:
        # 操作-结束本回合
        tap_key_with_delay(Key.enter)

        # 等待结束时间
        ComparePicUtil.wait_for_friend_round()
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
        for _ in range(int(game_round_entity.skill_swap_sequence)):
            # 执行 skill_swap_sequence 次循环
            # 操作-选中技能
            tap_key_with_delay(Key.down)

        # 操作-确认技能
        tap_key_with_delay(Key.enter)

        # 判断是否需要指定己方角色
        if 1 <= game_round_entity.skill_target_position <= 6:
            # 操作-指定角色
            tap_key_with_delay(str(int(game_round_entity.skill_target_position)))

    # 等待结束时间
    ComparePicUtil.wait_for_friend_round()

    # 判断是否结束本回合
    if game_round_entity.execute:
        # 操作-结束本回合
        tap_key_with_delay(Key.enter)


class ExecuteRoundProcess:
    # game_round_entity = GameRoundEntity.GameRoundEntity(2, 2, True, 4, 1, False, 0.5)
    # execute_round_process(game_round_entity)
    pass
