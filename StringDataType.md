### Strings 
1.a string is a sequence of characters. For example, "hello" is a string containing a sequence of characters 'h' , 'e' , 'l' , 'l' , and 'o' . (enclosed in sigle , double and triple quotes) 

2. triple quotes are used as multiline strings multiline comments as a doc strings.



```python
s1 = 'this is a string enclosed in single quotes'
s2 = "this is a string enclosed in double quotes"
s3 = '''this is a multi-string,
enclosed in triple quotes'''
print(s1,s2,s3, sep='\n')

'''this is an informative 
multiline comment
created by using triple double quotes'''
```

    this is a string enclosed in single quotes
    this is a string enclosed in double quotes
    this is a multi-string,
    enclosed in triple quotes
    




    'this is an informative \nmultiline comment\ncreated by using triple double quotes'




```python
###Escape characters 
print('a\nb') #new line
print('a\tb') #tab or four spaces
print('a\rb') #moves cursur to start and overwrites as 'b'
```

    a
    b
    a	b
    b
    


```python
a = "this world cup belong's to INDIA"
print (a)
b= 'this world cup belongs\'s to INDIA'
print(b)
```

    this world cup belong's to INDIA
    this world cup belongs's to INDIA
    

## raw strings : 
it reads in raw format


```python
print('c:\abc\newfolder\j.jpg') #compilers error
print('c:\\abc\\newfolder\\j.jpg') #alternative method of printing
print(r'c:\abc\newfolder\j.jpg') #using r string

```

    c:bc
    ewfolder\j.jpg
    c:\abc\newfolder\j.jpg
    c:\abc\newfolder\j.jpg
    


```python
r,h = 5,7
vol = (22/7)*(r**2)*h
print('the volume of a cyl, whose radius is ',r,'whose h is',h,'is',vol)
print(f'the volume of a cyl whose r and h are {r} and {h} respectively is {vol}') #format string 
```

    the volume of a cyl, whose radius is  5 whose h is 7 is 550.0
    the volume of a cyl whose r and h are 5 and 7 respectively is 550.0
    


```python
d = 10
r = d/2
pi = 22/7
vol = (4/3)*pi*(r**3)
print(f'the volume of sphere whose r is {r} is {vol}')


```

    the volume of sphere whose r is 5.0 is 523.8095238095237
    


```python
print(f'a sphere with diameter {10} cms, volume will be {(22/7)*((10/2)**3)*(4/3)} cubic cms')
```

    a sphere with diameter 10 cms, volume will be 523.8095238095237 cubic cms
    


```python
### positive indexing : it begins with 0 and ends with n-1 where n is the length of the string.
### positive indexing moves from left to right.

x='python'
print(x[3])  #accessing 'h'
```

    h
    


```python
### reverse indexing / negitive indexing : it begins with index -1 to -n , where n is length of string
### negitive indexing moves from right to left.
x = 'python'
print(x[-3])
```

    h
    

### slicing
Syntax: Object [start:stop:step] “Start” specifies the starting index of a slice. “Stop” specifies the ending element of a slice.To slice a sequence, you can use square brackets [] with the start and end indices separated by a colon.
1. start_index: start_index is the index of the first element in the sub-sequence
2. end_index :end_index is the index of the last element in the sub-sequence (excluding the element at the end_index ).
3. step_size :You can specify the step of the slicing using step parameter. The step parameter is optional 
and by default 1.



```python
x = 'welcome to innomatics'
print(len(x)) #length of string
print(x[0:10])
print(x[0:10:2])
print(x[::])
print(x[0:9])

```

    21
    welcome to
    wloet
    welcome to innomatics
    welcome t
    


```python
x = 'python'
print(x)
print(x[::-1])
```

    python
    nohtyp
    


```python
x = 'python'
print(x[-1:-6:-1])
```

    nohty
    


```python
x ='python'
print(x[-6::-1])
```

    p
    


```python
###string CONCATINATION :string concatenation is the operation of joining character strings end-to-end.
str1="Hello"
str2="Friends"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)

```

    String 1: Hello
    String 2: Friends
    Concatenated two different strings: HelloFriends
    


```python

```
