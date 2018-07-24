import random
import datetime
f = open('rpt.xml') #name of the XML file 
 #name of the output file
for i in xrange(600):
    outputfile="output" + str(i) + ".txt"
    f1 = open(outputfile, 'a')    
    for line in f.readlines():
         # change the values randomly 
        if '>' in line and (line[line.index('>')+1].isalnum()):
            l1=line[0:line.index('>')+1]
            line=line.replace(l1,'')
            l2=line[0:line.index('<')]
            line=line.replace(l2,'')
            l3=line[0:line.index('>')+1]
            l2=''.join(random.sample(l2,len(l2)))
            line=l1+l2+l3
            #print line
            #print    
        f1.write(line)
    line=datetime.datetime.now()
    f1.write(line)
f1.close()
f.close()
