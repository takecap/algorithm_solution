# 各桁の値が１以上９以下の数値のみである整数とみなせるような、長さ N の文字列 S が与えられます。
# この文字列の中で、文字と文字の間のうちのいくつかの場所に '+' を入れることができます。
# １つも入れなくても構いませんが、'+' が連続してはいけません。このようにしてできるすべての文字列を
# 数値とみなして、総和を計算する O(N^2) のアルゴリズムを設計してください。
# (AtCoder Beginner Contest 045 C - たくさんの数式)

def search(list1, idx):
  list2 = []
  for formula in list1:
    cnt = formula.count('+')
    list2.append(formula[:(idx + cnt)] + '+' + formula[(idx + cnt):])
  return list2

def count(numstr):
  strs = [numstr]
  for i in range(1, len(numstr)):
    strs += search(strs, i)
  sum = 0
  for s in strs:
    sum += eval(s)
  return sum
