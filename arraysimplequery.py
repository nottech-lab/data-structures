# Enter your code here. Read input from STDIN. Print output to STDOUT
nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = list(map(int, input().split()))

for _ in range(m):
    a,b,c = [int(n) for n in input().split()]
    if a == 1:
        arr = arr[b-1:c]+arr[:b-1]+arr[c:]
    elif a == 2:
        arr = arr[:b-1]+arr[c:]+arr[b-1:c]

f = arr[::-1]
print(abs(arr[0]-f[0]))
print(*arr)