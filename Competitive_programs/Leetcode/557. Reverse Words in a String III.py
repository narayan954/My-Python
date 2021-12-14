class Solution:
    def reverseWords(self, s: str) -> str:
        string = ''
        s = s.split()
        for i in range(len(s)-1):
            string += s[i][::-1] + " "
        string += s[-1][::-1]
        return string
    '''
    def reverseWords(self, s):
    return ' '.join(x[::-1] for x in s.split())
    '''
    '''
    def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]
    '''
    
