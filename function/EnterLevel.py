from standard.entity import GameRoundEntity
import ExecuteRoundProcess
import pygetwindow as gw


def start(df):
    # 获取窗口
    game_window = gw.getWindowsWithTitle('HeavenBurnsRed')[0]
    # 激活并将窗口切换到前台
    game_window.activate()

    # 创建一个空列表来存储 GameRound 对象
    game_rounds = []
    max_round_number = 0

    # 遍历每一行数据，并创建对应的 GameRound 对象
    for _, row in df.iterrows():
        # 创建 GameRound 对象
        game_round = GameRoundEntity.GameRoundEntity(
            round_number=row['round_number'],
            position=row['position'],
            swap_flag=row['swap_flag'],
            skill_swap_sequence=row['skill_swap_sequence'],
            skill_target_position=row['skill_target_position'],
            execute=row['execute'],
            wait_time_seconds=row['wait_time_seconds']
        )
        max_round_number = row['round_number']
        # 将对象添加到列表
        game_rounds.append(game_round)

    # 执行游戏脚本,遍历 game_rounds 列表
    execute_round_process = ExecuteRoundProcess
    for game_round in game_rounds:
        # 分步执行脚本命令
        execute_round_process.execute_round_process(game_round)

class EnterLevel:
    pass
