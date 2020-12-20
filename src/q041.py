# トリボナッチ数列とは、 T_0 = 0, T_1 = 0, T_2 = 1, T_N = T_N-1 + T_N-2 + T_N-3 (N=3,4,...)
# によって定義される数列です。トリボナッチ数列の第 N 項の値を求める再帰関数を設計してください。

def trib(n):
  if n < 2:
    return 0
  elif n == 2:
    return 1
  return trib(n-1) + trib(n-2) + trib(n-3)
