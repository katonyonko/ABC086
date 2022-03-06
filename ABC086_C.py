from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="086"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc089_a".format(times, problem)) as res:
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
  N=int(input())
  ans='Yes'
  nowx=0
  nowy=0
  now=0
  for i in range(N):
    t,x,y=map(int,input().split())
    if (t-now>=abs(x-nowx)+abs(y-nowy) and (t-now-abs(x-nowx)-abs(y-nowy))%2==0)==False:
      ans='No'
    nowx,nowy,now=x,y,t
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])