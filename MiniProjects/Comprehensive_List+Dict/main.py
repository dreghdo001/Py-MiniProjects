import random
with open("file1.txt") as file1:
    f1 = file1.readlines()
with open("file2.txt") as file2:
    f2 = file2.readlines()
"""
f1_new = [int(num.replace("\n", "")) for num in f1]
f2_new = [int(num.replace("\n", "")) for num in f2]
"""
result = [int(x) for x in f1 if x in f2]
#print(result)

names = ["Alex", "Mihai", "Petrica", "Cosmin", "Marian", "Maria", "Cristina"]
students_score = {student:random.randint(1, 100) for student in names}

# Dictionary Comprehension - 1
passed_students = {student:score for (student, score) in students_score.items() if score > 60}
#print(passed_students)

# Dictionary Comprehension - 2
text_var = "What is the Airspeed Velocity of an Unladen Swallow?"
letter_count_dict = {word:len(word) for word in text_var.split(' ')}
#print(letter_count_dict)

# Dictionary Comprehension - 3
celsius_dict = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
fahrenheit_dict = {day: (temp_c * 9/5) + 32 for (day, temp_c) in celsius_dict.items()}
#print(fahrenheit_dict)

import pandas
dict = {
    "student": ["Alex", "Mihai", "Petrica"],
    "score": [56, 76, 89]
}
# Create a DF and export it to a CSV file
df = pandas.DataFrame(dict)
df.to_csv("grades.csv")

# Loop to a DataFrame in the wrong way
#for (key, value) in df.items():
#   print(f"{value}")

# Loop to a DataFrame in the right way
for(index, row) in df.iterrows():
    print(row.score)
