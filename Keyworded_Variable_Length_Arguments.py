def person(name, **data):

    print(name)
    for i,j in data.items():
        print(i,j)



person('pythonistas',age=20,city='La',mob=999999999)
