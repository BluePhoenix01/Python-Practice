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

# Asserts
# assert spam < 10
# assert spam.lower() == bacon, "spam and bacon should be same"

# context managers

# class CtxManager:
#     def __init__(self) -> None:
#         print("made obj")
#         # self.file = open(...)

#     def __enter__(self):
#         print("entered context")
#         return "hello from context"
#         # return self.file

#     def __exit__(self, *args):
#         print("exit context")
#         # self.file.close()

# with CtxManager() as mg:
#     print(mg)
#     print("printed in context")

# Example for file open context manager

class FileOpen:
    def __init__(self, *args) -> None:
        self.file = open(*args)

    def __enter__(self):
        return self.file

    def __exit__(self, *args):
        self.file.close()

with FileOpen("test.txt", "w") as f:
    print(f.write("foobar"))