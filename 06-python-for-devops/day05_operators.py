# Arithmetic Operators
print(10 + 20)
print(20 - 10)
print(10 * 20)
print(10 / 5)
print(10 // 4)
print(10 ** 4)
print(10 % 3)

# Comparison Operators
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
print(10 >= 10)
print(10 <= 5)

# Assignment Operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

# Logical Operators
print(True and True)
print(True or False)
print(not False)

# DevOps Example
server_running = True
disk_usage = 65

print(server_running)
print(disk_usage < 80)

if server_running and disk_usage < 80:
    print("Server is Healthy")
else:
    print("Check Server")