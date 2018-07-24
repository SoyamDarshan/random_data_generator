import string,random,datetime,time
print "Enter number of columns"
No_of_Columns=int(raw_input())
print "enter datatypes of the columns"
dataTypes=[]
for i in xrange(No_of_Columns):
    b=raw_input()
    dataTypes.append(b.lower());    

for k in xrange(20):
    d='output/new_market_data' + str(k) + '.txt'
    f1=open(d,'w')
    for j in xrange(50):
        for i in xrange(len(dataTypes)):
            if(dataTypes[i] == "date"):
                year = random.choice(range(1950, 3001))
                month = random.choice(range(1, 13))
                day = random.choice(range(1, 29))
                date=datetime.datetime(year,month,day)
                f1.write(('{:%Y%m%d}'.format(date)).replace('\r',''))
            elif (dataTypes[i] == 'int'):
                integer= random.choice(range(0, 10001))
                f1.write((str(integer)).replace('\r',''))
            elif (dataTypes[i]== 'string'):
                s=''.join(random.choice(string.ascii_lowercase) for _ in xrange(3))
                f1.write((s.upper()).replace('\r',''))
            elif(dataTypes[i]=='time'):    
                hour=random.choice(range(1, 25))
                minutes=random.choice(range(0, 61))
                seconds=random.choice(range(0, 61))       
                f1.write(("%02d:%02d.%02d" % (hour, minutes, seconds)).replace('\r',''))
            elif(dataTypes[i]=='float'):
                flot=random.uniform(1.1, 9.9)
                f1.write(("%0.02f" % (flot)).replace('\r',''))
            if(i<No_of_Columns-1):
                f1.write(',')
        f1.write("\n")
f1.close()
