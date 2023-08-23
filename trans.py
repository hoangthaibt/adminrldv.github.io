import os
import shutil
for i in range(2, 21):
    path = "C:/Users/nguye/OneDrive/Desktop/TE/IMG"+str(i)
    ans = []
    for x in os.listdir(path):
        for i in range(len(x)):
            if x[i] == "(":
                temp = ''
                for j in range(i+1, len(x)):
                    if x[j] == ")":
                        ans.append(int(temp))
                        temp = ''
                        break
                    else: temp += x[j]
    ans.sort()
    print(ans)
    for x in ans:
        prev = path + "/rldv(" + str(x) + ").jpg"
        change = path + "/rldv(" + str(int(x)-1) + ").jpg"
        os.rename(prev, change)
    
