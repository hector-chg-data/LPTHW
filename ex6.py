x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "...a string with a right side."
new_string = w+e
print(new_string)

if (len(new_string) < (len(w)+len(e))):
    print("w+e shorter than the sum of its parts")
elif (len(new_string) == (len(w)+len(e))):
    print("w+e equals the sum of its parts")
else:
    print("w+e larger than the sum of its parts")

