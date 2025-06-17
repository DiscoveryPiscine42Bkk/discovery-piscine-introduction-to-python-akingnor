def add_one(x):
    x += 1
    print(f"Inside add_one, x = {x}")

num = 5
print(f"Before calling add_one, num = {num}")

add_one(num)

print(f"After calling add_one, num = {num}")