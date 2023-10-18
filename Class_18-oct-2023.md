1. <b>Class :</b> a class is a user-defined data type that contains both the data itself and the methods that may be used to manipulate it.Classes serve as a template to create objects. 
    A class describes the contents of the objects that belong to it: it describes an aggregate of data fields (called instance variables), and defines the operations (called methods). 

2. <b>object:</b> an object is an element (or instance) of a class; objects have the behaviors of their class.

3. <b>method() : </b> methods are functions that are associated with an object and can manipulate its data or perform actions on it.
4. <b>ASCII : </b> ASCII stands for American Standard Code for Information Interchange. It is a numeric value given to different characters and symbols, for computers to store and manipulate. For example, the ASCII value of the letter 'A' is 65.



```python
x=10 #integer datatype
print(x,type(x))
```

    10 <class 'int'>
    


```python
ord('A') 
ord('Z')
```




    90




```python
dir(x)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']




```python
y = "hardwork"
print(y,type(y))
```

    hardwork <class 'str'>
    


```python
dir(y)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']



1. strings are immutable the resulting strings from string methods have a new memory location.
2. in order to use these strings,we need reassign it to a var.


```python
tt = '''Betty Botter bought some butter
But she said the butter’s bitter
If I put it in my batter, it will make my batter bitter
But a bit of better butter will make my batter better
So ‘twas better Betty Botter bought a bit of better butter'''
tt
```




    'Betty Botter bought some butter\nBut she said the butter’s bitter\nIf I put it in my batter, it will make my batter bitter\nBut a bit of better butter will make my batter better\nSo ‘twas better Betty Botter bought a bit of better butter'




```python
tt.upper() #converts into capitals
print(id(tt))
```

    1972208280480
    


```python
p='tap'        # strings are immutable
n="TAP"
print(id(p))
id(n)
```

    1972201291952
    




    1972201291888




```python
T = tt.upper() 
T
id(T)
```




    1972208292800




```python
T.lower() #prints the complete string to lower case letters.
```




    'betty botter bought some butter\nbut she said the butter’s bitter\nif i put it in my batter, it will make my batter bitter\nbut a bit of better butter will make my batter better\nso ‘twas better betty botter bought a bit of better butter'




```python
T.capitalize() # 1st alphabet of the line is capital.
```




    'Betty botter bought some butter\nbut she said the butter’s bitter\nif i put it in my batter, it will make my batter bitter\nbut a bit of better butter will make my batter better\nso ‘twas better betty botter bought a bit of better butter'




```python
##title : converts 1st alphabet of every word is converted to capital.
T.title()
```




    'Betty Botter Bought Some Butter\nBut She Said The Butter’S Bitter\nIf I Put It In My Batter, It Will Make My Batter Bitter\nBut A Bit Of Better Butter Will Make My Batter Better\nSo ‘Twas Better Betty Botter Bought A Bit Of Better Butter'




```python
T.split() #The split() method splits a string into a list. 
```




    ['BETTY',
     'BOTTER',
     'BOUGHT',
     'SOME',
     'BUTTER',
     'BUT',
     'SHE',
     'SAID',
     'THE',
     'BUTTER’S',
     'BITTER',
     'IF',
     'I',
     'PUT',
     'IT',
     'IN',
     'MY',
     'BATTER,',
     'IT',
     'WILL',
     'MAKE',
     'MY',
     'BATTER',
     'BITTER',
     'BUT',
     'A',
     'BIT',
     'OF',
     'BETTER',
     'BUTTER',
     'WILL',
     'MAKE',
     'MY',
     'BATTER',
     'BETTER',
     'SO',
     '‘TWAS',
     'BETTER',
     'BETTY',
     'BOTTER',
     'BOUGHT',
     'A',
     'BIT',
     'OF',
     'BETTER',
     'BUTTER']




```python
T.swapcase() #if input is in caps o/p would be in lower case 
```




    'betty botter bought some butter\nbut she said the butter’s bitter\nif i put it in my batter, it will make my batter bitter\nbut a bit of better butter will make my batter better\nso ‘twas better betty botter bought a bit of better butter'



### casefold() :
This means the casefold() method converts more characters into lower case compared to lower() . For example, the German letter ß is already lowercase so, the lower() method doesn’t make the conversion. But the casefold () method will convert ß to its equivalent character ss .


```python
x="the ß character called eszett"
x.casefold()
```




    'the ss character called eszett'



### TASK (B) : 
1. Explain why strings are immutable by taking a string method() as an example.

<b>Immutable :</b> Immutable in Python is when you cannot change the object type over time.



```python

```


```python
x= "sowji"
print(id(x))
y = "sowji"
print(id(x))
```

    1972251104112
    1972251104112
    


```python
a = "Sowji" # 
print(id(a))# address of a is printed  
print(id(a.upper)) #when a method is used new object is created rather than overwriting the previous value
```

    1972259271984
    1972259691296
    

### Reverse one string


```python
str1 = "lets learn python"
str2 = "python is very interesting"
str1 = str1[::-1] #start index by default 0 :stop index by default last index 
print(str1)
            
```

    nohtyp nrael stel
    

### Concatenate two strings 


```python
str1 = "lets learn python"
str2 = "python is very interesting"
concat = str1 +str2
print(concat)

```

    lets learn pythonpython is very interesting
    

### Get the alternate chars of the concatenate string in reverse order.


```python
str1 = "lets learn python"
str2 = "python is very interesting"
concat = str1 +str2
concat = concat[::-2]
print(concat)
```

    gisrtiye inhynhy re tl
    
