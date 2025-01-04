def OnTime(n):
    iteration = 0 
    for i in range(1, n+1):
        iteration+=1
    print(f"When n is {n} Iterations = {iteration}")

OnTime(10)
OnTime(20)
print("\n With every 'n' the time taken and iterations will increase")
          