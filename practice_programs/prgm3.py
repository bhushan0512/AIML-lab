num = int(input("Enter your number:"))
output = 0
l =[]
while num>0:
    l.append(num%10)
    num = int(num/10)
l = sorted(l)
length = len(l)
for i in range(length):
    output = output + l[i] * (10**(length-i-1))
print(output)