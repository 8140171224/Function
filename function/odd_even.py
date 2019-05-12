def count(lst):

    even = 0
    odd = 0

    for i in lst:

        if i%2==0:
            even+=1
        else:
            odd+=1


    return even,odd

lst = [25,35,51,65,5745,132,4,21,32,541]

even, odd = count(lst)
print(f'Even : {even} & odd : {odd}')
