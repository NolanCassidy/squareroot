"""
squareroot.py:  Approximate pi with iterative function
Authors: Nolan Cassidy

CIS 210 assignment 2, Fall 2016.
"""
import argparse      # Used in main program to get PIN code from command line
import math
from test_harness import testEQ  # Used in CIS 210 for test cases

## Constants used by this program

def my_sqrt(number, iterations):
    """
    Generate an iterative approximation to the square root of a number
    Args:
        number:  positive number to calculate the square root of
        iterations: number of iterations to perform
    Returns:
        approximate value of the square root
    """

    value = number
    apprx = 1
    for i in range(iterations):
        apprx = (apprx + (value/apprx))/ 2

    return apprx

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    print("**** TESTING --- 5 iterations for sqrt of 1, 10, 100, 1000, 10000")
    testEQ("1.0", my_sqrt(1.0, 5), 1.0)
    testEQ("10.0", my_sqrt(10.0, 5), 3.162277665175675)
    testEQ("100.0", my_sqrt(100.0, 5), 10.032578510960604)
    testEQ("1000.0", my_sqrt(1000.0, 5), 41.24542607499115)
    testEQ("10000.0", my_sqrt(10000.0, 5), 323.0844833048122)
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two.
    """
    parser = argparse.ArgumentParser(description="Iterative approximation for pi")
    parser.add_argument("Number", type=float, help="number (a float)")
    parser.add_argument("-i", "--iterations", type=int, help="iterations (an int)")
    args = parser.parse_args()  # gets arguments from command line
    number = args.Number
    iterations = args.iterations
    value = my_sqrt(number, iterations)
    print("After", iterations, "iterations, sqrt(", number, ") = ", "{:.5}".format(value))
    print("This represent {:.2%} error compared to the math library.".format(abs(((math.sqrt(number)-value)/math.sqrt(number)))))

if __name__ == "__main__":
    #run_tests()
    main()


