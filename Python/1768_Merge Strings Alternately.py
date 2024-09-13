class Solution(object):
    def mergeAlternately(word1, word2):
        max_char=max(len(word1), len(word2))
        word3 = ""
        for x in range (max_char):
            if x < len(word1):
                word3 += word1[x]
            if x < len(word2):
                word3 += word2[x]
        return word3  
    print(mergeAlternately("a", "pq"))
    

