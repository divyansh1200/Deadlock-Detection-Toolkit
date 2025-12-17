# Main program file

from banker import is_safe
from graph import draw_graph

print("\nDEADLOCK DETECTION & PREVENTION TOOLKIT\n")

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

alloc = []
print("\nEnter Allocation Matrix:")
for i in range(n):
    while True:
        row = input(f"Process {i}: ").split()
        if len(row) != m:
            print(f"Enter exactly {m} numbers")
        else:
            alloc.append(list(map(int, row)))
            break

maxm = []
print("\nEnter Maximum Need Matrix:")
for i in range(n):
    while True:
        row = input(f"Process {i}: ").split()
        if len(row) != m:
            print(f"Enter exactly {m} numbers")
        else:
            maxm.append(list(map(int, row)))
            break

while True:
    avail = input("\nEnter Available Resources: ").split()
    if len(avail) != m:
        print(f"Enter exactly {m} numbers")
    else:
        avail = list(map(int, avail))
        break

# DEBUG PRINT (VERY IMPORTANT)
print("\nDEBUG CHECK")
print("Allocation:", alloc)
print("Maximum:", maxm)
print("Available:", avail)

safe, sequence = is_safe(n, m, alloc, maxm, avail)

if safe:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:", sequence)
else:
    print("\nDEADLOCK detected!")

draw_graph(n, m, alloc)

