# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:42:34 2018

@author: David
"""
# Get user input.
annual_salary = float(input('Enter your annual salary?: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal :'))
total_cost = float(input('Enter the cost of your dream home?: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
months_spent_saving = 0 

## Iterate savings until down payment is covered.
while(current_savings < total_cost * portion_down_payment):
    current_savings += monthly_salary * portion_saved + current_savings * r/12
    months_spent_saving += 1
    
print('Number of Months: ', months_spent_saving)