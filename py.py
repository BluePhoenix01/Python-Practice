
# while True:
#     try:
#         age = int(input("enter ur fking age"))
   
#     except ValueError:
#         continue
#     break

# print(age + 1)

# numbers = [3, 5, 45, 68]
# numbers_iter = iter(numbers)
# while True:
#     try:    
#         print(next(numbers_iter))
#     except StopIteration:
#         break

variable_FS = "henlo bye pye"
a, _, __ = variable_FS.partition("bye")
print(a, _, __)