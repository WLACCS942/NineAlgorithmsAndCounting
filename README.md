# NineAlgorithmsAndCounting
Python implementations of several algorithms from Rosen's Discrete Mathematics Textbook, along with some extra algorithms for fun.  

## I. Algorithms  
* Algorithms from the Textbook:  

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
    
* 2.Algorithms not from the Textbook:  

<table>
    <tr>
        <th>Name:</th>                       
        <th>File:</th>
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

All files can be executed from the command line and python 3.5 shell.  
    
HOW:  
    
1. Command line (Windows):  
    1. Change to local directory.  
    2. Input 
        $python.exe -i FileName.py -h [To see proper usage]  
    3. Exit python.exe with 
        $Ctrl+C and run 2 again with proper usage.  
        
2. Python 3.5 shell:  
    
    $import os  
        
    $os.chdir("C:/SomeDirectory") [Unix syntax]  
        
    $os.getcwd() [Check to make sure you're in the right directory]  
        
    $from FileName import Function [leave out the .py]  
        
    $function(args)  
