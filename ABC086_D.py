from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="086"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc089_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,K=map(int,input().split())
  white=[[0]*K for _ in range(K)]
  black=[[0]*K for _ in range(K)]
  ans=0
  for i in range(N):
    p=input().split()
    x,y=map(int,p[:2])
    c=p[2]
    if (x//K+y//K)%2==1:
      if c=='B': c='W'
      else: c='B'
    if c=='B': black[x%K][y%K]+=1
    else: white[x%K][y%K]+=1
  awhite=[[0]*K for _ in range(K)]
  ablack=[[0]*K for _ in range(K)]
  for i in range(K):
    for j in range(K):
      tmpb=black[i][j]
      tmpw=white[i][j]
      if i>0:
        tmpb+=ablack[i-1][j]
        tmpw+=awhite[i-1][j]
      if j>0:
        tmpb+=ablack[i][j-1]
        tmpw+=awhite[i][j-1]
      if i>0 and j>0:
        tmpb-=ablack[i-1][j-1]
        tmpw-=awhite[i-1][j-1]
      ablack[i][j]=tmpb
      awhite[i][j]=tmpw
  for i in range(K):
    for j in range(K):
      tmp=ablack[-1][-1]-ablack[i][-1]-ablack[-1][j]+2*ablack[i][j]+awhite[i][-1]+awhite[-1][j]-2*awhite[i][j]
      ans=max(ans, tmp)
      tmp=awhite[-1][-1]-awhite[i][-1]-awhite[-1][j]+2*awhite[i][j]+ablack[i][-1]+ablack[-1][j]-2*ablack[i][j]
      ans=max(ans, tmp)
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])