# This file defines a risk environment for reinforcement learning

import tensorflow as tf
import numpy as np
import random
import time
import matplotlib as plot
import sys
import argparse

class Risk_Env():
	# This class defines an environment with which an agent can interact
	# The environment is based on the Risk board game
	# KEY ASSUMPTION: The agent will act optimally for a single battle

	def __init__(self, board):
		# This is the constructor for the Risk_Env class
		# Arguments:
		# board - string - the filename of the .risk file being used as a board
		# The function assumes this file is in the boards folder

		# Member variables:
		# territories - list of territories
		self.territories = []

############### WIP #######################

		# Read through the .risk file and convert it to graph
		print('Opening file: {}'.format('./boards/' + str(board) + '.risk'))
		with open('./boards/' + board + '.risk') as fboard:
			lines = fboard.readlines()

			tID = 0
			for line in lines:
				territory = lines.
				print(line)


				tID += 1

			fboard.close()
		return


class Territory_():
	# This class defines a Territory or node in the graph

	def __init__(name, borders, tID):
		# This is the constructor for the Territory_ class
		# Arguments:
		# name - string - the name of the territory
		# borders - list of territory IDs - the names of bordering territories
		# tID - int - the unique id of the territory on the board

		self.name = name
		self.borders = borders
		self.tID = tID

def parse_arguments():
	# This function helps main read command line arguments
	parser = argparse.ArgumentParser(description=
		'Risk Environment Argument Parser')
	parser.add_argument('--board',dest='board',type=str)
	return parser.parse_args()


def main(args):
	# The main function for this file will print out environment details 
	args = parse_arguments()
	board = args.board

	environment = Risk_Env(board)


# This is something you have to do in Python... I don't really know why	
if __name__ == '__main__':
	main(sys.argv)