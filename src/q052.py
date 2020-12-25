# N 個の正の整数 a_0,a_1,...,a_N-1 からいくつか選んで総和を所望の整数 W に一致させることができるかどうかを
# 判定する問題を O(N) で解くアルゴリズムを設計してください。（部分和問題 3.5節、4.5節）

def search(arr, w):
  results = [True] + [False] * w
  for n in arr:
    temp = [b for b in results]
    for i in range(n, w+1):
      if temp[i-n]:
        results[i] = True
  return results

def main():
  arr = (3, 2, 6, 5)
  w = 14
  print("Search {:d} in".format(w), arr)
  results = search(arr, w)
  print("Answer", results[w])

if __name__ == '__main__':
  main()
