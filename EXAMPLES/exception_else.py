
numpairs = [(5, 1), (1, 5), (5, 0), (0, 5), (10, "15")]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
        total += quotient  # Only if no exceptions were raised
    except Exception as err:
        print(f"uh-oh, when y = {y}, {err}")
        break  # only for 'for' and 'while'
    finally:
        print("OK!")
print(total)

print("END OF PROGRAM")