for i in range(1, int(input())):
    print(i * (pow(10,i) - 1) // 9)

# #output  for N-1 which want in hackerRank rule
# 1
# 22
# 333
# 4444

# Why do we use n+1?
# In Python, range(start, end)
# the end value is NOT included 
# EX:-
# for i in range(1,5):
# 1
# 2
# 3
# 4

# 0 level
# n = int(input())
# for i in range(1, n+1):
#     print(i * i)



# for i in range(1, int(input()) + 1):
#     print(i * (10**i - 1) // 9)
# #output  for N+1
# 1
# 22
# 333
# 4444
# 55555


#by using str but this is not allowed in rule
# n = int(input())
# for i in range(1, n+1):
#     print(str(i) * i)