tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a new line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat= """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

####################

import subprocess as sp

while True:
    for i in ["/","-","\\","|"]:
        print("%s\r" %(i))
        sp.call('clear', shell=True)
