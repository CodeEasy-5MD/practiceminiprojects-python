sum = 0
count = 0
avg = 0

#block for the for loop
for m in range (0, 101):
#block for the if statement
    if m%2 ==0:
        print(m)
        sum+=m
        count = count+1

#block to calculate average
avg = sum/count
print("Sum=\n", sum)
print("Average\n", avg)


