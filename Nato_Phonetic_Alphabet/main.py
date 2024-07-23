with open("file1.txt") as file1:
    f1 = file1.readlines()
with open("file2.txt") as file2:
    f2 = file2.readlines()
"""
f1_new = [int(num.replace("\n", "")) for num in f1]
f2_new = [int(num.replace("\n", "")) for num in f2]
"""

result = [int(x) for x in f1 if x in f2]

print(result)