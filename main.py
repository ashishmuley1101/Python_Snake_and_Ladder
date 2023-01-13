
import random
class SnakeNLadder:

	STARTINGPOSITION = 0;
	ENDINGPOSITION = 100;
	roll_die = 0




	def start_game(self):

		current_position = 0
		print("Start Position Of Player :", current_position)

# UC 6: The number of times the dice was played to win the game and also the position after every die role.

		if current_position < SnakeNLadder.ENDINGPOSITION:

				count = 0

				while current_position < SnakeNLadder.ENDINGPOSITION:

					roll_die = random.randint(1, 6)

					option = random.randint(1, 3)

					if option == 1:
						if current_position + roll_die <= SnakeNLadder.ENDINGPOSITION :
							current_position = current_position + roll_die;
							print("Dies Roll  : ", roll_die)
							print("Ladder : ", option)
							print("Current position : ", current_position)

					elif option == 2:
						if current_position - roll_die >= SnakeNLadder.STARTINGPOSITION:
							current_position = current_position - roll_die
							print("Dies Roll : ", roll_die)
							print("Snake : ", option)
							print("Current position : ", current_position)

					else:
						if current_position == current_position:
								current_position = current_position
								print("Dies Roll : ", roll_die)
								print("No Play : ", option)
								print("Current position : ", current_position)

					count += 1

				if current_position == 100:
					print("\nPlayer Winner at position 100.")

				print("Number of times the dice was played : ", count)

print("Welcome to Snake and Ladder..!")
sl1 = SnakeNLadder()
sl1.start_game()