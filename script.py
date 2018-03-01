import os
import sys
import glob
import math
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


def dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def car_to_ride_score(car, ride, bonus):

	ride_length = dist((ride[0], ride[1]), (ride[2], ride[3]))
	start_moment = car[2] + dist(car[1], (ride[0], ride[1]))
	
	if start_moment <= ride[4]:
		return (ride_length + bonus, start_moment + ride_length)

	if start_moment + ride_length <= ride[5]:
		return (ride_length, start_moment + ride_length)

	return (0, start_moment + ride_length)


def emil(data):

	# create cars and rides
	cars = []
	for i in range(0, data.F):
		cars.append((i, (0, 0), 0))
	rides = data.data

	assign = {}

	# sort rides
	for i, r in enumerate(rides):
		# print(i)
		best_car = 0
		best_car_distance = (-math.inf, 0)
		for c in cars:
			d = car_to_ride_score(c, r, data.B)
			if d[0] > best_car_distance[0]:
				best_car_distance = d
				best_car = c[0]
		
		# assign car
		try:
			assign[best_car].append(i)
			cars[best_car] = (best_car, (r[2], r[3]), best_car_distance[1])
		except KeyError:
			assign[best_car] = [i]
			cars[best_car] = (best_car, (r[2], r[3]), best_car_distance[1])

	return assign


	return 0


def solve(path):

	d = read_data(path)

	result = emil(d)
	print(result)
	
	write_result(d.F, result, "./outputs/%s" % os.path.basename(path))



def write_result(F, d, output_path):

	with open(output_path, 'w') as f:
		for rides in d.values():
			f.write(str(len(rides)))
			for r in rides:
				f.write(' ' + str(r))
			f.write('\n')
		for i in range(F, len(rides), -1):
			f.write('0')
			f.write('\n')






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