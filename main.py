import pyperclip

# Here is where a user can paste in all of the Links / IP addresses that they want to defang. All of this input is stored
# in a string variable named dataInput
print("Paste in the different IP addresses/links and when done press enter twice to defang it:")
dataInput = ''
while True:
    lineInDataInput = input().strip()
    if lineInDataInput == '':
        break
    else:
        dataInput += lineInDataInput + '\n'

# Here is where the string is broken up into pieces and each piece is stored in a list
input_string = dataInput

# Split the input string into separate lines
lines = input_string.split("\n")

# Create a list to store the separate values
valuesCopy = []

# Loop over each line and append it to the list of values
for line in lines:
    valuesCopy.append(line)

# remove the last value on the list which is empty space as a result of how the break statement is used to tell the program no more data is coming
valuesCopy.pop()

# Here is where the data is defanged and then stored in the list called defanged values
# Print the list of values
defangedValues = []
for value in valuesCopy:
    tempValue = value.replace(".", "[.]")
    defangedValues.append(tempValue)

# Here pyperclip is used to copy the defanged values to the users clipboard
my_list = defangedValues

# Join the items in the list with a newline character
list_string = "\n".join(my_list)

# Copy the string to the clipboard
pyperclip.copy(list_string)

print("####################################################################################################")
print("Paste in the different IP addresses/links. You can either enter them in one by one and click enter to add another or you can simply paste multiple in at once. When you are done press enter twice to defang:")
print("####################################################################################################")

for value in defangedValues:
    print(value)
