import random
def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes)-1        #updates code automaticaly if quotes file is modified
    rnd = random.randint (0, last)  #choose a random value in an interval and atributes it to the variable rnd
    print(quotes[rnd])

if __name__== "__main__":
    primary()

