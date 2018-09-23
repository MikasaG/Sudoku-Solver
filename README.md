CSC 320 - Project
SAT-based Sudoku Solving
August 3rd, 2018

Bicheng Feng (V00834906)
Chang Gong (V00898803)
Yiming Sun (V00811496)
Xiangwen Zheng (V00849073)
Yufeng Zhu (V00898046)

This document will briefly introduce the contents of this submission, 
and the commands for executables.

----------------------------------------------------------------------
----------------------------------------------------------------------

Basic Task:

Go to the corresponding directory:

	$ cd 320_Project/Basic

There are two executable files sud2sat.py & sat2sud.py, and a input 
file p096_sudoku.txt retrieved from 
https://projecteuler.net/project/resources/p096_sudoku.txt.

Convert the Sudoku problems to SAT expressions:
	  
	$ ./sud2sat.py p096_sudoku.txt --multiple

It creates two directories of files: p096_sudoku_SAT containing the SAT 
expressions, and p096_sudoku_Result containing the prepared output 
files for the next step with running times already written on them. It 
also creates a file CNF-temp containing intermediate CNF formulas.

Convert the SAT expressions to solved Sudokus:

	$ ./sat2sud.py --multiple p096_sudoku_SAT p096_sudoku_Result

It appends the solved Sudokus to each prepared output file in 
p096_sudoku_Result.

If you want to run the excutables multiple times, please delete the two directories (p096_sudoku_SAT and p096_sudoku_Result) first.

----------------------------------------------------------------------

Extended Task 1:

Go to the corresponding directory:

	$ cd 320_Project/Extended_1

There are two executable files sud2sat.py & sat2sud.py, and an input 
file TOP95.txt retrieved from http://magictour.free.fr/top95.

Convert the Sudoku problems to SAT expressions:

	$ ./sud2sat-top95.py TOP95.txt --top95

It creates two directories of files: TOP95_SAT containing the SAT 
expressions, and TOP95_Result containing the prepared output files for 
the next step with running times already written on them. It also 
creates a file CNF-temp containing intermediate CNF formulas.

Convert the SAT expressions to solved Sudokus:

	$ ./sat2sud.py --multiple TOP95_SAT TOP95_Result

It appends the solved Sudokus to each prepared output file in 
TOP95_Result.

If you want to run the excutables multiple times, please delete the two directories (TOP95_SAT and TOP95_Result) first.
----------------------------------------------------------------------
Extended Task 3:

We implemented solving general n x n-size puzzles.

Go to the corresponding directory:

	$ cd 320_Project/Extended_3

There are two executable files sud2sat.py & sat2sud.py, and a sample
input file 4x4.txt containding a 4x4-size Sudoku problem.

Convert the Sudoku problem to SAT expression:

	$ ./sud2sat.py 4x4.txt sat.txt

It creates two files: sat.txt containing the SAT expression, and 
CNF-temp.txt containing intermediate CNF formulas.

Convert the SAT expression to solved Sudoku:

	$ ./sat2sud.py sat.txt

It prints the solved Sudoku on Terminal.

----------------------------------------------------------------------
----------------------------------------------------------------------