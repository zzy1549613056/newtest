#!/usr/local/bin/python3

class Fib():
   def __init__(self):
     self.a ,self.b ,self.n = 0,1,0
   def __iter__(self):
     return self
   def __next__(self):
     self.a,self.b,self.n=self.b,self.a+self.b,self.n+1
     if self.n <= 10:
        return self.a
     raise StopIteration()