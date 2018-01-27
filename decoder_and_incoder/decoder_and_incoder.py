for x in range(100):
    message = raw_input("enter in a message to deecode or in code, or press q to quit\n")
    message = message.upper()
    output = ""
    for letter in message:
        if letter.isupper():
            value = ord(letter) + 13
            letter = chr(value)
            if not letter.isupper():
                value -= 26
                letter = chr(value)
        output += letter
    print "Output message:  ", output
