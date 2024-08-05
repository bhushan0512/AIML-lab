num = int(input("Enter a number:"))
l = []
output = 0
while num>0:
    l.insert(0,num%2)
    num = int(num/2)
# print(l)
length = len(l)
for i in l:
    output = output*10 + i
print("Binary equivalent is",output)