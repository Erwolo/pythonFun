# break loop

x, y = 0, 0
while (True):
    x += 1
    y += 2
    if(x+y > 10):
        break
print(str(x) + " " + str(y))

# for loop

a = [1, 4, 6]
for i in a:
    print(i)

# range keyword

for i in range(30):
    print(i)

# continue

for i in range(30):
    if not (i % 3):
        continue
    print(i)

# chuj idk cvo to

primes = []
for i in range(2, 100):
    for x in range(2, i):
        if(i % x == 0):
            break
    else:
        primes.append(i)
print(primes)
