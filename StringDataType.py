#!/usr/bin/env python
# coding: utf-8

# ### Strings 
# 1.a string is a sequence of characters. For example, "hello" is a string containing a sequence of characters 'h' , 'e' , 'l' , 'l' , and 'o' . (enclosed in sigle , double and triple quotes) 
# 
# 2. triple quotes are used as multiline strings multiline comments as a doc strings.
# 

# In[9]:


s1 = 'this is a string enclosed in single quotes'
s2 = "this is a string enclosed in double quotes"
s3 = '''this is a multi-string,
enclosed in triple quotes'''
print(s1,s2,s3, sep='\n')

'''this is an informative 
multiline comment
created by using triple double quotes'''


# In[11]:


###Escape characters 
print('a\nb') #new line
print('a\tb') #tab or four spaces
print('a\rb') #moves cursur to start and overwrites as 'b'


# In[15]:


a = "this world cup belong's to INDIA"
print (a)
b= 'this world cup belongs\'s to INDIA'
print(b)


# ## raw strings : 
# it reads in raw format

# In[6]:


print('c:\abc\newfolder\j.jpg') #compilers error
print('c:\\abc\\newfolder\\j.jpg') #alternative method of printing
print(r'c:\abc\newfolder\j.jpg') #using r string


# In[20]:


r,h = 5,7
vol = (22/7)*(r**2)*h
print('the volume of a cyl, whose radius is ',r,'whose h is',h,'is',vol)
print(f'the volume of a cyl whose r and h are {r} and {h} respectively is {vol}') #format string 


# In[8]:


d = 10
r = d/2
pi = 22/7
vol = (4/3)*pi*(r**3)
print(f'the volume of sphere whose r is {r} is {vol}')



# In[12]:


print(f'a sphere with diameter {10} cms, volume will be {(22/7)*((10/2)**3)*(4/3)} cubic cms')


# In[33]:


### positive indexing : it begins with 0 and ends with n-1 where n is the length of the string.
### positive indexing moves from left to right.

x='python'
print(x[3])  #accessing 'h'


# In[36]:


### reverse indexing / negitive indexing : it begins with index -1 to -n , where n is length of string
### negitive indexing moves from right to left.
x = 'python'
print(x[-3])


# ### slicing
# Syntax: Object [start:stop:step] “Start” specifies the starting index of a slice. “Stop” specifies the ending element of a slice.To slice a sequence, you can use square brackets [] with the start and end indices separated by a colon.
# 1. start_index: start_index is the index of the first element in the sub-sequence
# 2. end_index :end_index is the index of the last element in the sub-sequence (excluding the element at the end_index ).
# 3. step_size :
# 

# In[46]:


x = 'welcome to innomatics'
print(len(x)) #length of string
print(x[0:10])
print(x[0:10:2])
print(x[::])
print(x[0:9])


# In[50]:


x = 'python'
print(x)
print(x[::-1])


# In[54]:


x = 'python'
print(x[-1:-6:-1])


# In[13]:


x ='python'
print(x[-6::-1])


# In[16]:


###string CONCATINATION :string concatenation is the operation of joining character strings end-to-end.
str1="Hello"
str2="Friends"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)


# In[ ]:




