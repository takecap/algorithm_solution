# N 個の正の整数 a_0,a_1,...,a_N-1 と正の整数 W が与えられます。
# a_0,a_1,...,a_N-1 から何個かの整数を選んで総和を W とすることができるかどうかを判定してください。

def search_dp(arr, w, memo):
  if len(arr) > 1:
    search_dp(arr[:-1], w, memo)
  m = arr[-1]
  temp = [b for b in memo]
  for n in range(1, w+1):
    if n - m >= 0 and temp[n - m]:
      memo[n] = True

def main():
  arr = (3, 2, 6, 5)
  w = 14
  memo = [True] + [False] * w
  print("Search {:d} in".format(w), arr)
  search_dp(arr, w, memo)
  print("Answer", memo[w])

if __name__ == '__main__':
  main()

def search_org(arr, w):
  if len(arr) == 0:
    return (w == 0)
  
  if search_org(arr[:-1], w):
    return True
  if search_org(arr[:-1], w - arr[-1]):
    return True
  return False

def search(arr):
  if len(arr) == 0:
    return { 0 }
  results = set()
  temp = search(arr[:-1])
  results |= temp
  results |= set( n + arr[-1] for n in temp )
  return results
