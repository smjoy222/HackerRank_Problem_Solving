a = int(input())
b = int(input())
m = int(input())

if b < 0 or m <= 0:
    print("Invalid input")
else:
    print(pow(a, b))   
    print(pow(a, b, m))   #  to calculate a^b and mod m


# from hackerRank problem
# Note: Here, a and b can be floats or negatives, 
# but, if a third argument is present, b cannot be negative.

# Note: Python has a math module that has its own pow().
# It takes two arguments and returns a float. It is uncommon to use math.pow().