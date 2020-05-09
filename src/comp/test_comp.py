import unittest

# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [i.name for i in humans if i.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [i.name for i in humans if i.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters = ["C", "D", "E", "F", "G"]
c = [i.name for i in humans if i.name[0] in letters ]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age + 10 for i in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [i.name + "-" + str(i.age) for i in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(i.name, i.age) for i in humans if i.age in range(27, 33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(i.name.upper(), i.age + 5) for i in humans]
print(g)
print(humans) #unmodified

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]
print(h)


def compare_humans(inp, exp):
  if len(inp) != len(exp):
    return False
  for i in range(len(inp)):
    if inp[i].name != exp[i].name:
      return False
    if inp[i].age != exp[i].age:
      return False
  return True

class CompTests(unittest.TestCase):
  def test_starts_with_D(self):
    self.assertEqual(a, ['Daphne', 'David'])

  def test_ends_with_e(self):
    self.assertEqual(b, ['Alice', 'Charlie', 'Daphne', 'Eve'])

  def test_between_C_and_G(self):
    self.assertEqual(c, ['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David'])

  def test_ages_plus_10(self):
    self.assertEqual(d, [39, 42, 47, 40, 36, 28, 52, 22, 51, 41])

  def test_name_hyphen_age(self):
    self.assertEqual(e, ['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31'])

  def test_names_ages_between_27_and_32(self):
    self.assertEqual(f, [('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)])

  def test_all_names_uppercase(self):
    expected = [Human("ALICE", 34), Human("BOB", 37), Human("CHARLIE", 42), Human("DAPHNE", 35), Human("EVE", 31), Human("FRANK", 23), Human("GLENN", 47), Human("HARRISON", 17), Human("IGON", 46), Human("DAVID", 36)]
    self.assertTrue(compare_humans(g, expected))

  def test_square_root_of_ages(self):
    self.assertEqual(h, [5.385164807134504, 5.656854249492381, 6.082762530298219, 5.477225575051661, 5.0990195135927845, 4.242640687119285, 6.48074069840786, 3.4641016151377544, 6.4031242374328485, 5.5677643628300215])


if __name__ == '__main__':
  unittest.main()
