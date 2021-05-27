#WAP that multiplies 2 integer numbers without using """ (*) """ operator, use repeted additon:

x = int(input("Enter any number : "))
y = int(input("Enter how many times the number should be multiplied with : "))

t = ()

for i in range(y):
    t += (x,)

print(x,"x",y,"=",sum(t))