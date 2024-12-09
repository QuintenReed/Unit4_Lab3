# Quinten Reed
# U4L2
# A Simple Reverse

from StackClass import ArrayStack

def reverse(original):
  new_string = ""
  new_stack = ArrayStack()

  for item in original:
    new_stack.push(item)

  for i in range(len(new_stack)):
    new_string += new_stack.pop()

  return new_string

def main():
  original = "Sphinx of black quartz, judge my vow"
  new = ""

  new = reverse(original)

  print(f"Original: {original}")
  print(f"Reversed: {new}")

if __name__ == "__main__":
  main()