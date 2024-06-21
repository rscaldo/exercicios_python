"""    LAB   Your own split
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument – a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
Use the template in the editor. Test your code carefully.


Expected output
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[] """

# MY SOLUTION
def mysplit(strng):
    strng_list = []
    word = ''
    for str in strng:
      if str == ' ':
       strng_list.append(word)
       word = ''
      else:
        word += str
    return strng_list




print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


""" def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return [ ]
    # prepare a list to return
    lst = []
    # prepare a word to build subsequent words
    word = ''
    # check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not strng[0].isspace()
    # iterate through all the characters in the string
    for x in strng:
        # if we are currently inside a string...
        if inword:
            # ... and the current character is not a space...
            if not x.isspace():
                # ... update the current word
                word = word + x
            else:
                # ... otherwise, we've reached the end of the word so we need to append it to the list...
                lst.append(word)
                # ... and signal the fact that we are outside the word now
                inword = False
        else:
            # if we are outside the word and we've reached a non-white character...
            if not x.isspace():
                # ... it means that a new word has begun so we need to remember it and...
                inword = True
                # ... store the first letter of the new word
                word = x
            else:
                pass
    # if we've left the string and there is a non-empty string in the word, we need to update the list
    if inword:
        lst.append(word)
    # return the list to the invoker
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit("")) """