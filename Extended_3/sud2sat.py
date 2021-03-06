#!/usr/bin/env python3
import sys
import os
import math
import time
import subprocess

puzzle_size = 0
dimension_size = 0

def Encode(i, j, k,):
        return str((i - 1) * puzzle_size + (j - 1) * dimension_size + (k-1) +1)


def Encode_variable(puzzle):
        row = 1
        col = 1
        count = 0

        variable_list = []
        while (row <= dimension_size):
            variable_encoded = Encode(row, col, int(puzzle[count]))
            variable_list.append(variable_encoded)
            col += 1
            if (col == dimension_size + 1):
                row += 1
                col = 1
            count += 1
        variable_list = [str(x) for x in variable_list]
        return variable_list


def pnf_GeneralInfo(n):
    variable_num = n**3
    clause_num = (n*n*int(math.sqrt(n))*int(math.factorial(n)/math.factorial(2)/math.factorial(n-2))) + (n*n)
    return "p cnf " + str(variable_num)+" " + str(clause_num)+ "\n"


def cons_OneNumPerEntry(variable_list,puzzle):
    output = ''
    for i in range(len(variable_list)):
        if (puzzle[i] != '0'):
            output += str(variable_list[i] + ' 0\n')
        else:
            loc = divmod(i, dimension_size)
            for x in range(1, dimension_size + 1):
                output += Encode(loc[0]+1,loc[1]+1,x) + ' '
            output += '0\n'
    return output


def cons_OneNumPerRow():
    output = ''
    for i in range(1, dimension_size + 1):
        for k in range(1, dimension_size + 1):
            for j in range(1, dimension_size):
                for l in range(j + 1, dimension_size + 1):
                    output += "-" + Encode(i, j, k) + " -" + Encode(i, l, k) + " 0\n"
    return output


def cons_OneNumPerCol():
    output = ''
    for j in range(1, dimension_size + 1):
        for k in range(1, dimension_size + 1):
            for i in range(1, dimension_size):
                for l in range(i + 1, dimension_size + 1):
                    output += "-" + Encode(i, j, k) + " -" + Encode(l, j, k) + " 0\n"
    return output


def cons_OneNumPerBlock():
    output = ''
    subgrid_size = int((dimension_size) ** (float(1 / 2)))
    for k in range(1, dimension_size + 1):
        for a in range(0, subgrid_size):
            for b in range(0, subgrid_size):
                for u in range(1, subgrid_size + 1):
                    for v in range(1, subgrid_size):
                        for w in range(v + 1, subgrid_size + 1):
                            output += "-" + Encode(subgrid_size * a + u, subgrid_size * b + v, k) + " -" + Encode(subgrid_size * a + u, subgrid_size * b + w, k) + " 0\n"

    for k in range(1, dimension_size + 1):
        for a in range(0, subgrid_size):
            for b in range(0, subgrid_size):
                for u in range(1, subgrid_size):
                    for v in range(1, subgrid_size + 1):
                        for w in range(u + 1, subgrid_size + 1):
                            for t in range(1, subgrid_size + 1):
                                output += "-" + Encode(subgrid_size * a + u, subgrid_size * b + v, k) + " -" + Encode(subgrid_size * a + w, subgrid_size * b + t, k) + " 0\n"
    return output


def write_CNF(puzzle,dimension_size,targetfile):
    variable_list = Encode_variable(puzzle)
    outfile = open(targetfile, "w")
    outfile.write(pnf_GeneralInfo(dimension_size))
    outfile.write(cons_OneNumPerEntry(variable_list,puzzle))
    outfile.write(cons_OneNumPerRow())
    outfile.write(cons_OneNumPerCol())
    outfile.write(cons_OneNumPerBlock())


def main():
    global puzzle_size,dimension_size
    puzzle = ""
    start = time.clock()# Start counting time for this process
    if (len(sys.argv) != 3):  # the input content must have more than two words
        print("Usage: ./sud2sat.py <input filename> <output filename>\n  or  : ./sud2sat.py  <input filename> --multiple")
        return
    try:  # check if can open file
        with open(sys.argv[1], 'r') as infile:
            if sys.argv[2]=='--multiple':
                line = infile.readline()
                count = 1
                if not os.path.exists(sys.argv[1].split('.')[0]+"_SAT"):
                    os.mkdir(sys.argv[1].split('.')[0]+"_SAT")
                if not os.path.exists(sys.argv[1].split('.')[0]+"_Result"):
                    os.mkdir(sys.argv[1].split('.')[0]+"_Result")
                while 1:
                    line = infile.readline()
                    if line:
                        line = line.strip()
                    if not line or line[0] == 'G' or line[0] == 'g':
                        puzzle = puzzle.replace('\n', '').replace('?', '0').replace('*', '0').replace('.','0')  # replace special symbols to 0
                        puzzle_size = len(puzzle)
                        if int(math.sqrt(puzzle_size)) ** 2 != puzzle_size:
                            print("The %d th Sudoku grid is invalid!!!"%(count))
                            if not line:
                                break
                        else:
                            dimension_size = int(math.sqrt(puzzle_size))
                            write_CNF(puzzle, dimension_size, "CNF-temp.txt")
                            subprocess.call(["minisat", "CNF-temp.txt", sys.argv[1].split('.')[0]+"_SAT/"+sys.argv[1].split('.')[0]+"_SAT_"+str('{:0>2d}'.format(count))+".txt"])
                            totalTime = time.clock() - start
                            resultfile = open(sys.argv[1].split('.')[0]+"_Result/"+sys.argv[1].split('.')[0]+"_"+str('{:0>2d}'.format(count)), 'w')
                            resultfile.write("Grid No.%d - time used (including running minisat): " % (count) + str(totalTime) + " seconds"+"\n")
                            print("Grid No.%d - time used (including running minisat): " % (count) + str(totalTime) + " seconds")  # end the time counting
                            start = time.clock()
                            puzzle = ""
                            if not line:
                                break
                        count +=1
                    else:
                        puzzle += line

            else:
                puzzle = infile.read().replace('\n', '').replace('?', '0').replace('*', '0').replace('.', '0')# replace special symbols to 0
                puzzle_size = len(puzzle)
                if int(math.sqrt(puzzle_size)) ** 2 != puzzle_size:
                    print("This is not a valid Sudoku file!!!")
                else:
                    dimension_size = int(math.sqrt(puzzle_size))
                    write_CNF(puzzle, dimension_size, "CNF-temp.txt")
                    subprocess.call(["minisat", "CNF-temp.txt", sys.argv[2]])
                    totalTime = time.clock() - start
                    print("Time used (including running minisat):" + str(totalTime) + " seconds")  # end the time counting
    except IOError:  # file doesn't exist so print error!
        print("File does not exist!")


if __name__ == "__main__":
    main()
