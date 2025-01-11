#1
def sum(n):
    return n*(n+1)/2
print(sum(22))
#Space Complexity: O(1), Auxiliary Space: O(1)

#2
def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return(sum)
a = [11, 15, 7, 22]
print(arraysum(a))
#Space Complexity: O(n), Auxiliary Space: O(1)

#3
def sum2(n):
    if(n<=0):
        return
    return n+ sum2(n-1)
print(sum2(22))
#Space Complexity: O(n), Auxiliary Space: O(1)
    