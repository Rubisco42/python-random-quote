import random
#defining the function: function name is chosen. When the function is called, the corresponding script is run
def primary():
    #function defined, corresponding script (following) is indented
# creates a variable =  opening quote source file. "a"=append= add new content at the end of the opened file
    f = open("quotes.txt")
# creates another variable = reading lines of f= source file
    quotes = f.readlines()
#close opened file
    f.close()
#updates code automatically if quotes file is modified
    last = len(quotes)-1
#choose a random value in an interval and atributes it to the variable rnd
    rnd = random.randint (0, last)
#print more quotes at the same times
    rnd2 = random.randint (0, last)

    print(quotes[rnd], end="")
    print(quotes[rnd2])
# "end" remove extra line (= newline) between each random quote
#adding programmatically new quotes
    question = ''
    while question != 'yes':
#Quote bot is annoyingly insistant. creates a question loop looking for answer=yes
        print('Do u want ot add new quote?')
        question = input()
        if question == 'yes':
            print('Type the new quote')
            new_quote = input()
            g = open("quotes.txt", "a")
# "a" is the command to append the file (add at the end). "w" overwrites the file, "r" to open and read only.
            g.write(new_quote)
#this is a basic way to add on a new line each time code is run. But creates an empty line
            g.write("\n")
            g.close()
            print('thank u quoter')

#obsolete way to call the function
if __name__== "__main__":
#new way to call the function: function name followed by () is enough
    primary()
print('I am Quote Bot')