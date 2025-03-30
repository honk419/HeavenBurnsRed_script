class GameRoundEntity:
    def __init__(self, round_number, position, swap_flag, skill_swap_sequence, skill_target_position, execute):
        self.round_number = round_number  # 回合数
        self.position = position  # 位置
        self.swap_flag = swap_flag  # 换位标志
        self.skill_swap_sequence = skill_swap_sequence  # 技能/换位顺序
        self.skill_target_position = skill_target_position  # 技能指定位置
        self.execute = execute  # 执行标志

    def __repr__(self):
        return (f"GameRound(round_number={self.round_number}, position={self.position}, "
                f"swap_flag={self.swap_flag}, skill_swap_sequence={self.skill_swap_sequence}, "
                f"skill_target_position={self.skill_target_position}, execute={self.execute}) ")

