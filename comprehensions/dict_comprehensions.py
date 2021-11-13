"""
Dictionary comprehension is a simpler or concise way of declaring dictionary 

dictionary = {key: value for var in iterable}
"""
old_price = {"milk": 1.02, "coffee": 2.5, "butter": 3.5}

cube_dict = dict()
for num in range(1, 20):
    cube_dict[num] = num ** 3
print("Cube roots dict: ", cube_dict)

cubed = {num: num ** 3 for num in range(0, 20)}
print("COnsize declaration: ", cubed)

new_price = {item: value * 0.76 for (item, value) in old_price.items()}
print("Updated Price: ", new_price)

person_data = {"John": 36, "micheal": 25, "Russom": 45, "hap": 58}
even_age = {k: v for (k, v) in person_data.items() if v % 2 == 0}
print("Even aged persons: ", even_age)

even = {k: v for (k, v) in person_data.items() if v % 2 == 0 if v < 40}
print("Even aged persons whose age less than 40: ", even)

y_o = {k: ("old" if v > 40 else "young") for (k, v) in person_data.items()}
print(y_o)

dic1 = dict()
for k1 in range(1, 10):
    dic1[k1] = dict()
    for k2 in range(1, 5):
        dic1[k1][k2] = k1 * k2


dic = {k1: {k2: k1 * k2 for k2 in range(1, 5)} for k1 in range(1, 10)}
print(dic)

words = ["data", "python", "django", "webscraping", "tensorflow"]

print({string: len(string) for string in words if len(string) > 5})

print({string: "long" if len(string) > 5 else "short" for string in words})

zip_dict = {i: j for i, j in zip(words, range(len(words)))}
print(zip_dict)
