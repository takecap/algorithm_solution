# 図 1.3 の左側の虫食い算の解を求めてください。
# ２□　×　□□　｜　□３□　□□　｜　□４□

def main():
  for i in range(10):
    val1 = 20 + i
    for j in range(1, 10):
      for k in range(10):
        val2, val3, val4 = j * 10 + k, val1 * k, val1 * j * 10
        if val4 > 999:
          continue
        if (val3 // 10) % 10 == 3 and ((val3 + val4) // 10) % 10 == 4:
          print("{:d} * {:d} = {:d} + {:d} = {:d}".format(val1, val2, val3, val4, val3 + val4))
          return

if __name__ == '__main__':
  main()
