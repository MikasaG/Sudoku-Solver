SAT-based Sudoku Solver
# Basic Function:

Go to the corresponding directory:

	$ cd Basic

There are two executable files **sud2sat.py** & **sat2sud.py**, and a input 
file **p096_sudoku.txt** retrieved from [Here](https://projecteuler.net/project/resources/p096_sudoku.txt).
>The input contains 95 puzzles:
![p096_sudoku.txt](https://raw.githubusercontent.com/MikasaG/Sudoku-Solver/master/images/1.PNG)
.

Convert the Sudoku problems to SAT expressions:
	  
	$ ./sud2sat.py p096_sudoku.txt --multiple

>It creates two directories of files: p096_sudoku_SAT containing the SAT expressions, and p096_sudoku_Result containing the prepared output files for the next step with running times already written on them. It also creates a file CNF-temp containing intermediate CNF formulas.

Convert the SAT expressions to solved Sudokus:

	$ ./sat2sud.py --multiple p096_sudoku_SAT p096_sudoku_Result

>It appends the solved Sudokus to each prepared output file in 
p096_sudoku_Result.
The result looks like this:
![Sample Result](https://raw.githubusercontent.com/MikasaG/Sudoku-Solver/master/images/2.PNG)

If you want to run the excutables multiple times, please delete the two directories (p096_sudoku_SAT and p096_sudoku_Result) first.
# Extended Task 1:

Go to the corresponding directory:

	$ cd Extended_1

There are two executable files **sud2sat.py** & **sat2sud.py**, and an input 
file **TOP95.txt** retrieved from [Here](http://magictour.free.fr/top95).

Convert the Sudoku problems to SAT expressions:

	$ ./sud2sat-top95.py TOP95.txt --top95

> It creates two directories of files: TOP95_SAT containing the SAT 
expressions, and TOP95_Result containing the prepared output files for the next step with running times already written on them. It also 
creates a file CNF-temp containing intermediate CNF formulas.

Convert the SAT expressions to solved Sudokus:

	$ ./sat2sud.py --multiple TOP95_SAT TOP95_Result

>It appends the solved Sudokus to each prepared output file in 
TOP95_Result.

If you want to run the excutables multiple times, please delete the two directories (TOP95_SAT and TOP95_Result) first.

# Extended Task 3:

We implemented solving general n x n-size puzzles.

Go to the corresponding directory:

	$ cd 320_Project/Extended_3

>There are two executable files sud2sat.py & sat2sud.py, and a sample
input file 4x4.txt containding a 4x4-size Sudoku problem.

Convert the Sudoku problem to SAT expression:

	$ ./sud2sat.py 4x4.txt sat.txt

>It creates two files: sat.txt containing the SAT expression, and 
CNF-temp.txt containing intermediate CNF formulas.

Convert the SAT expression to solved Sudoku:

	$ ./sat2sud.py sat.txt

>It prints the solved Sudoku on Terminal.
