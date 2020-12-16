# N (>=2) 個の相異なる整数 a_0...a_N-1 が与えられます。
# このうち２番目に小さい値を求める O(N) のアルゴリズムを設計してください。

from math import inf

def second(arr):
  num1, num2 = inf, inf
  for a in arr:
    if a < num1:
      num2, num1 = num1, a
    elif a < num2:
      num2 = a
  return num2
