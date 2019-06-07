import unidecode

class Player:
  def __init__(self,name,position,nationality):
   self.name=name
   self.position=position
   self.nationality=nationality
   self.scrabble_score=self.get_scrabble_score()

  #function that counts the scrabble score for a given name
  def get_scrabble_score(self):
    name_cleaned=clean(unidecode.unidecode(self.name.lower()))
    count=count_letters(name_cleaned)
    scrabble_scores={'a':1,'b':3,'c':3,'d':2,'e':1,
		     'f':4,'g':2,'h':4,'i':1,'j':8,
		     'k':5,'l':1,'m':3,'n':1,'o':1,
		     'p':3,'q':10,'r':1,'s':1,'t':1,
		     'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
    score=0
    for i in count.keys():
       score=score+count[i]*scrabble_scores[i]
    return score

  def __str__(self):
    return self.name+", who plays as a "+self.position+" for "+self.nationality+", has a scrabble score of "+self.scrabble_score

  def __lt__(self,other):
    return self.scrabble_score<other.scrabble_score

  def __gt__(self,other):
    return self.scrabble_score>other.scrabble_score

  def __le__(self,other):
    return not self.__gt__(other)

  def __ge__(self,other):
    return not self.__lt__(other)

#function that counts the number of letters in a string and saves it as a dictionary
#Eg. count_letters("chicken waffles") = {'a':1,'c':2,'e':2,'f':2,'h':1,'i':1,'k':1,'l':1,'n':1,'s':1,'w':1}
def count_letters(text):
  count={}
  for i in text:
    if(i in count.keys()):
      count[i]+=1
    else:
      count[i]=1
  return count

#function that takes in text and removes all non-lower case characters
#Eg. clean("chicke'n waffle!#@$%#@()@)#s") = "chickenwaffles"
def clean(text):
  for i in range(97):
    text=text.replace(chr(i),"")
  for i in range(123,256):
    text=text.replace(chr(i),"")
  
  return text

def main():
  fin=open("Players_cleaned.txt",'r')
  players=[]
  for line in fin:
    line=line.strip().split("\t")
    players.append(Player(line[0],line[1],line[2]))
  fin.close()

  players.sort(reverse=True)

  fout=open("Scrabble_Scores.txt",'w')
  fout.write("Name\tPosition\tNationality\tScrabble Score\n")
  for i in players:
    fout.write(i.name+"\t"+i.position+"\t"+i.nationality+"\t"+str(i.scrabble_score)+"\n")
  fout.close()

if(__name__=="__main__"):
  main()
