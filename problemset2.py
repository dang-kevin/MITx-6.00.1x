# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:30:34 2018

@author: kd_ch
"""

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
    print("Remaining balance:", round(balance, 2))

def min_payment(balance, annualInterestRate):
    payment = 10
    start_balance = balance
    while balance > 0:
        for i in range(12):
            balance = balance - payment + ((balance - payment) * (annualInterestRate/12))
        if balance > 0:
            payment += 10
            balance = start_balance
        elif balance <= 0:
            break
    print("Lowest payment:", payment)

def min_payment_bisect(balance, annualInterestRate):
    start_balance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    lower_bound = start_balance / 12
    upper_bound = (start_balance * (1 + monthlyInterestRate) ** 12) / 12.0
    epsilon = 0.01
    
    while abs(balance) > epsilon:
        payment = (lower_bound + upper_bound) / 2
        balance = start_balance
        for i in range(12):
            balance = balance - payment + ((balance - payment) * (annualInterestRate/12))
        if balance > epsilon:
            lower_bound = payment
        elif balance < -epsilon:
            upper_bound = payment
        else:
            break
    print("Lowest payment:", round(payment, 2))