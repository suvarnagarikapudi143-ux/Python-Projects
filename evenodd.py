n=[11,13,12,14,15,16]
even=0
odd=0
for i in n:
    if i % 2 == 0:
        even+=i
    else:
        odd+=i
print("Even sum:",even)
print("odd sum:",odd)