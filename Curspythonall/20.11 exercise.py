# # Safely open the file
# file = open("hello.txt", "w")
#
# try:
#     file.write("Hello, World!")
# except Exception as x:
# #     print("Error is",x)
# # finally:
#     # Make sure to close the file after using it
#     file.close()

f = open(“test.txt”, "r")
print(f.readline())
f.close()

with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))


print(f.closed)  # True
