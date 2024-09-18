'''
1071. Greatest Common Divisor of Strings

Problem: 
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
Test cases:
    -Example 1:
        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"
    -Example 2:
        Input: str1 = "ABABAB", str2 = "ABAB"
        Output: "AB"
    -Example 3:
        Input: str1 = "LEET", str2 = "CODE"
        Output: ""
        
Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

'''


def order_list(str1, str2):
        temp_list = []
        loop_count = 0
        while str2 != "":
            if len(str1) <= len(str2):
                temp_list.insert(loop_count, str2[:(len(str1))])
                str2 = str2[(len(str1)):]
                #print(temp_list)
                #print(self.string2)
                loop_count += 1
            else:
                loop_count=0
                temp_list = []
                str2 = str2
                str1 = str1[:-1]
        return temp_list

def get_answer(str1, str2):
    answer = False
    temp_list = order_list(str1, str2)
    while answer == False:
        temp_list = order_list(str1, str2)
        #print(temp_list)
        for i in temp_list:
            if i == str1:
                answer = True
            else:
                answer = False
                str1 = str1[:-1]
                break
    return str1

class Solution(object):
   
    def gcdOfStrings(self, str1, str2):
        self.sum1 = str1 + str2
        self.sum2 = str2 + str1
        self.string1 = str1
        self.string2 = str2
        
        if self.sum1 != self.sum2:
            self.gcd = ""
        elif len(str1) == len(str2) and self.sum1 != self.sum2:
            self.gcd = str1
        elif len(str1) < len(str2):
            self.gcd = get_answer(self.string1, self.string2)
        elif len(str1) > len(str2):
            self.gcd = get_answer(self.string2, self.string1)
        return self.gcd
                    
            
sol = Solution()

print(sol.gcdOfStrings("LEET", "CODE"))


'''result = False
            tempstring = str2[:(len(str1))]
            #print(tempstring)
            loop_count = 0
            while True:
                loop_count += 1
               
                for i in range (round(len(str2) / (len(str1)))):
                    print("Inside for: " + str(i))
                    if tempstring == str1:
                        tempstring = str2.replace(tempstring, '')
                        print(tempstring)
                        result = True
                        print(result)
                    else:
                        tempstring = str2[:(len(str1)) - loop_count]
                        str1 = str1[:-1]
                        result = False
                if result == True:
                    print(str1)
                    break
                
                #print(tempstring)
        return self.gcd'''