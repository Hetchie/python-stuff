# the snake names python does your homework

print "the snake, Python does your math!"

problem = raw_input ("enter in a math problem or press q to quit:\n")
while (problem != 'q'):
    print "the awnser to", problem, "is:", eval(problem)

    problem = raw_input("enter in a math problem or press q to quit:\n")
