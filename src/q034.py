# N 個の整数 a_0...a_N-1 が与えられます。
# この中から２つ選んで差を取ります。その差の最大値を求める O(N) のアルゴリズムを設計してください。

from math import inf

def max_diff(arr):
  mi, ma = inf, -inf
  for n in arr:
    if n < mi:
      mi = n
    if n > ma:
      ma = n
  return ma - mi
