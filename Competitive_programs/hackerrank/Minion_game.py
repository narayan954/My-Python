def minion_game(s):
    st, ke = 0, 0
    for i in range(len(s)):
        if s[i] not in 'AEIOU':
            st += len(s)-i
        else:
            ke += len(s)-i
    if ke>st:
        print('Kevin',ke)
    elif st>ke:
        print('Stuart',st)
    else:
        print('Draw')
            

if __name__ == '__main__':
    s = input()
    minion_game(s)
