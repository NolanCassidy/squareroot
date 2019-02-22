"""
squareroot.py:  Approximate square root with iterative function
Authors: jsventek (Joe Sventek)

CIS 210 assignment 2, Fall 2016. 
"""
import argparse      # Used in main program to get interations and number
from test_harness import test_approx  # Used in CIS 210 for test cases 
import math

## Constants used by this program

def my_sqrt(number, iterations):
    """
    Generate an iterative approximation to the square root of a number
    args:
        number:  positive number to calculate the square root of
        iterations: number of iterations to perform
    returns:
        approximate value of the square root
    """
    value = 1.0		# initial value (value is X-sub-k)
    while iterations > 0:
        value = 0.5 * (value + number / value)
        iterations -= 1
    return value

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    print("**** TESTING --- 5 iterations for sqrt of 1, 10, 100, 1000, 10000")
    test_approx("1.0", my_sqrt(1.0, 5), 1.0)
    test_approx("10.0", my_sqrt(10.0, 5), 3.162277665175675)
    test_approx("100.0", my_sqrt(100.0, 5), 10.032578510960604)
    test_approx("1000.0", my_sqrt(1000.0, 5), 41.24542607499115)
    test_approx("10000.0", my_sqrt(10000.0, 5), 323.0844833048122)
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Iterative approximation for square root")
    parser.add_argument("Number", type=float, help="number (a float)")
    parser.add_argument("-i", "--iterations", type=int, help="iterations (an int)")
    args = parser.parse_args()  # gets arguments from command line
    number = args.Number
    if number < 0:
        print("Square root undefined for", number)
        return
    iterations = args.iterations
    value = my_sqrt(number, iterations)
    true = math.sqrt(number)
    difference = math.fabs(value - true)
    if true == 0:
        fraction = 0
    else:
        fraction = difference / true
    fmt = "After {} iterations, sqrt({}) = {:.5f}; this represents {:.2%} error compared to the math library"
    print(fmt.format(iterations, number, value, fraction))

if __name__ == "__main__":
    # run_tests()  # Comment this out when your program is working
    main()     # Uncomment this when your program is working



