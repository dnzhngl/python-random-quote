import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)- 1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  def isItSame():
    if rnd == rnd2 :
      rnd2 = random.randint(0, last)
      isItSame()
      return rnd2
    
  print(quotes[rnd],quotes[rnd2], end='')

def writeQuote():
  quote = input("Enter quote :")
  f = open("quotes.txt", "a")
  f.write("\n" + quote)
  f.close()
  
if __name__== "__main__":
  primary()
  writeQuote()
