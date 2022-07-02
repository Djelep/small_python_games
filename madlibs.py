# this project is crated mainly to show all the ways of formatting string in python

name = input("Enter your name: ")
age = input("Enter your age: ")
language = input("Enter your favorite programming language: ")


madlib = f"So you are {age} years old {name} who loves to write in {language}"
madlib2 = "So you are {0} years old {1} who loves to write in {2}".format(name, age, language)
madlib3 = ("So you are %s years old %s who loves to write in %s" % (name, age, language))


print(madlib3)