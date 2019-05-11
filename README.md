# Class-Object-function
basic class and object
# Function & Arguments

    def function define
    def add (x,y) is an example of adding numbers
    def add(x,y):
        c = x+y
        print(c)

    add(45,85)

# Function & Keyword

    def person(name,age):
        print(name,age)


    person(age=85,name='pythonistas')

# Function & default answer
 
     def person(name,age=18):
        print(name,age)


     person(name='pythonistas')

# Variable length argument function

    def sum(a, *b):
        for i in b:
            a = a + i


        print(a)


    sum(4,5,6)
