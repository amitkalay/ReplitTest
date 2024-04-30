from collections import deque

import imageCache


def readTheTestFile(file_name: str):
  imageCache.img_func()
  with open(file_name) as file:
    for line in file:
        print(line)

def aFunction() -> str:
  print("running a function")
  test_deque = deque()
  return "something"

# aFunction()

readTheTestFile("testFile.txt")