# Quinten Reed
# U4L2
# A Simple Reverse

from StackClass import ArrayStack

def clean_text(text):
  new = ""

  for item in text:
    if item == "\n" or item == " " or 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
      new += item

  return new

def reverse(original):
  new_string = ""
  new_stack = ArrayStack()

  for item in original:
    new_stack.push(item)

  for i in range(len(new_stack)):
    new_string += new_stack.pop()

  return new_string

def main():
  file_name = "earnest.txt"
  with open(file_name, 'r') as openFile:
    original = openFile.read()
    original = clean_text(original)
    original = original.split("\n")
    
    for i in range(len(original)):
      original[i] = original[i].split(" ")
  
  new = ""

  for i in range(len(original)):
    for jtem in original[i]:
      new += reverse(jtem) + " "
    
    new += "\n"

  with open("reversed.txt", 'w') as openFile:
    openFile.write(new)

if __name__ == "__main__":
  main()