my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()


# f = open("output.txt", "w")
"""This told Python to open output.txt in "w" mode
 ("w" stands for "write"). We stored the result of
  this operation in a file object, f.Doing this opens
   the file in write-mode and prepares Python
    to send data into the file.

    
1. write-only mode ("w")
2.read-only mode ("r")
3.read and write mode ("r+")
4.append mode ("a"), which adds any new data you write to the file to the end of the file.
"""