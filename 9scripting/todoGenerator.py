import argparse
import re
import os




parser = argparse.ArgumentParser()



parser.add_argument("-r","--recursive", help="set this to recurse down the file tree",
                    action="store_true")

parser.add_argument("--maxDepth", help="state a max-depth for recusion",
                    type=int)

parser.add_argument("filename",
                    help="The file or directory you want to gather TODO's from")

parser.add_argument("-extension", help="The extensions for compiled todo lists",
                    default='.todo')
args = parser.parse_args()

todoRE = re.compile(r"TODO:(?P<todo>.+)")

##############################################################################
######  Helper Functions
##############################################################################

def walklevel(directory, level=None):
    directory = directory.rstrip(os.path.sep)
    assert os.path.isdir(directory)
    numSep = directory.count(os.path.sep)
    for root, dirs, files in os.walk(directory):
        yield root,dirs,files
        if level is not None:
            localNumSep = root.count(os.path.sep)
            if numSep + level <= localNumSep:
                del dirs[:]


def indent(string, amount=4, char=' '):
    if string[-1] == '\n':
        return indent(string[:-1],amount,char)+'\n'
    padding = amount * char
    return padding + ('\n' + padding).join(string.split('\n'))

##############################################################################
######  Functions for handling the todos
##############################################################################


def todoCompilerFromFile( inFile):
    def helper(inFile):
        with open(inFile,'r') as f:
            output = ""
            for linenumber, line in enumerate(f):
                match = re.search(todoRE, line)
                if match is not None:
                    output += str(linenumber) + ":    " + match.group("todo") + "\n"
            if output != "":
                return output
            else:
                return None
    output = helper(inFile)
    if output is not None:
        return str(inFile) + ':\n' + indent(output) +'\n'
    else:
        return None

def todoCompilerFromDirectory(directory):
    fileTodos = ""
    for root,dirs,files in walklevel(directory,level=0):
        for filename in files:
            if filename[-3:] == 'swp' or filename[-4:] == 'todo':
                continue
            fullpath = os.path.join(root,filename)
            todos = todoCompilerFromFile(fullpath)
            if todos is not None:
                fileTodos = fileTodos + todos
    output = "-------------------\n" + str(directory) +":\n-------------------\n\n"
    if fileTodos != "":
        output += indent(fileTodos)
    return output


##############################################################################
######  Actual Script
##############################################################################
if os.path.basename(args.filename) == "":
    raise ValueError("Expected filename")
if args.filename == '.':
    outfile = os.path.basename(os.getcwd()) + args.extension
else:
    outfile = os.path.basename(args.filename) + args.extension

if os.path.isdir(args.filename):
    if not args.recursive:
        args.maxDepth = 0
    todos = ""
    for dirName, subdirList, fileList in walklevel(args.filename, args.maxDepth):
        if '.git' in dirName:
            del subdirList[:]
            continue
        level = dirName.count(os.path.sep)
        todos += indent(todoCompilerFromDirectory(dirName), 4 * level)
    with open(outfile,'w') as f:
        f.write(todos)


else:
    todos = todoCompilerFromFile(args.filename)
    if todos is not None:
        print todos
        with open(outfile,'w') as f:
            f.write(todos)


