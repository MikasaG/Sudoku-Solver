#!/usr/bin/env python3
import sys
import os
import math

def readSAT(filename):
	output = ''
	with open(filename, 'r') as infile:
		if not infile:
			print("File does not exist!")
			exit(1)

		for line in infile:
			if line == "SAT\n" or line == '\n':
				continue

			variable_list_sol = []
			for var in line.split(' '):
				if int(var) > 0:
					variable_list_sol.append(int(var))
			
			size = len(variable_list_sol)
			n = int(math.sqrt(size))
			board = [[0 for i in range(n)] for j in range(n)]
			
			# Decode.
			count = 0
			for i in range(n):
				for j in range(n):
					var = variable_list_sol[count]
					count += 1
					k = var - size * i - n * j
					board[i][j] = k

			# Print board.
			gird = int(math.sqrt(n))
			for i in range(len(board)):
				if i % gird == 0:
					output += '\n'
				for j in range(len(board[i])):
					if j % gird == 0:
						output += ' '
					output += str(board[i][j]) + ' '
				output += '\n'
			output += '\n'
		return output


def main(argv):
	if len(argv) not in range(2, 5):
		print("Usage: ./sat2sud.py <filename>")
		print("    or ./sat2sud.py --multiple <SAT data directory> <result directory>")
		exit(1)

	if len(argv) == 2:
		print(readSAT(argv[1]))

	else:
		if argv[1] != "--multiple":
			print("Usage: ./sat2sud.py <filename>")
			print("    or ./sat2sud.py --multiple <SAT data directory> <result directory>")
			exit(1)
		count = 0
		result_list = sorted(os.listdir(argv[3]))
		for filename in sorted(os.listdir(argv[2])):
			resultfile = open(argv[3]+ '/' + result_list[count], 'a')
			resultfile.write(readSAT(argv[2] + '/' +filename))
			count +=1


if __name__ == "__main__":
    main(sys.argv)
