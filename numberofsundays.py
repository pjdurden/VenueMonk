#Prajjwal Chittori
#Delhi Technological University(2k18/co/249)
#8700694107
#prajjwalchittori_2k18co249@dtu.ac.in
from typing import List
import math
class Solution:
    def numberofSundays(self, startingyear:int,endingyear:int):
        #we can use zeller's cogruence to calculate the day of the week
        #https://en.wikipedia.org/wiki/Zeller%27s_congruence#:~:text=Zeller's%20congruence%20is%20an%20algorithm,day%20and%20the%20calendar%20date.
        # and then we'll calculate the number of sundays from 1901 to 2000
        sundays=0
        days=2
        month = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(startingyear,endingyear+1):
            month[1] = 28 + ((i%4==0 and i % 100 !=0) or i%400==0)
            for j in range(0,12):
                days+=month[j]%7
                if days%7==0:
                    sundays+=1
        print("number of sundays are")
        return sundays

a=Solution()
print(a.numberofSundays(1901,2000))
