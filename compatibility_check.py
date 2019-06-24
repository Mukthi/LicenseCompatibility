# Script for compatibility check

license_matrix = [
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 1],
[1, 0, 1, 0, 1]
]

licenses = {0: "GPL 2.0", 1: "GPL 3.0", 2: "BSD New", 3: "BSD Old", 4: "MIT"}

print("Please use the values from 0 to n from the licenses given below for your entries")
print("*"*80)

for key, value in licenses.items():
	print(key, ":", value)


license1 = input("Enter the first license: ")
license2 = input("Enter the second license: ")

output = license_matrix[license1][license2]

if output:
	print (licenses[license1], " is compatible with ", licenses[license2])
else:
	print (licenses[license1], " is not compatible with ", licenses[license2])
