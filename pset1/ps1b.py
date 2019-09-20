# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:14:12 2018
@author: David

Input: positive values for total_cost, portion_saved, annual_salary and semi_annual_raise. 
Output: A positive integer, the number of months needed to save for down payment.
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal :'))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi annual raise as a percentage: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
months_spent_saving = 0 

while(current_savings < total_cost * portion_down_payment):
    current_savings += annual_salary/12 * portion_saved + current_savings * r/12
    months_spent_saving += 1
    if months_spent_saving % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    
print('Number of Months: ', months_spent_saving)