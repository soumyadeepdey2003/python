class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        print(self.day," : ",self.month," : ",self.year)
    def next_day(self):
        if(self.day<30):
            print(self.day+1," : ",self.month," : ",self.year)
        elif(self.day==30 and self.month<12):
            print(1," : ",self.month+1," : ",self.year)
        else:
            print(1," : ",1," : ",self.year+1)
date1=Date()
date2=Date(15)
date3=Date(2,10)
date4=Date(5,11,2002)

date1.display()
date2.display()
date3.display()
date4.display()

date5=Date(30,11,2002)
date6=Date(30,12,2002)
date7=Date(5,11,2002)

date5.next_day()
date6.next_day()
date7.next_day()