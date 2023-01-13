
import random
class SnakeNLadder:


	def start_game(self):
		player1 = 0
		roll_die = random.randint(1, 6)
		print("Start Position Of Player1 :", player1)
		print("Die Roll : ", roll_die)

# UC 3: The Player then checks for a Option. They are No Play,Ladder or Snake.

		option = random.randint(1, 3)
		if option == 1:
			player1 = player1 + roll_die
			print("Player got ladder : ", player1)
		elif option == 2:
			player1 = player1 - roll_die
			print("Player got snake : ", player1)
		else:
			player1 = player1
			print("Player not played : ", player1)

print("Welcome to Snake and Ladder..!")
uc1 = SnakeNLadder()
uc1.start_game()