# N 個の整数 a_0...a_N-1 のうち、整数値 v が何個含まれるかを求める O(N) のアルゴリズムを設計してください。

def count(arr, v):
  result = 0
  for a in arr:
    if a == v:
      result += 1
  return result
