#!/usr/bin/env python
# coding: utf-8

# # Assignment # 4
# 

# In[2]:


#1.Make a calculator using Pbthon with addition , subtraction , multiplication ,division and power.


def Add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiplb(a, b):
    return a * b


def divide(a, b):
    return a / b


print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiplb")
print ("4.Divide")

while True:
   
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiplb(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        neat_calculation = input("Let's do more calculation? (yes/no): ")
        if neat_calculation == "no":
          break
    
    else:
        Print ("Invalid Input")


# In[3]:


#2. Write a program to check if there is any numeric value in list using for loop.
list = ["sumbul", "saleem", 4, "5",6,7,"jakhura"] 
for x in list: 
    if type(x) == int: 
        print(x)


# In[4]:


#3. Write a Python script to add a key to a dictionary.
dictionary={1:"hello", 2:"how are you"}
print(dictionary)
dictionary.update({3:"world"})
print(dictionary)


# In[5]:


#4. Write a Python program to sum all the numeric items in a dictionary.
my_dict = {'a':200,'b':400,'c':100}
print(sum(my_dict.values()))


# In[6]:


#5. Write a program to identify duplicate values from list.
list1=[1,2,3,4,5,6,7,2,4,7,8,9,8]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print(i,end=' ')


# In[21]:


#6. Write a Python script to check if a given key already exists in a dictionary


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(6)
is_key_present(9)


# In[ ]:




