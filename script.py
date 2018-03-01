import sys
import glob
import numpy as np


def read_data(path):

	with open(path, 'r') as f:
		
		for i, row in enumerate(f):

			# read first line
			if i == 0:
				R, C, F, N, B, T = map(lambda x: int(x), row.split(' '))
				print(C)
				break


def solve(path):

	data = read_data(path)



def run_all():

	input_files = glob.glob("inputs/*.in")
	for input_file in input_files:
		solve(input_file)


def run_single(file_path):
	solve(file_path)



if __name__ == "__main__":

	if len(sys.argv) < 2:
		run_all()
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		run_single(file_path)
	else:
		sys.exit('Wrong input !')