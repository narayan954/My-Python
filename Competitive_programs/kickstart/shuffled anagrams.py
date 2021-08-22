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

"""
Analysis
Test set 1
For this test set, since the length of S ≤8, we can try every permutation of characters and check whether there exists a permutation such that for all i, S[i]≠A[i]. To find every permutation, we can first convert the string to a character array. Then, we swap the first element with every other element and recursively find permutations of the rest of the string.

This can be performed in O(N!), where N is the length of S.

Test set 2
For this test set, the above solution would exceed the time limits.

The key observation here is that if a character exists more than ⌊N2⌋ times, then it's impossible to find such a permutation, because at least one position will have a letter that stays the same. Otherwise, we can sort the letters and keep track of the initial position of each letter.

Let the new sorted letters be P. We can split the sorted letters into two halves, from index 0 to N2, P[0:N2], and from N2 to the end, P[N2:]. If N is odd, split P such that the second half has an extra letter, where the first half is 0 to ⌊N2⌋ and the second half is from ⌈N2⌉ to the end. Then, we put each character from the second half of the sorted letters P[i+(N2)] into the original position of the corresponding letter in the first half P[i]. Similarly, we put each character from the first half of the sorted letters P[i] into the original position of the corresponding letter in the second half P[i+(N2)]. Note that if N is odd, the second half of the sorted letters P[i+(N2)] will occupy the first ⌊N2⌋+1 spaces, while the original first half will occupy the last ⌊N2⌋ spaces, as shown in the example below. The letter orginally at P[N−1] will be in the middle of the array after the swap, replacing P[i+⌊N2⌋].


Example solution.

![image](https://user-images.githubusercontent.com/77617189/130346794-532d675d-abd0-4abe-a1ff-0fb3623989c4.png)

This works because we know that no more than half the characters are equal, and hence the character at P[i] cannot be equal to the letter at P[i+(N2)].

This can be performed in O(NlogN), due to sorting. However, due to the limited size of the alphabet, we can actually sort even faster using a non-comparative sorting algorithm such as counting sort.
"""
