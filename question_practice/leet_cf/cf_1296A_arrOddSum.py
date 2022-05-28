# we have to check if we can make array with odd sum
# for this purpose :

# If there is no odd number, then no matter how to move it will
# stay all even, so it’s NO.

# If there is odd number and even number, then it can be YES
# because it can make the number of odds an odd number.

# If there is only odd number, checkout for the total number n, if
# n is a odd number, then it’s YES; If n is an even number, then
# it’s NO.

# solution
user = int(input())
for i in range(user):
    len_arr = int(input())
    a = list(map(int, input().split()))
    ans = 0  # if ans is odd then yes
    odd = 0  # if odd is odd then yes
    even = 0  # if even & odd both-> yes, only even 0 odd then no

    for j in range(len_arr):
        ans += a[j]
        if a[j] % 2 != 0:
            odd += 1
        else:
            even += 1
    if (even != 0 and odd == 0) or (even == 0 and odd % 2 == 0):
        print("NO")
    else:
        print("YES")


# my try: aya hi nahi

# user = int(input())
# for i in range(user):
#     len_arr = int(input())
#     a = list(map(int, input().split()))
#     if sum(a) % 2 != 0:
#         print("YES")
#     else:
#         print("NO")
