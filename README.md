# NineAlgorithmsAndCounting
Python 3.5 implementations of several algorithms from __Discrete Mathematics and its Applications, 7th ed.__, by Kenneth H. Rosen. There are also some extra algorithms for fun. __*Needs Python 3.5*__

## I. Algorithms: 

### Note: In each file, the actually relevant core algorithm is usually below the 'main()' function. Exception handling and 'main()' are not part of the core algorithm itself but are implementation details allowing for the code to perform as intended and be usable on the command line and python 3.5 shell.
* __Algorithms from the Textbook:__  

<table>
    <tr>
        <th>Name:</th>                                                              
        <th>File:</th>
    </tr>
    <tr>
        <td>Greedy Change-Making Algorithm (Algorithm 3.1.6, pg.199)</td>
        <td>GreedyChange.py</td>
    </tr>
    <tr>
        <td>Constructing Base b Expansions (Algorithm 4.2.1, pg.249)              
        <td>BaseExpansion.py</td>
    </tr>
    <tr>
        <td>Addition of Integers (Algorithm 4.2.2, pg. 251)</td>
        <td>BinaryAddition.py</td> 
    </tr>
    <tr>
        <td>Modular Exponentiation (Algorithm 4.2.5, pg. 254)</td>
        <td>BinaryModularExponentiation.py</td> 
    </tr>
    <tr>
        <td>The Euclidean Algorithm (a.k.a gcd) (Algorithm 4.3.1, pg. 269)</td>  
        <td>EuclideanAlgorithm.py</td> 
    </tr>
    <tr>
        <td>A Recursive Algorithm for Fibonacci Numbers (Algorithm 5.7, pg. 365)</td>
        <td>Fibonacci.py</td>
    </tr>
</table>
    
* __Algorithms not from the Textbook:__  

<table>
    <tr>
        <th>Name:</th>                       
        <th>File:</th>
    </tr>
    <tr>
        <td>Change Base of Number</td>             
        <td>ConvertBase.py</td> 
    </tr>
    <tr>
        <td>Convert Base to Decimal</td>             
        <td>ToDecimal.py</td> 
    </tr>
    <tr>
        <td>Extended Euclidean Algorithm</td>   
        <td>ExtendedEuclideanAlgorithm.py</td>  
    </tr>
    <tr>
        <td>Lowest Common Multiple (a.k.a lcm)</td> 
        <td>lcm.py</td>
    </tr>
    <tr>
        <td>Modular Inverse</td>             
        <td>ModularInverse.py</td> 
    </tr>
</table>
    

## II. How to Run  

__*All files can be executed from the command line and python 3.5 shell.*__
    
HOW:  
    
1. _Command line (Windows):_ 
    1. Change to local repo clone directory.  
    2. Input '$python.exe -i FileName.py -h' [To see proper usage]  
    3. Exit python.exe with '$Ctrl+C' and run 2 again with proper usage.  
        
2. _Python 3.5 shell:_  
    
    $import os  
        
    $os.chdir("C:/RepoCloneDirectory") [Unix syntax]  
        
    $os.getcwd() [Check to make sure you're in the right directory]  
        
    $from FileName import Function [leave out the .py]  
        
    $Function(args)  
