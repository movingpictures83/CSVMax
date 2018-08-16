import sys
#import numpy
import PyPluMA


class CSVMaxPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      self.m = 0
      for line in filestuff:
         contents = line.split(',')
	 self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            self.ADJ[self.m].append(value)
         self.m += 1

   def output(self, filename):
      for i in range(self.m):
         max = -1
         for j in range(self.n):
            if (self.ADJ[i][j] > max):
               max = self.ADJ[i][j]
         print "I: ", i, " MAX: ", max   



