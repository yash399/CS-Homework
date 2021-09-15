'''# QUESTION 1
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
spl_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
space = [' ']

array = []

char = []
digit = []
special = []
alpha = []

attempts = int(input("Enter the number of attempts: "))

for i in range(attempts):
    string = input(f"Write the line {i+1}: ")
    split_string = string.split(" ")
    st = list(string)
    for letter in st:
        if letter in alphabets:
            alpha.append(letter)
        if letter in numbers:
            digit.append(letter)
        if letter in spl_char:
            special.append(letter)

print("Total Characters: ",len(st))
print("Total Alphabets: ",len(alpha))
print("Total Digits: ",len(digit))
print("Total Special Characters: ",len(special))
print("Total Words : ",len(split_string) )
'''


"""# QUESTION 2
input_string='the brown fox'
array=input_string.split()
for word in array:
    new_word = ''
    input_string = ''.join(word[0].upper() + word[1:])
    print(input_string)
"""



'''#QUESTION 3
input_string = input("Enter the string: ")
array = input_string.split()
simple_array=set(array)
st = ' '.join(simple_array)
print(st)
'''



'''#QUESTION 4
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
array = []
converted_array = []
input_string = input("Enter the string: ")
for num in list(input_string):
    if num in numbers:
        array.append(num)
for num in array:
    converted_num = int(num)
    converted_array.append(converted_num)
print(array)
print(sum(converted_array))
'''


'''#QUESTION 5
string = input("Write a sentence: ")
split_string = string.split()
hyphen_string = ';'.join(split_string)
print(hyphen_string)
'''