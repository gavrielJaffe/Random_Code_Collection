# Student dictionaries
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}

tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

class_list_names = [tyler, alice, lloyd]  # List of student dictionaries

# Function to calculate average
def average(numbers):
  total = float(sum(numbers))
  total = total / len(numbers)
  return total

# Function to calculate the average score of a student
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  sum = (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
  return sum

# Function to assign letter grade based on score
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

# Function to calculate the average score for the entire class
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  
  return average(results), results

# Main function
def main():
  print(get_letter_grade(get_average(lloyd)))  # Print letter grade for Lloyd
  print("class_list_names:", class_list_names)  # Print the list of student dictionaries
  print(" ")
  print(get_class_average(class_list_names))  # Print class average score and individual scores
  print(get_class_average(class_list_names))
  print(get_letter_grade(get_class_average(class_list_names)))  # Print class average grade

if __name__ == '__main__':
    main()
