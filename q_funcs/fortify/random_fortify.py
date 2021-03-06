"""
This file contains the Q function for random fortification
Each territory held by the player has an equal probability of being selected
Output is a random vector of size T^2
Assuming that it is strictly better to fortify somewhere rather than not fortify
Env will not fortify only if there are no valid moves specified

Env will determine how many troops to move
TODO: How to determine this?  Is there an optimal decision?

"""

import numpy as np
import random

global MAX_ARMIES #max armies per player

class RandomFortify():
	"""
	Class to hold the maximum success policy
	"""
	def __init__(self, T, act_list):
		"""
		Constructor so RandomFortify can be held as an object
		:param T: int the length of the state vector
		:param act_list: 2D list mapping edges to territories
		:return : none
		"""
		self.T = T
		self.act_list = act_list
		return

	def call_Q(self, state_vector, update=None, action_taken=None, target=None, loss_weights=None):
		"""
		Function for executing maximum battle success
		:param state_vector: np-array 1D vector of armies on territory
		:return action_vector: np-array 1D vector of edges to attack along
		"""


		# T = len(state_vector[0])
		# Leaving edge_matrix in as a visualization
		# edge_matrix[row, col] = action_vector[row*T + col]
		# edge_matrix = np.zeros((T,T), dtype=int)
		
		# action_vector = np.random.rand(T**2)	

		# Code below will work but is unnecessary
		# Since action_vector can be naive to game validity, a random vector will suffice
		# action_vector = np.zeros(T, dtype=int)
		# valid_terrs = []
		# for terr in range(T):
		# 	if state_vector[terr] > 0:
		# 		valid_terrs.append(terr)

		# allot_choice = random.choice(valid_terrs)
		# action_vector[allot_choice] = 1


		######### Code for updated action space using 2D List ################
		action_vector = np.random.rand(len(self.act_list))

		return action_vector

		