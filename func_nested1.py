def first():
    def second():
        i=1
        sum=0
        while i<=10:
            sum=sum+1
            i+=1
        return sum+1
    return second()
print(first())