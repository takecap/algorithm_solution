# N 個の整数 a_0...a_N-1 が与えられます。これらに対して「 N 個の整数がすべて偶数ならば２で割った値に置き換える」
# という操作を、操作が行えなくなるまで繰り返します。何回の操作を行うことになるかを求めるアルゴリズムを設計してください。

def count2(num):
  d = 0
  while True:
    mask = 1 << d
    if num & mask == mask:
      return d
    d += 1

def count(arr):
  counts = [count2(n) for n in arr]
  return min(counts)
