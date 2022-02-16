n=int(input())
m=int(input())
adjectives=[]
nouns=[]
for i in range(0,n):
    adj=input()
    adjectives.append(adj)
for j in range(0,m):
    noun=input()
    nouns.append(noun)

for i in range(0,n):
    for j in range(0,m):
        print(adjectives[i], "as",nouns[j])