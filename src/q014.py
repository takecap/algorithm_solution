# 図 1.3 の右側の虫食い算の解を求めてください。
#     □□□□□□ val1
# *     □□□□ val2
#     66□□□□ val3
#    6□□□□□  val4
#  □□666□□   val5
#  □□6□□6    val6
# □□□□66□□□□ val7

def check5(val):
  text = str(val)
  return len(text) == 9 and text[2:5] == '666'

def check6(val):
  text = str(val)
  return len(text) == 9 and text[2] == '6' and text[5] == '6'

def check7(val):
  text = str(val)
  return len(text) == 10 and text[4:6] == '66'

def search(base):
  results = []
  if not base in {1, 2, 3, 4, 5, 6}:
    return results
  top = 66 // base
  for i1 in range(10):
    for i2 in range(10):
      for i3 in range(10):
        for i4 in range(10):
          for j3 in range(10):
            for j4 in range(1, 10):
              val1 = int("{:d}{:d}{:d}{:d}{:d}".format(top, i4, i3, i2, i1))
              val2 = int("{:d}{:d}{:d}{:d}".format(j4, j3, base, base))
              val3 = val1 * base
              val4 = val1 * base * 10
              val5 = val1 * j3 * 100
              val6 = val1 * j4 * 1000
              val7 = val3 + val4 + val5 + val6
              if check5(val5) and check6(val6) and check7(val7):
                results.append((val1, val2, val3, val4, val5, val6))
  return results

def disp(values):
  print("{:d} * {:d} = {:d}".format(values[0], values[1], values[0] * values[1]))
  print("{:d} + {:d} + {:d} + {:d}".format(values[2], values[3], values[4], values[5]))

def main():
  results = []
  for i in range(1, 7):
    print("Search for [{:d}]".format(i))
    results = search(i)
    print("count: {:d}".format(len(results)))
    for res in results:
      disp(res)
    print("")

if __name__ == '__main__':
  main()
