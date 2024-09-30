"""
Gavin Riggins
9/30/2024
Advanced Programming & Data Structures

This file contains an implimentation of the bubble sort search algorithm. 
"""
import random 

def bubble(input_list):
    """Sort via bubble sort"""
    # Note: Two nested loops that loop the same thing feels wrong. 
    for e in range(0, len(input_list)):

        for i in range(0, len(input_list) - e): # e-1 ignores the previous searches
            if e != 0 and input_list[i + 1] < input_list[i]:
                # Store i+1 so we could switch it with i without any problems
                storage_var = input_list[i + 1]
                input_list[i+1] = input_list[i]
                input_list[i] = storage_var

    # Return the sorted list for future use later
    return input_list    

print(bubble([random.randint(1,100) for x in range(random.randint(1,100))]))
print(bubble([random.randint(1,100) for x in range(random.randint(1,100))]))
