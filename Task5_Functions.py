

"""
#function declaration
def about_me(firstname, lastname, age):
    print("My name is " + firstname + " " + lastname + " and my age is " +str(age)) #str() is converting the integer to a string

#calling the function with an argument
about_me("Emma", "Watson", 37)
"""

#The addition of default values allows for polymorphism
def about_me(firstname="DefaultFirst", lastname="DefaultLast"):
    print("My name is " + firstname + " " + lastname)

about_me("Test")
about_me("Nikk", "One")