"""Case Closed?
Finally, we'll want a way to test whether a file
 we've opened is closed. Sometimes we'll have a lot
of file objects open, and if we're not careful,
they won't all be closed. How can we test this?

f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True"""

with open("text.txt", "w") as my_file:
    my_file.write("My Data!")

if not file.closed:
    file.close()

print my_file.closed


"""Below your with...as code, do two things:

Check if the file is not closed.
If that's the case, call .close() on it.
(You don't need an else here, since your if statement
 should do nothing if closed is True.)
After your if statement, print out the value of
 my_file.closed to make sure your file is really closed."""