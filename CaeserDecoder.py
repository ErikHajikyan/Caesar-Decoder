import json


def loadletterencr():
    with open('cd_letters.json') as data_file:
        cd_letters = json.load(data_file)
        letters = cd_letters['letters']
        return letters


def encr_decr():
    print "    "
    print "Choose an option ( INPUT 1,2 OR 3)"
    print "1 - Encode"
    print "2 - Decode"
    print "3 - Exit"
    need = str(raw_input())
    while True:
        if need == "1" or need == "2":
            return need
        elif need == "3":
            print "See you :)"
            exit()
        else:
            need = str(raw_input("Wrong input, please enter 1,2 or 3"))


def askfor_encrword(need):
    file = open("saved_data.json", "r")
    saved_data = json.load(file)
    print("Enter the sentence/word you want to encode/decode here(the sentence should be with lowercase letters):  ")
    answer = str(raw_input())
    print("Enter the number by which you want to shift elements in your word/sentence:  ")
    shift = int(raw_input())
    if answer in saved_data:
        for item in saved_data[answer]:
            if need == "1" and item["shifted by"] == shift:
                print "The word is:" + str(item["encr"])
            elif need == "2" and item["shifted by"] == shift:
                print "The word is: " + str(item["decr"])

    return answer, shift


def isInt(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


def encrypt(encr_word, letters, shift, need):
    if need == "1":
        encrypted_word = ""
        for key in encr_word:
            if key == " ":
                encrypted_word = encrypted_word + " "
            elif shift not in range(0, 52):
                print ("Invalid input. You cannot shift your word/sentence by ", shift,". Max is 52, Min is 0. ")
                break
            elif isInt(key):
                encrypted_word = encrypted_word + str((int(key) + shift)%10)
            else:
                index = letters.index(key)
                new_index = index + shift
                if new_index > len(letters):
                    new_index = new_index - len(letters)
                encrypted_word = encrypted_word + letters[new_index]
        print encrypted_word
        return encrypted_word


def decrypt(encr_word, letters, shift, need):
    if need == "2":
        decrypted_word = ""
        for key in encr_word:
            if key == " ":
                decrypted_word = decrypted_word + " "
            elif shift not in range(0,52):
                print("Invalid input. You cannot shift your word/sentence by ", shift,". Max is 52, Min is 0. ")
                break
            elif isInt(key):
                decrypted_word = decrypted_word + (str((int(key)-shift)%10))
            else:
                index = letters.index(key)
                new_index = index - shift
                if new_index < 0:
                    new_index = len(letters) + new_index
                decrypted_word = decrypted_word + letters[new_index]

        print decrypted_word
        return decrypted_word


def savecoding(word, encrypted_word, decrypted_word,shift):
    file = open("saved_data.json", "r")
    saved_data = json.load(file)
    if word not in saved_data:

        saved_data[word] = []
    saved_data[word].append({"encr": encrypted_word,"decr": decrypted_word,"shifted by": shift})
    file.close()

    file = open("saved_data.json", "w")
    file.write(json.dumps(saved_data))
    file.close()


def main():
    print "This is the program which will help you to encode or decode words, sentences, numbers."
    print "You will be able to choose the shift by which you can move the elements in your word."
    need = encr_decr()
    encr_word, shift = askfor_encrword(need)
    letters = loadletterencr()
    encrypted_word = encrypt(encr_word, letters, shift, need)
    decrypted_word = decrypt(encr_word, letters, shift, need)

    savecoding(encr_word, encrypted_word,decrypted_word, shift)


main()

