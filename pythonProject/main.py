# This is a sample Python script.
import random
from collections import Counter

from models.player import Player

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
num_turns = 0
current_turn_score = 0


def roll_dice(num_dice):
    dice_results = []
    for die in range(num_dice):
        dice_results.append(random.randint(1, 6))
    return dice_results


def choose_to_continue(player, dice_left, last_turn_score):
    # How do determine base threshold, this math is random atm
    return player.reward_points > last_turn_score * 1 / dice_left


def score(roll_result):
    print("SCORING")
    print(str(roll_result))
    count = Counter(roll_result)
    print(str(count))
    roll_points = 0
    num_dice = len(roll_result)
    for value, freq in count.items():
        if freq == 3:
            if value == 1:
                roll_points += 1000
                num_dice -= freq
            else:
                roll_points += 100*value
                num_dice -= freq
        elif freq > 3:
            if value == 1:
                roll_points += 1000 * (freq-3) * 2
                num_dice -= freq
        elif value == 1:
            roll_points += 100 * freq
            num_dice -= freq
        elif value == 5:
            roll_points += 50 * freq
            num_dice -= freq
    if roll_points == 0:
        num_dice = 0
    return roll_points, num_dice


def start_turn(player, dice_left, last_turn_score, first_roll):
    print("player " + player.name + " rolling.")
    global current_turn_score
    if dice_left == 0 or (player.total_points < 650 and first_roll):
        print("rolling all dice")
        roll_result = roll_dice(6)
        roll_score, dice_left_new = score(roll_result)
        print("rolled " + str(roll_score) + " now have " + str(dice_left_new) + " dice left.")
        if roll_score > 0:
            current_turn_score += roll_score
            print(str(current_turn_score) + " current score")
            return start_turn(player, dice_left_new, current_turn_score, False)
        else:
            print("Farkle with all dice, nice")
            current_turn_score = 0
            return 0, 0
    else:
        if first_roll or choose_to_continue(player, dice_left, last_turn_score):
            print("Might be first roll " + str(first_roll) + " or chose to continue.")
            roll_result = roll_dice(dice_left)
            roll_score, dice_left_new = score(roll_result)
            print("rolled " + str(roll_score) + " and now have " + str(dice_left_new) + " dice left")
            if roll_score > 0:
                current_turn_score += roll_score
                print(str(current_turn_score) + " current score")
                return start_turn(player, dice_left_new, current_turn_score, False)
            else:
                print("Farkle")
                current_turn_score = 0
                return 0, 0
        else:
            passing_score = current_turn_score
            current_turn_score = 0
            return passing_score, dice_left


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players = []
    player1 = Player("1")
    player2 = Player("2")
    player3 = Player("3")
    players.append(player1)
    players.append(player2)
    players.append(player3)
    no_winner = True
    dice_left = 0
    while no_winner:
        for player in players:
            result, dice_left = start_turn(player, dice_left, 0, True)
            print("player " + player.name + " turn over " + str(result) + " <- score--- dice left ->" + str(dice_left))
            if player.total_points > 650 or result >= 650:
                player.total_points += result
                player.reward_points += result
            elif player.total_points <= 650 and result < 650:
                player.reward_points -= 20
            if result == 0:
                player.reward_points -= 20
            if player.total_points >= 10000:
                no_winner = False
                print(players)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
