# Activity Python 13: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    16 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Calculate factorials given user input


import math

# Input user number
N = int(input('Enter calculated number for factorials: '))

# Calculate the number of factorial
M = 1
    
while (N > 0):
    M= M*N
    N=N-1
print(M)

 
if N < 0:
    print("Please enter a non-negative number")
if N == 0:
    N1 = 1    



