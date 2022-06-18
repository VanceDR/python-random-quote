import random
import string
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  # Removing Newline (\n) using .strip()
  # First Quote
  rnd = random.randint(0,last)
  noNewLine = quotes[rnd].strip()
  print(noNewLine)

  # Second Quote
  rnd = random.randint(0,last)
  noNewLine = quotes[rnd].strip()
  print(noNewLine)

  newQuote = str(input("Type out New Quote Here: "))
  f = open("quotes.txt", 'a') # 'a' for append
  f.write("\n") # add new line to add in the next line
  f.write(newQuote) # remove newline
  f.close() # close file

if __name__== "__main__":
  primary()
