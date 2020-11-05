#Prajjwal Chittori
#Delhi Technological University(2k18/co/249)
#8700694107
#prajjwalchittori_2k18co249@dtu.ac.in
from typing import List
class Solution:
    mod=1000000007
    def numberofWays(self, money:List[int],N):
        #we can solve this by dynamic programming by using the following reccurence relation
        # numberofways(sum)=sigma(1 to N)(numberofways(sum-money[i]))
        # to reach a given sum, we will first calculate all the ways we can
        # reach sum-money[i] and then add it to the current sum for i 1 to N
        # the pseudo algorithm will be
        #for i 1  to N:
            #for j 0 to number of notes:
                #if (i >= money[j]):
                    #sum[i] += sum[i - money[j]]
        l=len(money)
        dp = [0 for i in range(N + 1)]
        dp[0] = 1
        for i in range(1, N + 1):
            for j in range(l):
                if (i >= money[j]):
                    dp[i] += dp[i - money[j]]
        print("number of ways to get",N)
        return dp[N]%self.mod

a=Solution()
money=[10, 20, 50, 100, 200, 500, 1000,2000]
print(a.numberofWays(money,2000))
