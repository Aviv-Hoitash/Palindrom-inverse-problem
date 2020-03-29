# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:21:40 2020

@author: Aviv Hoitash
"""
'''
The function below is trying to solve a math problem that asks: For any number if you add its inverse a certian amount 
of times, it will eventually become a palindrome, True or False? For example, 23 + its inverse, 32 = 55. 
Numbers that are already palindromes like 3, or 77 don't go through this process.


There are 2 inputs that you need to provide:
1. The amount of numbers you want to examine.
2. The maximum number of times that each number goes through the adding its inverse process.
'''


def palindrome_inverse():
    
    y = int(input("what would you like your range of numbers to be?:"))
    x = int(input("what would you like your counter range to be?:"))
    
    step_counter = 0 #counts the amount of steps each number takes before becoming a palindrome
    non_palindrome_counter = 0 #counts the amount of numbers that take more than your input steps to become a palindrome
    counter_list = [0]*x #sets up a list with your input 0's so it can become a counter later
    
    for num in range(y): #for numbers in the input that is given
        str_num = str(num)         
        while not int(str_num) == int(str_num[::-1]) and not step_counter > x: # while its not a palindrome and the
            #step counter is less than your input
            
            str_num = str(int(str_num)+int(str_num[::-1])) #number is added to its inverse
            step_counter = step_counter + 1 #another step is added to the amount of steps
        
        if step_counter > x: #if the amount of steps is bigger than your input
            print(num, "takes more than",x,"steps to become a palindrome")# print out the number and that it takes more steps
            non_palindrome_counter +=1 #another number does not become a palindrome in less than your input
            step_counter = 0 #step counter restets
            
            
        
        else: #if the number becomes a palindrome in less than your input
            print(num,"becomes a palindrome in",step_counter,"steps") #print the number and how many steps it takes
            counter_list[step_counter] +=1 # the amount of numbers that take that amount of steps, goes up by 1
            step_counter = 0 #step counter restets

    print('\n')
    print('\n')
    for i in range(len(counter_list)): # for number in the length of the counter list
             print("There are",counter_list[i],"numbers that take",i,"steps") #print out the amount of numbers there are that take each amount of steps
    print("There are",non_palindrome_counter,"numbers, less than",y, "that take more than",x,"steps to become a palindrome") #print out the aount of numbers that don't become a palindrome
palindrome_inverse()
