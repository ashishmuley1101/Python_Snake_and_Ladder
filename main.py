
import random
class SnakeNLadder:

	STARTINGPOSITION = 0;
	ENDINGPOSITION = 100;


	# def __init__(self, STARTINGPOSITION,ENDINGPOSITION):
	# 	self.ENDINGPOSITION = ENDINGPOSITION
	# 	self.STARTINGPOSITION = STARTINGPOSITION

	def start_game(self):
		current_position = 0
		print("Start Position Of Player :", current_position)

# UC 4: The Player reaches the winning position 100.

		if current_position < SnakeNLadder.ENDINGPOSITION:
			# for position in range(SnakeNLadder.ENDINGPOSITION):
				while current_position < SnakeNLadder.ENDINGPOSITION:
					roll_die = random.randint(1, 6)
					option = random.randint(1, 3)
					if option == 1:
						if current_position + roll_die <= SnakeNLadder.ENDINGPOSITION :
							current_position = current_position + roll_die;
							print("Dies roll : ", roll_die)
							print("Ladder : ", option)
							print("Current position : ", current_position)
					elif option == 2:
						if current_position - roll_die >= SnakeNLadder.STARTINGPOSITION:
							current_position = current_position - roll_die
							print("Dies roll : ", roll_die)
							print("Snake : ", option)
							print("Current position : ", current_position)
					else:
						if current_position == current_position:
								current_position = current_position
								print("Dies roll : ", roll_die)
								print("No Play : ", option)
								print("Current position : ", current_position)

print("Welcome to Snake and Ladder..!")
uc1 = SnakeNLadder()
uc1.start_game()