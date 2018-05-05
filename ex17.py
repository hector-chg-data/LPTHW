from sys import argv as agv
from os.path import exists

script, from_file, to_file = agv

prompt = ">"

print("Copying from %s to %s..." %(from_file, to_file))

#we could do these two in one line too, how?
in_file = open(from_file)
indata = in_file.read()

indata2 = open(from_file).read()

print("The input file is %d bytes long" %(len(indata)))
print("And using the other method it's %d bytes long" %(len(indata2)))

print("Does the output file exists? %r" %(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL+C to abort.")
input(prompt)

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, everything done. :)")

out_file.close()
in_file.close()





