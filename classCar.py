class Car(object):
    condition = "new"


def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg


def display_car(self):
    print "This is a %s %s with %s MPG." % (
        self.color, self.model, str(self.mpg))

    my_car = Car("DeLorean", "silver", 88)

    my_car.display_car()

    """Inside the Car class, add a method named display_car to Car
     that will reference the Car's member variables to return the
      string, "This is a [color] [model] with [mpg] MPG."
       You can use the str() function to turn your mpg
       into a string when creating the display string.

Replace the individual print statements with a single 
print command that displays the result of calling
 my_car.display_car()"""
