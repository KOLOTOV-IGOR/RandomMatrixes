#!/usr/bin/env python
import numpy.matlib 
import sys, getopt
import numpy as np
import random

def main(argv):
	if len(argv) == 0:
		print('MatrixMake.py -r(--row) <number_of_rows> -c(--col) <number_of_columns> --random --filename')
		sys.exit()
	try: opts, args = getopt.getopt(argv, "hr:c:", ["row=", "col=", "random", "filename="])
	except getopt.GetoptError:
		print('MatrixMake.py -r(--row) <number_of_rows> -c(--col) <number_of_columns> --random --filename')
		sys.exit()
	#Values for default mode######################
	rand = False
	filename = "default.txt"
	##############################################
	for opt, arg in opts:
		if opt == '-h':
			print('MatrixMake.py -r(--row) <number_of_rows> -c(--col) <number_of_columns> --random --filename')
			sys.exit()
		elif opt in ("-r", "--row"):
			row = arg
			try: row = int(row)
			except Exception:
				print("r|row must be an integer")
				sys.exit()
		elif opt in ("-c", "--col"):
			col = arg
			try: col = int(col)
			except Exception:
				print("c|col must be an integer")
				sys.exit()
		elif opt == '--random':
			rand = True
		elif opt == '--filename':
			filename = arg
	return (row, col, rand, filename)	

def rand_numbers(matrix, max_val):
	(rows, cols) = matrix.shape
	for i in range(rows):
		for j in range(cols):
			matrix.itemset((i, j), random.randrange(0, max_val))
	return	

def one_number(matrix, val):
	(rows, cols) = matrix.shape
	for i in range(rows):
		for j in range(cols):
			matrix.itemset((i, j), val)
	return	

#main part:
(row, col, rand, filename) = main(sys.argv[1:])
matrix = np.matlib.zeros((row, col), dtype = np.float64)
if rand:
	print("Enter what numbers you want[int,float]: ", end = "")
	try: comm = str(input())
	except Exception:
		print("You must input string!")
		sys.exit()
	if comm == "float":
		print("Enter the min value of the random range: ", end = "")
		try: min_val = int(input())
		except Exception:
			print("min_val must be an integer")
			sys.exit()
		print("Enter the max value of the random range: ", end = "")
		try: max_val = int(input())
		except Exception:
			print("max_val must be an integer")
			sys.exit()
		#rand_numbers(matrix, max_val)
		matrix = (max_val - min_val)*np.random.rand(row, col) + min_val 
	elif comm == "int":
		print("Enter the min value of the random range: ", end = "")
		try: min_val = int(input())
		except Exception:
			print("min_val must be an integer")
			sys.exit()
		print("Enter the max value of the random range: ", end = "")
		try: max_val = int(input())
		except Exception:
			print("max_val must be an integer")
			sys.exit()
		#rand_numbers(matrix, max_val)
		matrix = np.random.randint(min_val, max_val, size = (row, col))
	else:
		print("You input wrong command. Must be one of [int,float]")
else:
	print("Enter the number: ", end = "")
	val = float(input())
	one_number(matrix, val)
	
#print(matrix)
np.savetxt(filename, matrix)

#print(np.random.rand(3,2))
