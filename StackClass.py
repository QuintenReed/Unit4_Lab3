# Your Code & Heading go Here!

# Quinten Reed
# U4L1
# ArrayStack

class ArrayStack():
  def __init__(self):
    self.__size = 0
    self.__stack = []

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

  def __len__(self):
    """Returns the length of the stack"""
    return self.__size

  def __is_empty(self):
    return self.__size < 1

  def push(self, element):
    """Add element to the stack"""
    self.__stack.append(element)
    self.__size += 1

  def pop(self):
    """Remove element from the stack"""
    if self.__is_empty() == True:
      raise IndexError("stack has no elements")
    else:
      element = self.__stack[-1]
      del self.__stack[-1]
      self.__size -= 1
      return element

  def top(self):
    """Return the top element of the stack"""
    if self.__is_empty() == True:
      raise IndexError("stack has no elements")
    else:
      return self.__stack[-1]