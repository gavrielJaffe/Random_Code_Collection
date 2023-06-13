#!/usr/bin/env python

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for lst in lists:
    for i in lst:
        results.append(i)
  return results


def main():
  print(flatten(n))
#   flatten(n)
  
if __name__ == '__main__':
    main()