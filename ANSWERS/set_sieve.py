import sys

if len(sys.argv) == 2:
    limit = int(sys.argv[1])
else:
    limit = 1001

is_prime = set()

print(2, end=' ')  # we know 2 is prime
for num in range(3, limit, 2):  # only test odd numbers
    if num not in is_prime:
        print(num, end=' ')
        for x in range(num, limit, num):
            is_prime.add(x)
