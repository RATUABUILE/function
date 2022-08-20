alphabet= ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
def reverse_list(alphabet):
    i=0
    while i<len(alphabet):
        alphabet.reverse()
        i+=1
    print(alphabet)
reverse_list(alphabet)