#notes on a piano

class BPaw:   
   
    def __init__(self,name,colr,stem,fnger,xloc,duration,adjduration,notenum):
        
        self.name = name     
        self.colr = colr
        self.stem = stem
        self.fnger = fnger
        self.xloc = xloc
        self.duration = duration
        self.adjduration = adjduration
        self.notenum = notenum
      
    

#c3--------------------------------------------------------------------
c3 = BPaw('c3','1','up','index','5','','',48)
cs3 = BPaw('cs3','1','up','index','5','','',49)
d3 = BPaw('d3','2','up','middle','4.45','','','50')
ds3 = BPaw('ds3','2','up','middle','4.45','','',51)
e3 = BPaw('e3','1','dwn','ring','4.40','','',52)
f3 = BPaw('f3','0','dwn','pinky','3.36','','',53)
fs3 = BPaw('fs3','0','dwn','pinky','3.36','','',54)
g3 = BPaw('g3','1','dwn','index','2.7','','',55)
gs3 = BPaw('gs3','1','dwn','index','2.7','','',56)
a3 = BPaw('a3','2','dwn','middle','2.22','','',57)
as3 = BPaw('as3','2','dwn','middle','2.22','','',58)  
b3 = BPaw('b3','1','dwn','ring','1.57','','','59')
#C4--------------------------------------------------------------------
c4 = BPaw('c4','0','up','thumb','.97','','',60)
cs4 = BPaw('cs4','0','up','thumb','.97','','',61)
d4 = BPaw('d4','1','up','index','.4','','',62)
ds4 = BPaw('ds4','1','up','index','.4','','',63)
e4 = BPaw('e4','2','up','middle','-0.17','','',64)
f4 = BPaw('f4','1','up','ring','-0.72','','',65)
fs4 = BPaw('fs4','1','up','ring','-0.72','','',66)
g4 = BPaw('g4','0','up','thumb','-1.29','','',67)
gs4 = BPaw('gs4','0','up','thumb','-1.29','','',68)
a4 = BPaw('a4','1','dwn','index','-1.86','','',69)
as4 = BPaw('as4','1','dwn','index','-1.86','','',70)  
b4 = BPaw('b4','2','dwn','middle','-2.28','','',71)
#C5--------------------------------------------------------------------
c5 = BPaw('c5','1','dwn','ring','-2.03','','',72)
cs5 = BPaw('cs5','1','dwn','ring','-2.03','','',73)
d5 = BPaw('d5','0','dwn','thumb','-3.5','','',74)
ds5 = BPaw('ds5','0','dwn','thumb','-3.5','','',75)
e5 = BPaw('e5','1','dwn','index','-4.1','','',76)
f5 = BPaw('f5','2','dwn','middle','-4.8','','',77)
fs5 = BPaw('fs5','2','dwn','middle','-4.8','','',78)
g5 = BPaw('g5','1','dwn','ring','-5.25','','',79)
gs5 = BPaw('gs5','1','dwn','ring','-5.25','','',80)
a5 = BPaw('a5','0','dwn','thumb','-1.86','','',81) #
as5 = BPaw('as5','0','dwn','thumb','-1.86','','',82)  
b5 = BPaw('b5','1','up','index','-2.28','','',83)
#C6--------------------------------------------------------------------
c6 = BPaw('c6','2','up','middle','-2.03','','',84)
cs6 = BPaw('cs6','2','up','middle','-2.03','','',85)
d6 = BPaw('d6','1','up','ring','-3.6','','',86)
ds6 = BPaw('ds6','1','up','ring','-3.6','','',87)
e6 = BPaw('e6','0','up','thumb','-4.1','','',88)
f6 = BPaw('f6','1','up','index','-4.8','','',89)
fs6 = BPaw('fs6','1','up','middle','-4.8','','',90)
g6 = BPaw('g6','2','dwn','ring','-6.26','','',91)
gs6 = BPaw('gs6','2','dwn','ring','-6.26','','',92)
a6 = BPaw('a6','1','dwn','thumb','-1.86','','',93) #
as6 = BPaw('as6','1','dwn','thumb','-1.86','','',94)  
b6 = BPaw('b6','0','dwn','index','-2.28','','',95)



# BPaw is my class- it works as expected using obj.attribute to get values

# r is an entirely separate python list, I need to "for loop" through this r list
# and pull corresponding attribute values out of my BPaw class for a particular note - because this r list is made up of strings and not
# objects it wont let me

# How do I do it take a note from the r list and get attribute info out of my class  without getting str attribute errors, any note in my class is an object, not a string

r =['c54', 'c64', 'd64', 'e64', 'f64', 'g64', 'f44', 'g44', 'e42', 'g44']

for x in r:
    
  return BPaw.?????????????
