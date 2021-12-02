#!/usr/bin/env python
# coding: utf-8

# # Assignment: Intro to Python
# 
# ## Instructions
# 
# This is the template file for the assignment of Module 4 called "Intro to Python." Please carefully follow the instructions below.
# 
# 1. Rename this file by filling out your surname and first name in the file name. For example, if your surname is Ilagan and if your first name is Joben, then rename the file to ILAGAN-JOBEN-introToPython.ipynb.
# 2. Fill out the markdown cell just above `Problem 1` with your student details as indicated.  
# 3. To submit this file, first, upload your file to your GitHub repository and, second, submit your repository link to the assignment on Canvas.
# 

# # Student Details
# 
# ID Number:  195004
# Surname:  Tio
# Year and Course: 3 BS ITE  

# ## Problem 1 (5 points)
# 
# This is the only problem in this assignment.  
# 
# Overall prompt:  
# **Write a program that prompts the user to input three positive integers and outputs the average of those three positive integers.**  
# 
# The program must follow these specifications:  
# 1. Accept the user's input numbers one at a time. Use this format:  
# `Enter first number: {firstnumber}`  
# `Enter second number: {secondnumber}`  
# `Enter third number: {thirdnumber}`  
# 2. The output should display using this format:  
# `The average is {average}.`  
# 3. The program must, at some point, call a function called `three_number_average` that accepts three arguments and returns the average of those three arguments.  
# 
# ### Sample input and output
# 
# Sample Input:  
# `Enter first number: 1`  
# `Enter second number: 2`  
# `Enter third number: 3`  
# Sample Output:  
# `The average is 2.0`  
# 
# Sample Input:  
# `Enter first number: 1`  
# `Enter second number: 1`  
# `Enter third number: 1`  
# Sample Output:  
# `The average is 1.0`  
# 
# Sample Input:
# `Enter first number: 2`  
# `Enter second number: 4`  
# `Enter third number: 6`  
# Sample Output:  
# `The average is 4.0`  

# In[11]:


def three_number_average():
    input_1 = int(input("Enter first number: "))
    input_2 = int(input("Enter second number: "))
    input_3 = int(input("Enter third number: "))
    return int((input_1+input_2+input_3)/3) 

print("The average is",[three_number_average()])


# In[ ]:




