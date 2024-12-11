input_string = input("Enter principal amount, rate of interest, and time period separated by spaces: ")
x_str, y_str, z_str = input_string.split()

x = float(x_str)
y = float(y_str)
z = float(z_str)

result = x * y * z / 100
print(result)
