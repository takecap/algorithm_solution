# 問題 4.1 で設計した再帰関数をメモ化によって効率化してください。
# また、メモ化を実施後の計算量を評価してください。

def trib(n, memo):
  if n in memo:
    return memo[n]
  memo[n] = trib(n-1, memo) + trib(n-2, memo) + trib(n-3, memo)
  return memo[n]
