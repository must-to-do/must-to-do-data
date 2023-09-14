arr = [None]*6

def swap(num1, num2):
    arr[num1], arr[num2] = arr[num2], arr[num1]

#main

n, m = map(int, input().split())
for i in range(1, n+1):
    arr[i] = i

for i in range(0, m):
    n1, n2 = map(int, input().split())
    swap(n1, n2)


for i in range(1, n+1):
    print(arr[i], end=' ')

