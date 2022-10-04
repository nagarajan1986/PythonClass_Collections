#jumping statement
# break    continue

for i in range(1,10):
    if i==5:
        break
    print(i)
print("program exited")

for i in range(1,10):
    if i==5:
        continue
    print(i)
print("program exited")

for i in range(1,10):
    if i==5 or i==7 or i==8:
        continue
    print(i)
print("program exited")