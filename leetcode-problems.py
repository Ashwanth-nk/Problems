
'''
# 3093. Longest Common Suffix (Hard)
# 800+ Testcases ran
# Error: Time Limit Executed
wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
ans = []
for i in wordsQuery:
    x = []
    for j in wordsContainer:
        a = 0
        c = min(len(i) - 1, len(j) - 1)
        m, n = len(i) - 1, len(j) - 1
        while c > -1:
            if j[n] == i[m]:
                a += 1
                c -= 1
                m -= 1
                n -= 1
            else:
                break
        if a > 0:
            if x == []:
                x.append([j, a])
            else:
                if a > x[0][1]:
                    x = [[j, a]]
                elif a == x[0][1] and len(j) < len(x[0][0]):
                    x = [[j, a]]
    if x != []:
        ans.append(wordsContainer.index(x[0][0]))
    else:
        ans.append(wordsContainer.index(sorted(wordsContainer, key=len)[0]))

print(ans)
'''