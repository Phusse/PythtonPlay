import random

# List of popular baby names
boy_names = ["Oliver", "Liam", "Noah", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander"]
girl_names = ["Olivia", "Emma", "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn"]

# Get user input for baby's gender
gender = input("Enter the baby's gender (boy or girl): ")

# Get the number of names to generate
num_names = int(input("Enter the number of names to generate: "))

# Generate and display baby names
print("\nGenerated Baby Names:")
if gender.lower() == "boy":
    generated_names = random.sample(boy_names, num_names)
else:
    generated_names = random.sample(girl_names, num_names)

for name in generated_names:
    print(name)


#new question
import re
from collections import Counter

def count_word_frequency(filename):
    word_frequency = Counter()
    with open(filename, 'r') as file:
        for line in file:
            words = re.findall(r'\w+', line.lower())
            word_frequency.update(words)
    
    return word_frequency

# Demonstration
filename = "words.txt"
word_frequency = count_word_frequency(filename)
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

for word, frequency in sorted_word_frequency:
    print(f"{word}: {frequency}")

#another one
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Demonstration
rectangle = Rectangle(5, 10)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()
print("Area:", area)
print("Perimeter:", perimeter)
