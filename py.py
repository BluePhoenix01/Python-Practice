#Input validation
# while True:
#     try:
#         age = int(input("enter ur fking age"))
   
#     except ValueError:
#         continue
#     break
# print(age + 1)

#iterator for for loop
# numbers = [3, 5, 45, 68]
# numbers_iter = iter(numbers)
# while True:
#     try:    
#         print(next(numbers_iter))
#     except StopIteration:
#         break

# _ variable
# variable_FS = "henlo bye pye"
# a, _, __ = variable_FS.partition("bye")
# print(a, _, __)

#Generators
# def generate_ID(start):
#     count = start
#     while True:
#         yield count
#         count += 1
    
# id_generator = generate_ID(6782)

# print(next(id_generator))
# print(next(id_generator))

# Python Debugger
# def fact(num):
#     fact = 1
#     for i in range(1, num+1):
#         breakpoint()
#         fact *= i
#     return fact

# print(fact(10))

assert spam < 10
assert spam.lower() == bacon