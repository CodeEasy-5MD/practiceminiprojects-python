sum = 0
avg = 0
count = 0
j = 100
while j >= 0:
    if j%2 == 1:
        print(j)
        sum += j
        count += 1
    j-=1

avg = sum/count
print("Sum =\n", sum)
print("Average=\n ", avg)

