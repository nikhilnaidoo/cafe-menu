#!/usr/bin/env python
# coding: utf-8

# In[1]:


menu = []
# {} used to create a dictionary 
sotck_price = {}
menu_price = {}
# 0 used as staring to point for stock
total_stock=0
total_price=0
# creating the lenght of the dictionary 

while True:
    try:
        number_of_items = int(input( "please enter how many items you would like to add to the menu"))
    except ValueError:
        print ("please enter the number of items")
        number_of_items = int(input( "please enter how many items you would like to add to the menu"))

# i is used for interger to create loop
    for i in range (number_of_items):
    # stock to create name of product in dictioanry 
        stock = input("name of item: ")
    # adding to menu list 
        menu.append([stock])
        try:
            value = float(input("the cost of item: "))
        except ValueError:
            print ("please enter a number for cost")
            value = float(input("the cost of each item: "))
    
    
    # to add each item as entered
        total_stock += value
    # fromula of 40% mark up of product
        price = (value*.4)+value
    # adding each product price after mark up 
        total_price += price 
    # adding items to dictionary  
        sotck_price[stock]=value
        menu_price[stock]=price
    # caluclating net profit
        net_profit = total_price - total_stock

# print out each out come 
    print ("items on menu","\n", menu)
    print ("\n item : cost ", "\n", sotck_price)
    print ("\n item : price on menu", "\n", menu_price)
    print ("\n toatal value of the menu", "\n", total_price)
    print ("\n toatal stock worth", "\n",total_stock)
    print ("\n potenial net profit", "\n", net_profit)
    break


# In[ ]:




