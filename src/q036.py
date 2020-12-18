# ２つの整数 K, N が与えられます。 0 <= x, y, z <= K を満たす整数 (x, y, z) の組であって
# x + y + z = N を満たすものが何通りあるかを求める O(N^2) のアルゴリズムを設計してください。

def count(k, n):
  results = 0
  for x in range(0, k+1):
    if n - x > 2 * k:
      continue
    for y in range(0, k+1):
      z = n - x - y
      if 0 <= z <= k:
        results += 1
  return results

def count2(k, n):
  results = []
  for x in range(0, k+1):
    if n - x > 2 * k:
      continue
    for y in range(0, k+1):
      z = n - x - y
      if 0 <= z <= k:
        results.append((x, y, z))
  return results
