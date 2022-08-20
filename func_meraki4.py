numbers= [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def ordered_list(numbers):
    i=0
    while i<len(numbers):
        numbers.sort()
        i+=1
    print(numbers)
ordered_list(numbers)