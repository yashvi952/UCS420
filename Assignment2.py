import random
from collections import Counter


# =========================================================
# Q1 - LISTS
# =========================================================

roll_no = input("Enter your roll number: ")

L = [int(digit) * 10 for digit in roll_no]

print("\nQ1(i) L =", L)


L.append(55)
print("\nAfter append(55):", L)


L.insert(2, 75)
print("After insert(2, 75):", L)


L.remove(55)
print("\nAfter remove(55):", L)


removed = L.pop(2)
print("Removed using pop():", removed)
print("After pop():", L)


L.sort()
print("\nAscending:", L)


L.sort(reverse=True)
print("Descending:", L)


print("\nFirst three:", L[:3])
print("Last three:", L[-3:])


avg = sum(L) / len(L)
above_average = [x for x in L if x > avg]

print("Average:", avg)
print("Greater than average:", above_average)



# =========================================================
# Q2 - TUPLES
# =========================================================

scores = tuple(L[:8])

print("\nScores:", scores)

highest = max(scores)
lowest = min(scores)

print("Highest:", highest)
print("Index:", scores.index(highest))

print("Lowest:", lowest)
print("Occurrences:", scores.count(lowest))


reversed_scores = list(scores[::-1])

print("Reversed:", reversed_scores)


search_score = int(input("\nEnter score to search: "))

if search_score in scores:
    print("Index:", scores.index(search_score))
else:
    print("Score not present.")



first_score, second_score, *remaining_scores = scores

print("First:", first_score)
print("Second:", second_score)
print("Remaining:", remaining_scores)



# =========================================================
# Q3 - RANDOM NUMBERS
# =========================================================

random.seed(int(roll_no))

numbers = [
    random.randint(100, 900)
    for _ in range(100)
]

print("\nRandom numbers:")
print(numbers)


odds = [x for x in numbers if x % 2 != 0]

print("\nOdd numbers:")
print(odds)
print("Odd count:", len(odds))


evens = [x for x in numbers if x % 2 == 0]

print("\nEven numbers:")
print(evens)
print("Even count:", len(evens))


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


primes = [x for x in numbers if is_prime(x)]

print("\nPrime numbers:")
print(primes)

print("Prime count:", len(primes))


counter = Counter(numbers)

most_common_number, count = counter.most_common(1)[0]

print("\nMost frequent number:", most_common_number)
print("Frequency:", count)



# =========================================================
# Q4 - SETS
# =========================================================

digits = [int(d) for d in roll_no[:8]]

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}

print("\nA =", A)
print("B =", B)


print("\nUnion:", A.union(B))

print("Intersection:", A.intersection(B))


print("A - B:", A.difference(B))
print("B - A:", B.difference(A))


print("Symmetric difference:",
      A.symmetric_difference(B))


print("A subset of B:",
      A.issubset(B))

print("B superset of A:",
      B.issuperset(A))


X = int(input("\nEnter X to remove from A: "))

A.discard(X)

print("A after discard:", A)



# =========================================================
# Q5 - DICTIONARIES
# =========================================================

my_dict = {
    "name": input("\nEnter name: "),
    "roll_no": roll_no,
    "branch": input("Enter branch: "),
    "age": int(input("Enter age: ")),
    "city": input("Enter home city: ")
}

print("\nOriginal dictionary:")
print(my_dict)

my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city:")
print(my_dict)


my_dict["cgpa"] = float(input("Enter CGPA: "))

print("\nAfter adding CGPA:")
print(my_dict)


my_dict["age"] += 1

print("\nAfter increasing age:")
print(my_dict)


dict_pop = my_dict.copy()
dict_del = my_dict.copy()


removed_branch = dict_pop.pop("branch")

print("\nUsing pop():")
print(dict_pop)
print("Returned value:", removed_branch)


del dict_del["branch"]

print("\nUsing del:")
print(dict_del)


print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)


if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email is not available.")


friend_dict = {
    "name": "Aarav Sharma",
    "roll_no": "1023456789",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}


merged = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged)


string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nOnly string values:")
print(string_values)
