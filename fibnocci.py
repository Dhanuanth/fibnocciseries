c=0
d=1
i=int(input("Enter the length of the sequence: "))
print(c)
print(d)
while i>=3:
    print(c+d)
    s=c+d
    c=d
    d=s
    i-=1

