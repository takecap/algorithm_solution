# N 個の正の整数 a_0,a_1,...,a_N-1 と正の整数 W が与えられます。N 個の整数から k 個以下の整数を選んで
# 総和を W に一致させることができるかどうかを O(NW) で判定するアルゴリズムを設計してください。

def search(arr, w, k):
  results = [0] + [k+1] * w
  for n in arr:
    temp = [n for n in results]
    for i in range(n, w+1):
      if temp[i-n] < k and temp[i-n] + 1 < results[i]:
        results[i] = temp[i-n] + 1
  return results

def main():
  arr = (3, 2, 6, 5)
  w = 14
  k = 3
  print("Search {:d} in ".format(w), arr, " within {:d} terms".format(k))
  results = search(arr, w, k)
  print("Answer", results[w] <= k)
  k = 2
  print()
  print("Search {:d} in ".format(w), arr, " within {:d} terms".format(k))
  results = search(arr, w, k)
  print("Answer", results[w] <= k)

if __name__ == '__main__':
  main()
