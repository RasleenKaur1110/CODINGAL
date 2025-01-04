def OnSquareTime(n):
    iteration = 0
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
            iteration+=1
        print()#Empty print is used to go to the next line
    print(f"\n When n is {n} Iterations = {iteration}")

OnSquareTime(5)
OnSquareTime(4)
OnSquareTime(3)

print("\n With every 'n' the time taken equals n^2")
print("O(n^2)")