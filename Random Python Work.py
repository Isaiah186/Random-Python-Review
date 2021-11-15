#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Colours:
    def __init__(self):
        pass
    
    def colors(self):
        color_list=["Red","Green","White","Black","Yellow","Blue"]
        print(color_list)
    


# In[8]:


poop = Colours()


# In[12]:


poop.colors()


# In[13]:


#This is a class that contains a color list and prints it out once it's turned into an object and used.


# In[19]:


class Multiplication:
    def __init__(self):
        pass
    
    def product(self,num1,num2):
        num3 = num1 * num2
        print(num3)
        


# In[22]:


lemonade= Multiplication()


# In[23]:


lemonade.product(2,4)


# In[24]:


#A class is a group of functions made to unite them all and create objects


# In[25]:


#Self lets the functions in a class know they are all related


# In[26]:


#A constructor is the foundation of the class


# In[31]:


class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
    def eat(self,name,age):
        print(f"{name} is {age} years old and eating.")
    
    def sleep(self,name,age):
        print(f"{name} is {age} years old and sleeping.")
    
    def walk(self,name,age):
        print(f"{name} is {age} years old and walking.")
    


# In[34]:


tea = Human("Isaiah",16)


# In[35]:


tea.sleep("Isaiah",16)


# In[47]:


class List:
    def __init__(self):
        pass
    
    
    def reverse(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
        numbers.reverse
        print(numbers)
        
    
    def even(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
        for i in numbers:
            if i%2==0:
                print(i)
        
    
    def odd(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
        for i in numbers:
            if i%2 != 0:
                print(i)
                


# In[48]:


worm = List()


# In[49]:


worm.odd()


# In[9]:


class Palindrome:
    def __init__(self):
        pass
    
    def detector(self):
        x = input("Enter a Word :)")
        
        y = [x]
        
        y.reverse()
        
        if y==y.reverse():
            print("This is a palindrome.")
            
        else:
            print("This isn't a palindrome.")


# In[10]:


coffee = Palindrome()


# In[11]:


coffee.detector()


# In[ ]:




