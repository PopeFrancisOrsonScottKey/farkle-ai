import random


class Player:
    total_points = 0

    def roll_dice(self, num_dice):
        dice_results = []
        for die in range(num_dice):
            dice_results.append(random.randint(1, 6))
        return dice_results

    def end_turn(self, turn_points, dice_left):
        global num_turns
        global total_points
        if total_points or turn_points >= 650:
            total_points += turn_points
        num_turns += 1
