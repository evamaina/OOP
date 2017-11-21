my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for value in my_list:
    my_file.write(str(value) + "\n")

my_file.close()
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()


"""Finally, we want to know how to read from our output.txt file.
 As you might expect, we do this with the read() function"""


"""Declare a variable, my_file, and set it equal to the file object
  returned by calling open() with both "output.txt" and "r".

Next, print the result of using .read() on my_file, like the example above.

Make sure to .close() your file when you're done with it!
 All kinds of doom will happen if you don't."""