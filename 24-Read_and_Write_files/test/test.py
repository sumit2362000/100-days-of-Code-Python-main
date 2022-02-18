

"""Reading Files"""

# file = open("my_file.txt", mode='r')
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

"""Writing to files"""
'''deletes all old text and adds new'''
# with open("my_file.txt", mode='w') as file:
#     file.write("New text.")

'''Appends to file'''
# with open("my_file.txt", mode='a') as file:
#     file.write("Even newer text.")

'''If new file doesn't exist, will create new file for you'''
# with open("created_file.txt", mode='w') as file:
#     file.write("Created file with text.")

'''Modify file on desktop, in Python use '/' and not '\' '''
# with open("/Users/janti/OneDrive/Desktop/test.txt",mode='w') as file:
#     file.write("Success!")