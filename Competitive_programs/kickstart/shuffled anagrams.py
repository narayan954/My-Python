"""
Google Kickstart Problem
Let S be a string containing only letters of the English alphabet. An anagram of S is any string that contains exactly the same letters as S (with the same number of occurrences for each letter), but in a different order. For example, the word kick has anagrams such as kcik and ckki.
Now, let S[i] be the i-th letter in S. We say that an anagram of S, A, is shuffled if and only if for all i, S[i]≠A[i]. So, for instance, kcik is not a shuffled anagram of kick as the first and fourth letters of both of them are the same. However, ckki would be considered a shuffled anagram of kick, as would ikkc.
Given an arbitrary string S, your task is to output any one shuffled anagram of S, or else print IMPOSSIBLE if this cannot be done.
Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line, a string of English letters.
Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a shuffled anagram of the string for that test case, or IMPOSSIBLE if no shuffled anagram exists for that string.
Limits
Memory limit: 1 GB.
1≤T≤100.
All input letters are lowercase English letters.
Test Set 1
Time limit: 20 seconds.
1≤ the length of S ≤8.
Test Set 2
Time limit: 40 seconds.
1≤ the length of S ≤104.
Sample
Sample Input
save_alt
content_copy
2
start
jjj
Sample Output
save_alt
content_copy
Case #1: tarts
Case #2: IMPOSSIBLE
In test case #1, tarts is a shuffled anagram of start as none of the letters in each position of both strings match the other. Another possible solution is trsta (though you only need to provide one solution). However, in test case #2, there is no way of anagramming jjj to form a shuffled anagram, so IMPOSSIBLE is printed instead.
"""

import random
import math

for j in range(1, int(input()) + 1):
    s = input().strip()

    for i in range(math.factorial(len(s))):
        temp = list(s)
        random.shuffle(temp)
        temp = ''.join(temp)
        flag = 1
        for i in range(len(s)):
            if s[i] == temp[i]:
                flag = 0
        if flag:
            print(f'Case #{j}: {temp}')
            break
    if not flag:
        print(f'Case #{j}: IMPOSSIBLE')
