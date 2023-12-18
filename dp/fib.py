

def fib(n):
    arr = []
    for i in range(0, n+1):
        if i == 0:
            arr.append(0)
             
        elif i == 1:
            
            arr.append(1)
        elif i == 2:
            
            arr.append(1)
        else:
            n1 = arr[i-1]
            n2 = arr[i-2]
            arr.append((n2 + n1) % 1000000007)

    print('arr[n] ->', arr[n], arr[n-1], arr[n-2])
    return arr[n]






print(fib(2))
print(fib(3))
print(fib(45))
