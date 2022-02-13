"""
Your MinList class must implement the following functions:

- def push(val)
    - This function adds an element to the end of the list
- def pop()
    - This function removes the last element of the list and 
      returns it
- def top()
    - This function returns the last element of the list
- def get_min()
    - This function returns the minimum element of the list

Notes:
- get_min() must NOT use any loops (for-loops, while-loops) or any 
  built in functions that get the minimum of the list automatically.
"""

# Uncomment and write your code here!


class MinList:
     arr = []

     def push(self, val):
         self.arr.append(val)

     def pop(self):
         num = self.arr[-1]
         del self.arr[-1]
         return num

     def top(self):
         return self.arr[-1]

     def get_min(self):
         sortarr = self.arr
         sortarr.sort()
         return sortarr[0]

l = MinList()
l.push(5)
l.push(1)
l.push(21)
l.push(534)
l.push(531)
l.push(4123)
l.push(89)

print(l.get_min())
