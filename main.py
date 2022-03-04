split_word = []
correct_letters = []
wrong_letters = []
partial_result = []
def enterword():
    word = input("Enter the word: ")
    if len(word) < 1:
        enterword()
    else:
        split_word.append([c for c in word.lower()])
def partial():
    print("Wrong Letters: {}".format(str(wrong_letters).replace('[','').replace(']', '').replace(',', '').replace("'", '')))
    print(str(partial_result).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))
def enterletter():
    letterinput = input("Enter a letter: ").lower()
    while len(letterinput) < 1 or len(letterinput) > 1 or " " in letterinput:
        enterletter()
    for i in range(len(correct_letters)):
        if correct_letters[i][0] == letterinput:
            enterletter()
    for i in range(len(split_word[0])):
        if split_word[0][i] == letterinput:
                correct_letters.append([letterinput, i])
    print("\n" * 150)
    for i in range(len(correct_letters)):
        for z in range(len(split_word[0])):
            if correct_letters[i][0] == split_word[0][z]:
                partial_result[correct_letters[i][1]] = correct_letters[i][0]
    if letterinput not in wrong_letters and letterinput not in partial_result:
        wrong_letters.append(letterinput)
    partial()
    check()
    enterletter()
def check():
    if len(correct_letters) == len(split_word[0]):
        exit("Nice Job!")
enterword()
print("\n" * 150)
for i in range(len(split_word[0])):
    partial_result.append("_ ")
print(str(partial_result).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))
enterletter()
