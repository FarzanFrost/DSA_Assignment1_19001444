
# Horspool algorithm
# text = "cogwrgaccag"
#  pattern = "c_g"
# result = []

def preprocessingFunction(x):
    # This function goes through the pattern and creates a python dictionary which has the right most postion of a
    # character in the pattern excluding the last character
    pre_dict = {}
    value = 1  # value given to each character from right to left excluding the last character of the pattern is
    # given by the variable value
    valueFromRightExceptTheLastCharacter = len(x) - 2
    # index - 1 = length -1 -1 = length -2 , this part actually
    # skips the last character of the pattern
    for i in range( len(x) - 2, -1, -1):

        if x[valueFromRightExceptTheLastCharacter] in pre_dict:
            value += 1
            valueFromRightExceptTheLastCharacter -= 1
            continue
        # in this if loop we check if the character was already given a value, if so the characher is skipped. i.e
        # only the character rightmost in the pattern is considered other repetition are skipped.
        else:
            pre_dict[x[valueFromRightExceptTheLastCharacter]] = value
        value += 1
        valueFromRightExceptTheLastCharacter -= 1
    if not "_" in pre_dict:  # in case the wild-card is only at the last character in the pattern, as wild-card can
        # match to any character we have to consider the last character of the pattern.
        pre_dict["_"] = 1
    return pre_dict


# preprocessed_values = preprocessingFunction(pattern)
# print(preprocessed_values)


def StingMatchPosition(result, m, n, pattern, text, preprocessed_values):
    # In this function the text and the pattern are compared according to the rules of horspool algorithm
    # Since there may be wild-card in a pattern certain logical changes are included in this funtion.
    pos = 0
    # m = len(pattern)
    # n = len(text)

    while pos <= n- m:
        j = m - 1
        while j >= 0:
            if j == 0:
                # when the j become zero then it is in the first character in the pattern
                # which can produce several scenarios as wild-card may be present in the pattern
                if text[pos + j] == pattern[j] or pattern[j] == "_":
                    # Here, this if condition runs when the first character of the pattern and the 1st character of
                    # the selected window in the text have the same character or pattern has a wild-card print(
                    # "occurrence found at",pos+j)
                    result.append(pos + j)

                if text[(pos + m - 1)] in preprocessed_values:  # here is checks if the last character of the selected
                    # window is in the preprocessed dictionary
                    # We have to move the pattern in a minimum distance between a related character in the dictionary
                    # and the position on the wild-card, as wild card can match to any characters.
                    pos = pos + min(preprocessed_values[text[pos + m - 1]], preprocessed_values["_"])
                else:
                    # if the last character of the selected window is not in the preprocessed dictionary, then we get
                    # the minimum distance between the length of the pattern and the distance of the right most
                    # wild-card
                    pos = pos + min(m, preprocessed_values["_"])
                break
            else:
                if text[pos + j] == pattern[j]:
                    # when j is not zero and the pattern and selected text window have a match then we move to
                    # compare the next character (we move from right to left)
                    j -= 1
                else:
                    if pattern[j] == "_":
                        # when j is not zero and the pattern and the selected text does not have a direct match but
                        # the pattern contains a wild-card there then we consider that as a match and move to the
                        # next character (we move from right to left)
                        j -= 1
                    else:
                        # We have to move the pattern in a minimum distance between a related character in the
                        # dictionary and the position on the wild-card, as wild card can match to any characters.
                        if text[(pos + m - 1)] in preprocessed_values:
                            pos = pos + min(preprocessed_values[text[pos + m - 1]], preprocessed_values["_"])
                        else:
                            # if the last character of the selected window is not in the preprocessed dictionary,
                            # then we get the minimum distance between the length of the pattern and the distance of
                            # the right most wild-card
                            pos = pos + min(m, preprocessed_values["_"])
                        break


# StingMatchPosition(result)
#
# if len(result) != 0:
#     print("The locations where match was found are: ", result)
# else:
#     print("No match found")



