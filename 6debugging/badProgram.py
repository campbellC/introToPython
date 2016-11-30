# This program should take a string with HTML tags and remove the HTML tags
# e.g. "<b>foo</b>" ---> "foo"

def stripOffHTML(s):
    insideString=False
    tag = False
    out = ""
    for index,c in enumerate(s):
        if c == "'" and tag:
            insideString = not insideString

        elif c == '<' and not insideString:
            tag = True

        elif c == '>' and not insideString:
            tag = False
        elif not tag:
            out = out + c

    return out



testInput1 = "<b>foo</b>"
print stripOffHTML(testInput1)


testInput2 = '<em>foo</em>'
print stripOffHTML(testInput2)

testInput3= "<a href='foo.html'>foo</a>"
print stripOffHTML(testInput3)



# import pdb; pdb.set_trace()
testInput4 = "'<a href='>.html'>foo</a>'"
print stripOffHTML(testInput4)



















































































































