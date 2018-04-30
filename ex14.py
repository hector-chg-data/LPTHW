from sys import argv as input_terminal

script, user_name = input_terminal
prompt = "> "

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me, %s?" % user_name)
likes = input(prompt)

print("And, %s, where do you live?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so, as a summary, you said:
\t You live in %s. Not sure where that is...
\t You said \"%r\" to whether you like me or not.
\t And you also said that you have a %s computer.
""" %(lives, likes, computer))
