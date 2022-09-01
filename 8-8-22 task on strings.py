# test 1
1.What is String in Python?
A sequence of character which are enclosed in single(‘ ‘) or double (“”) quotes is known as String.
--------
2.Is there any difference in ‘a’ or “a” in python?
No, becauseA sequence of character which are enclosed in single(‘ ‘) or double (“”) quotes is known as String so there is no difference in "a" or'a'
--------
3.Is there any difference between 1 or ‘1’ in python?
Yes, why because 1 is is an interger and the character where the digit is enclosed with quotes is know as not string.
-------
4.Python treats single quotes same as double quotes.(T/F)
 True
-------
5.A string with zero character is called __________ string.
 Empty
------
6. Python does not support a character type.(T/F)
True
-------
7.Write a code to store following String in a variable named ‘str’.            This is Amit’s Blog
str="This is Amit's Blog"
print(str)
----------
8.Write the output of the following code:
str1 = "Welcome to my blog"
str2 = "Welcome to my \n Blog"
print(str1)
print(str2)
str1 will print:"Welcome to my blog"
str2 will print:Welcome to my
                Blog # \n will break the line add it will continue in another new line
----------
9.Write the output of the following.
str1 = "Welcome \tto my Blog"
str2 = "Welcome to\n my \tBlog
print(str1)
print(str2)
str1 will print:"Welcome   to my Blog" \t is used for tab space
str2 will print: Welcome to
 my 	Blog
----------
10.Write the output of the following.

str1 = “”” Welcome to my
                blog.
                This is for
                Class X”””
                print(str1)
                will print:Welcome to my
                blog.
                This is for
                Class X

#test 2
1.str="hello"
print(str[:3])
will print:hel
-------
2.str=’My Blog’
    a=""
for i in range(len(str)):
    a+=str[i]
    print(a)
will print: My Blog
--------
3.
str='MyBLog'
a=' '
for i in range(len(str)):
    print(i * str[i])
    y
    BB
    LLL
    oooo
    ggggg
---------
4.  s='My'
    s1='Blog'
s2=s[:1]+s1[len(s1)-1:]
print(s2)
will print:
Mg
---------
5. print(“My”+’Blog’ * 2)
wil print:MyBlogBlog
----------------------
6.print(“My” *3 + “Blog” +’7′)
will print:
MyMyMyBlog7
---------
7.for i in range(2,7,2):
    print(i * '2')
    will print:
22
2222
222222

8. for i in range(3,12, 2):
    print("a".upper())
A
A
A
A
A
----------
9.for i in range(3,12,13):
    print("a".upper)
will print:<built-in method upper of str object at 0x7f7781cacbf0>
--------
10.s='Welcome to My Site https://csiplearninghub.com '
       print(s.find('come'))
       print(s.find('o'))
       print(s.find('o', 10, 20))
       print(s.find('o', 5, 10))
will print:
3
4
-1
9
---------
#3.test
1.Write a code to create empty string 'str1'
str1=""
print(str1)
---------
2.What do you mean by traversing a string?
Traversing a string means accessing all the elements of the string one after the other by using the subscript. A string can be traversed using for loop or while loop.
-----------
3.What is the index value of first element of a string?
0
----------
4.What is the index value of last element of a string?
-1
----------
5.If the length of the string is 10 then what would be the positive index value of last element?
9
-------------
6.If the length of string is 9, what would be the index value of middle element?
4
----------------
7.Index value of a string can be in float. (T/F)
True
----------------------
8.What type of error is returned by following statement, if the length of string 'str1' is 10.
NameError: name
'str1' is not defined
 ----------------------
9.
Write the output of the following:
str1 = "Welcome to my Blog"

a. print(str1[-1])
b. print(str1[9])

wll print:
g
o
----------
10.Write a code to assign a string "Hello World"' to a string variable named "str1".
str1="hello World"

#4.test
1.Write a program to display each character of the following string in separate line using 'for' loop.
                                       str1 = Welcome to My Blog
for i in str1:
    print(i)
2. Write a program to display each character of the following string in separate line using 'while' loop.
                                       str1 = Welcome to My Blog
count=0
n=len(str1)
while count<n:
    print(str1[count])
    count+=1
----------
3. Write a program to display each character of the following string in separate line using 'while' loop.
                                       str1 = Welcome to My Blog
True
--------------------
4. Write the positive and negative index value of 'B' in the following string.
                "Welcome to my Blog"
the positive index is 14 when the index is start from 0
the negative index is -1 when the index is start from -1
----------------
5.What do you mean by concatenation of string?
 by adding tow strings is know as string concantenation
----------------
6.  Which of the following is an example of concatenation?

       a.  6 + 3
       b.  '6' + '3'
       c.  'a' + 'b' + 'c'
b and c
-----------------
7.   Write a program to count the length of string without using inbuilt function.
str="Thundersoft"
count=0
for i in str:
    count+=1
print(count)
------------------

Q8. Write the output of the following statement.

str1 = "Welcome to my Blog"
for i in str1:
    print(i)
    print(i, end =' ')
    print(i, end = '#')
    will print

    -----------
9.Write the output of the following statement.

str1 = "Amit"
for i in str1:
    print(i)
    print(i, end =' ')
10.Write the output of the following statement.

    str1 = "Welcome to my Blog"
    for i in str1:
        print(i)
        print(i, end =' ')
    print(i, end = '#')
# test 5
1.