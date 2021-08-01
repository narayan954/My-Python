class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letter_set = set(words[0])
        for i in range(len(words)):
            letter_set.intersection_update(set(words[i]))
        letter_count = []
        for i in letter_set:
            temp_count = []
            for j in range(len(words)):
                x = words[j].count(i)
                temp_count.append(x)
            temp_count.sort()
            letter_count.append(temp_count[0])
        answer = []
        letter_set = list(letter_set)
        for i in range(len(letter_set)):
            for j in range(letter_count[i]):
                answer.append(letter_set[i])
        return answer
