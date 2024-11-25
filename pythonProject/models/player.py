class Player:
    total_points = 0
    reward_points = 200
    name = ""

    def __init__(self, name):
        self.name = name

    def end_turn(self, turn_points, dice_left):
        global num_turns
        global total_points
        if total_points or turn_points >= 650:
            total_points += turn_points
        num_turns += 1
