
import random
class SnakeNLadder:

# UC2 : The Player rolls the die to get a number between 1 to 6.

	def start_game(self):
		player1 = 0
		roll_die = random.randint(1, 6)
		print("Start Position Of Player1 :", player1)
		print("Player roll die : ", roll_die)

print("Welcome to Snake and Ladder..!")
uc1 = SnakeNLadder()
uc1.start_game()