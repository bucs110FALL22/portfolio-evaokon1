class StringUtility:
  def __init__(self,string):
    self.string = string
    
  def __str__(self):
    return self.string
    
  def vowels(self):
    count = 0
    for i in self.string:
      if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count = count + 1
    if count < 5:
      return str(count)
    else:
      return "many"
      
  def bothEnds(self):
    if len(self.string) >= 2: 
       mystring = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
       return mystring
    else:
      return('')
      
  def fixStart(self):
    if len(self.string) >= 1:
      first_ch = self.string[0]
      for i in self.string:
        mystring = self.string[1: ].replace(first_ch,"*")    
      return self.string[0] + mystring
    else: 
      return ('')

  def asciiSum(self):
    ascii_codes = []
    for ch in range(len(self.string)):
      ascii_codes.append(ord(self.string[ch]))
    return sum(ascii_codes)

  def cipher(self):
    for ch in self.string: 
      mystring = "".join(chr(ord(ch)+len(self.string)) for ch in self.string)
    return mystring