fin=open("Players.txt","r")
fout=open("Players_cleaned.txt","w")
for line in fin:
  name,position,nationality=line.strip().split("\t")
  print(name)
  print(position)
  print(nationality)
  name=name[10:]
  print(name,len(name))
  fout.write(name[:len(name)//2]+"\t"+position+"\t"+nationality+"\n")

fout.close()
fin.close()
