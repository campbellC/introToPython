#This program should take a string with HTML tags and remove the HTML tags
#e.g. "<b>foo</b>" ---> "foo"
# THIS PROGRAM IS STILL BROKEN
def stripOffHTML(s):
    tag = False
    insideQuote = False
    out = ""
    for index,c in enumerate(s):

        if c == '<' and not insideQuote:
            tag = True

        elif c == '>' and not insideQuote:
            tag = False
        elif c== "'" or c == '"' and tag:
            insideQuote = not insideQuote
        elif not tag:
            out = out + c

    return out

import pdb; pdb.set_trace()
testInput4 = "'<a href='>.html'>foo</a>'"
print stripOffHTML(testInput4)


testInput1 = "<b>foo</b>"
print stripOffHTML(testInput1)

testInput2 = "<em>foo</em>"
print stripOffHTML(testInput2)

testInput3= "<a href='foo.html'>foo</a>"
print stripOffHTML(testInput3)



