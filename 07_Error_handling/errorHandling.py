file = open("sampleText.txt", "w") # This will create a new file if it doesn't exist

try:
    file.write("Hello, world!")

finally:
    file.close()
# The file is closed here, regardless of whether an error occurred or not
# This is important because it ensures that resources are properly released
# This is an old way of handling files in Python

with open("sampleText.txt", "w") as file:
    file.write("Hello, world!")
# The file is automatically closed when the block is exited
# This is the preferred way of handling files in Python