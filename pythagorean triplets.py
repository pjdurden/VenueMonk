#Prajjwal Chittori
#Delhi Technological University(2k18/co/249)
#8700694107
#prajjwalchittori_2k18co249@dtu.ac.in
import math
class Solution:
    def tripletsBruteForce(self, sums:int) -> int:
        #since a<b<c then we can safely assume that a can be at most
        #a<sum/3 and a<b<s/2
        for i in range(1, (int)(sums / 3)):
            for j in range(i,(int)(sums/2)):
                k=sums-i-j
                if(i*i+j*j==k*k):
                    print("the triplets are")
                    print(i," , ",j," and ",k)
                    return i*j*k
        return -1
    def tripletseffecient(selfself,sums:int)->int:
        #every primitive triplet has terms of the form
        #a =d(m2-n2)
        #b =2d*m*n
        #c =d(m2+n2)
        #where the condition to find m,n and d is
        #a+b+c=2m(m+n)d
        #m <k < 2m
        #k < s/(2m)
        #k is odd and gcd(m,k) = 1.
        l:int=(int)(math.sqrt((int)(sums/2)))
        k=0
        for m in range (2,l+1):
            if (int)(sums/2)%m==0:
                if m%2==0:
                    k=m+1
                else:
                    k=m+2
            while k<2*m and k<=(sums/(2*m)):
                if (sums/(2*m)%k)==0 and math.gcd(k,m)==1:
                    d = sums / 2 / (k * m)
                    n = k - m
                    a= (int)(d * (m * m - n * n))
                    b= (int)(2 * d * n * m)
                    c= (int)(d * (m * m + n * n))
                    print("the triplets are")
                    print(a, " , ", b, " and ", c)
                    return (int)(a*b*c)
                k+=2
        return -1

a=Solution()
print(a.tripletseffecient(1000))
