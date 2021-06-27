import os
import stringMatching

# In this file we read data from the file named inputTestData we read each line with in a while loop,
# each line contains the text and the pattern separated by a space, As we split them into a list, and we use the
# horspool algorithm which we have defined and imported from stringMatching.py file and then we simply output the
# result in a console

readTestDataFromFile = open(r"inputTestData", 'r')
oneLine = readTestDataFromFile.readline()
i = 1
while oneLine and oneLine != []:
    try:
        result = []
        oneLineList = oneLine.split()
        text = oneLineList[0]
        pattern = oneLineList[1]
        print("Test Number: ", i)
        print("The text: ", text)
        print("The Pattern: ", pattern)
        preprocessed_values = stringMatching.preprocessingFunction(pattern)
        stringMatching.StingMatchPosition(result, len(pattern), len(text), pattern, text, preprocessed_values)
        if len(result) != 0:
            print("The locations where match was found are: ", result)
        else:
            print("No match found")

        print()
        oneLine = readTestDataFromFile.readline()
    except IndexError:
        oneLine = readTestDataFromFile.readline()

    i += 1

readTestDataFromFile.close()

text = "cogwr gaccag"
pattern = " "
result = []

preprocessed_values = stringMatching.preprocessingFunction(pattern)
# print(preprocessed_values)
print("Test Number: ", i)
print("Test on empty string")
print("The text:", text)

stringMatching.StingMatchPosition(result, len(pattern), len(text), pattern, text, preprocessed_values)

if len(result) != 0:
    print("The locations where match was found are: ", result)
else:
    print("No match found")
os.system("pause")
