# Print all integers from 0 to 150
for a in range(0, 151):
    print(a)

# Print all the multiples of 5 from 5 to 1000
for b in range(5, 1005, 5):
    print(b)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisibly by 10m print "Coding Dojo".
for c in range(1, 101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

# Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for d in range(0,500001,2):
    sum += d
print(sum)

# Print postive numbers starting at 2018, countind down by fours
for e in range(2018,0,-4):
    print(e)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
lowNum = 2
highNum = 20
mult = 5
for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)