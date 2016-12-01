i = 10
while(i >= 0):

    print i
    i -= 1

    while(True):
        print "continue? y/n"

        x = raw_input()

        if x == "y":
            break

        if x == "n":
            continue

        print x + " is not correct, try again!"
