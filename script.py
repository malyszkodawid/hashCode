import sys
import glob
import numpy as np



class Data(object):

	def __init__(self, header, array):

		self.header = header

		self.R, self.C, self.F, self.N, self.B, self.T = header

		self.data = np.array(array)

def read_data(path):

	data_array = []
	header = []

	with open(path, 'r') as f:
		
		for i, row in enumerate(f):

			row = list(map(lambda x: int(x), row.split(' ')))

			# read first line
			if i == 0:
				header = row
				continue

			data_array.append(row)

	return Data(header, data_array)

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