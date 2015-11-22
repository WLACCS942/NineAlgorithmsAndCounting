# NineAlgorithmsAndCounting
Python implementations of several algorithms from Rosen's Discrete Mathematics Textbook, along with some extra algorithms for fun.
I. Algorithms
    1. Algorithms from the Textbook:
    Name:                                                                 File:
    Greedy Change-Making Algorithm (Algorithm 3.1.6, pg.199)              GreedyChange.py 
    Constructing Base b Expansions (Algorithm 4.2.1, pg.249)              BaseExpansion.py
    Addition of Integers (Algorithm 4.2.2, pg. 251)                       BinaryAddition.py
    Modular Exponentiation (Algorithm 4.2.5, pg. 254)                     BinaryModularExponentiation.py
    The Euclidean Algorithm (a.k.a gcd) (Algorithm 4.3.1, pg. 269)        EuclideanAlgorithm.py
    A Recursive Algorithm for Fibonacci Numbers (Algorithm 5.7, pg. 365)  Fibonacci.py
    
    2.Algorithms not from the TextBook:
    Name:                              File:
    Extended Euclidean Algorithm       ExtendedEuclideanAlgorithm.py
    Lowest Common Multiple (a.k.a lcm) lcm.py
    Modular Inverse                    ModularInverse.py

II. How to Run
    All files can be executed from the command line and python 3.5 shell.
    HOW:
    1. Command line (Windows):
        1. Change to local directory.
        2. Input $python.exe -i FileName.py -h [To see proper usage]
        3. Exit python.exe with $Ctrl+C and run 2 again with proper usage.
    2. Python 3.5 shell:
        $import os
        $os.chdir("C:/SomeDirectory") [Unix syntax]
        $os.getcwd() [Check to make sure you're in the right directory]
        $from FileName import Function [leave out the .py]
        $function(args)
