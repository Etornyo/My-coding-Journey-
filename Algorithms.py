#1. Eucledian Algorithm
a = int(input('Enter the First Number'))"asking for input"
b = int(input('Enter the Second Number'))
r = a%b

while r:"The while loop used to cause the change in values and later reduces it to the lowest term"
    a=b
    b=r
    r = a%b

print('GCD =' + str(b))"stringing the value to concatonate"


#2. Representation of Integers
def Base_expansion(n,b);
a=[]
q=n
k=0
n=int(input('Input a number to convert'))
b=int(input('Input the base number'))
 while q!=0:
     a.append(0)"This is to assign each number as a member of the list a"
     a[k]=q%b
     q=q/b
     k=k+1

a.reverse()"This reverses the position of the members of the array"
for i in range(i,len(0)):
    s = s + str(a[i])"Then in turn is added together and the comma usually separating each member is removed"
    return s


#3. Addition of Integers
def add(a, b, base):"creating a function"
    assert a > 0 and b > 0 and base > 1
    "Declaring some variables and a list"
    w = 0 
    v = []


    a = [int(i) for i in list(str(a))[::-1]]"stringing each member of the lists"
    b = [int(i) for i in list(str(b))[::-1]]
    
    n = len(a)
    
    for j in range(0, n):
        d = (a[j] + b[j] + w) // base "adding the two numbers and dividing by the base value"
        v.append(a[j] + b[j] + w - (base*d))"writing each value as a member in the list"
        w = d
    
    v.append(w)"final list to append and use"
    
    v = [str(i) for i in v[::-1]]"writing the members as one removing the commas"
    return int(''.join(v)) "stringing the new value" 


print(add(111, 111, 2))






