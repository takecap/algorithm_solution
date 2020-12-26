# N 個の正の整数 a_0,a_1,...,a_N-1 と正の整数 W が与えられます。この中からいくつか選んで総和を取って得られる
# 1 以上 W 以下の整数が何通りあるかを O(NW) で求めるアルゴリズムを設計してください。
# (AtCoder Typical DP Contest A - コンテスト)

def search(arr, w):
  results = [True] + [False] * w
  for n in arr:
    temp = [b for b in results]
    for i in range(n, w+1):
      if temp[i-n]:
        results[i] = True
  return results

n = int(input())
arr = list(map(int, input().split()))

results = search(arr, sum(arr))
print(sum(results))
