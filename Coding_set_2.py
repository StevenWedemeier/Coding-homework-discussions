#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculating sale profit with 23% of the sale.
profit = total_sales * 0.23

print('The profit is $', format(profit, ',.2f'))


# In[ ]:


COLOR = input('What\'s your favorite color? ')
print(f"Your favorite color is {COLOR}")


# This doesnt work how I wanted it.

# In[ ]:


R = float(input('How many feet in rows')) 
E = float(input('The amount of space used by an end-post assembly, in feet'))
S = float(input('The amount of space between the vines, in feet'))

V = (R - 2 * E) / S

print(V)

print('You can have this amount of grapevines within the given area:')
print(V)







# The correct way, with if statements.

# In[ ]:


def calculate_grapevines(R, E, S):

    V = (R - 2 * E) / S
    return V

# Get user input for R, E, and S
try:
    R = float(input("Enter the length of the row (R) in feet: "))
    E = float(input("Enter the space used by an end-post assembly (E) in feet: "))
    S = float(input("Enter the space between the vines (S) in feet: "))

    grapevines = calculate_grapevines(R, E, S)
    print(f"Number of grapevines that can be planted: {grapevines}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")

