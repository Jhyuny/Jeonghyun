import sys

def input():
  return sys.stdin.readline().rstrip()

dic = {}
N = int(input())
M = int(input())

for i in range(N):
    poketmon = input()
    dic[i] = poketmon

for i in range(M):
    Question = input()
    if int(Question) <= N:
        print(dic[i])
    else:
        for i in range(N):
            Question == dic[i]
            print(i)
