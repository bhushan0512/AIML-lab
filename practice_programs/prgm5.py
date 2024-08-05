l = [2,5,2,2,8,6,4,8,2,1,8]

output = {} 

for i in l:
    if i in output.keys():
        output[i] +=1
    else:
        output[i]= 1
print(l)
print(output)
print(max(output.values()))