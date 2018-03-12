"""
A file for testing different state vector inputs on policies
This function will print out which state vectors are being tested and the results
Policy functions must share name with file
"""

import numpy as np
import sys
import argparse
import importlib


def parse_arguments():
	# This function helps main read command line arguments
	parser = argparse.ArgumentParser(description=
		'Risk Environment Argument Parser')
	parser.add_argument('--module',dest='module',type=str)
	parser.add_argument('--class',dest='policy',type=str)
	return parser.parse_args()

def main(args):
	"""
	Reads a policy filepath and runs state vectors on the given policy
	Prints results to console
	:param policy_filepath: string that contains directory and policy function dir.policy
	:return : none
	"""

	#import attack.max_success as pol0
	args = parse_arguments()
	module = args.module
	policy_class = args.policy

	policy_module = importlib.import_module(module, package=None)
	policy_obj = getattr(policy_module, policy_class)

	print(policy_obj)

	# Define a list of state vectors
	s_v_list = []

	# Add state vectors to the list
	s_v_list.append(np.array([1, -1]))
	s_v_list.append(np.array([1, 2, -1]))
	s_v_list.append(np.array([2, -2, -1]))
	s_v_list.append(np.array([1, -2, -1]))


	# Begin test
	print("Testing policy {}".format(module))
	for s_v in s_v_list:
		print("State : {}".format(s_v))
		print("Action:")
		print(policy_obj.enact_policy(s_v))
		print("\n")
	return



if __name__ == '__main__':
    main(sys.argv)
