import sys


# +- Takes input +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-


sys.stdout.write("Hello world!\n")  # equivalent to print("Hello world!")


# +- Debugging +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-


# if we know something went wrong about we can bundle this up with try and execpt
# so that the other program keeps running

sys.stderr.write("Oopies! Something went wrong! GET BACK TO WORK...\n")

# +- read data as input +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

print("something idk:")
line = sys.stdin.readline()  # reads a line from input
print("something idk is:", line)


