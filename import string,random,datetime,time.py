import string,random,datetime,time
f=open('market_data.txt')
print "Enter number of columns"
No_of_Columns=int(raw_input())
print "enter datatypes of the columns"
dataTypes=[]
for i in xrange(No_of_Columns):
    b=raw_input()
    dataTypes.append(b.lower());    
f1=open('new_market_data.txt','w')
for j in xrange(50):
    data=[]
    for i in dataTypes:
        if(i == "date"):
            year = random.choice(range(1950, 3001))
            month = random.choice(range(1, 13))
            day = random.choice(range(1, 29))
            date=datetime.datetime(year,month,day)
            f1.write('{:%Y%m%d}'.format(date))
        elif (i == 'int'):
            integer= random.choice(range(0, 10001))
            f1.write(integer)
        elif (i== 'string'):
            s=''.join(random.choice(string.ascii_lowercase) for _ in xrange(3))
            f1.write(s.upper())
        elif(i=='time'):    
            hour=random.choice(range(1, 25))
            minutes=random.choice(range(0, 61))
            seconds=random.choice(range(0, 61))       
            f1.write("%02d:%02d.%02d" % (hour, minutes, seconds))
        elif(i=='float'):
            flot=random.uniform(1.1, 9.9)
            f1.write("%0.02f" % (flot))
        if(i!=len(dataTypes)):
            f1.write(',')
        else:
            f1.write('\n')
f1.close()
f.close()
