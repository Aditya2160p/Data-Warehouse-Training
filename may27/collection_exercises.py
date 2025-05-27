# 1. List of Squares
squares=[]
for i in range(1, 21):
    squares.append(i**2)
print("Squares:", squares)

# 2. Second Largest Number (no sort)
nums = [12, 45, 2, 99, 45, 32]

largest = max(nums)
nums_without_largest=[]
for n in nums:
    if n != largest:
        nums_without_largest.append(n)

if nums_without_largest:
    second_largest = max(nums_without_largest)
    print("Second Largest:", second_largest)
else:
    print("No second largest value found.")


#3. Remove Duplicates Write a program to remove all duplicate values from a list
#while preserving order.
nums = [1, 2, 2, 3, 4, 3, 5]
no_dupli = set()
for num in nums:
    if num not in no_dupli:
        no_dupli.add(num)
print("Without Duplicates:", no_dupli)

# 4. Rotate List Rotate a list to the right by k steps. Example: [1, 2, 3, 4, 5]
# rotated by 2 → [4, 5, 1, 2, 3]
l = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    last = l.pop()
    l.insert(0, last)
print("Rotated List:", l)


# 5. List Compression From a list of numbers, create a new list with only the even
# numbers doubled.
nums = [1, 2, 3, 4, 5, 6]
c=[]
for x in nums:
    if x % 2 == 0:
        c.append(x * 2)
print("Even Doubled:", c)

#6.6. Swap Values Write a function that accepts two tuples and swaps their contents.
def swap_tuples(t1, t2):
    return t2, t1

a = (1, 2, 3)
b = (4, 5, 6)
a, b = swap_tuples(a, b)
print("a:", a)
print("b:", b)

#7.Unpack Tuples Unpack a tuple with student details: (name, age, branch, grade)
# and print them in a sentence.
student = ("Alex", 20, "CSE", "A")
name, age, branch, grade = student
print(f"{name} is {age} years old, studies {branch}, and got grade {grade}.")


#8.Tuple to Dictionary Convert a tuple of key-value pairs into a dictionary.
# Example: (("a", 1), ("b", 2)) → {"a": 1, "b": 2}
t = (("a", 1), ("b", 2))
d = dict(t)
print(d)


#9.9. Common Items Find the common elements in two user-defined lists using sets.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
print("Common elements:", list(common))


#10. Unique Words in Sentence Take a sentence from the user and print all unique
# words.
sentence = input("Enter a sentence: ")
words = sentence.split()
unique = set(words)
print("Unique words:", unique)

#11. Symmetric Difference Given two sets of integers, print elements that are in one
# set or the other, but not both.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symd = set1 ^ set2
print("Symmetric Difference:", symd)


#12.12. Subset Checker Check if one set is a subset of another.
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print("Set1 is subset of Set2:", set1.issubset(set2))

#13. Frequency Counter Count the frequency of each character in a string using a
# dictionary.
text = "apple"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Character Frequency:", freq)

#14. Student Grade Book Ask for names and marks of 3 students. Then ask for a name
# and display their grade ( >=90: A , >=75: B , else C).
students = {}
for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
query = input("Enter name to check grade: ")
if query in students:
    marks = students[query]
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Student not found.")

#15. Merge Two Dictionaries Merge two dictionaries. If the same key exists, sum the
# values.
d1 = {"apple": 10, "banana": 20}
d2 = {"banana": 5, "orange": 15}
merged = {}

for key in d1:
    merged[key] = d1[key]
for key in d2:
    if key in merged:
        merged[key] += d2[key]
    else:
        merged[key] = d2[key]

print("Merged Dictionary:", merged)

#16. Inverted Dictionary Invert a dictionary’s keys and values. Input: {"a": 1, "b":
# 2} → Output: {1: "a", 2: "b"}
original = {"a": 1, "b": 2}
inverted = {}

for key in original:
    value = original[key]
    inverted[value] = key

print("Inverted Dictionary:", inverted)

# 17. Group Words by Length Input a list of words. Create a dictionary where the key
# is word length and the value is a list of words of that length.
words = ["hi", "hello", "this", "apple", "hat"]
grouped = {}

for word in words:
    length = len(word)
    if length in grouped:
        grouped[length].append(word)
    else:
        grouped[length] = [word]

print("Words grouped by length:", grouped)
