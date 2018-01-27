for x in range(100):
    message = raw_input("enter in a message to decode or in code, or press q to quit\n")
    if message == "incode":
        key = raw_input("enter in a key from 1 - 26")
        message = message.upper()
        output = ""
        for letter in message:
            if letter.isupper():
                value = ord(letter) + key
                letter = chr(value)
                if not letter.isupper():
                    value -= 26
                    letter = chr(value)
            output += letter
        print "Output message:  ", output

    elif message == "decode":

        key = 13
        message = message.upper()
        output = ""
        for letter in message:
            if letter.isupper():
                value = int((26 - key))
                if not letter.isupper():
                    value -= 26
                    letter = chr(value)
            output += letter
        print "Output message:  ", output
