import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)- 1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  isItSame(rnd, rnd2, last)
    
  print(quotes[rnd],quotes[rnd2], end='')
  
def isItSame(rnd1, rnd2, last):
  if rnd1 == rnd2 :
    rnd2 = random.randint(0, last)
    isItSame()
    return rnd2

def writeQuote():
  quote = input("Enter quote :")
  f = open("quotes.txt", "a")
  f.write("\n" + quote)
  f.close()
  
if __name__== "__main__":
  primary()
  writeQuote()
