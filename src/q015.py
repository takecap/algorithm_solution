# 図 1.6 の迷路で右下（ゴール）の数値がわかっている状態から、実際にSのマスからGのマスまで至る
# 最短経路を復元する方法について論じてください。

maze = [
  [100] * 10,
  [100,  -1, 100,  -1,  -1,  -1,  -1, 100,  16, 100],
  [100,  -1, 100,  -1, 100,  -1,  -1,  -1,  -1, 100],
  [100,  -1,  -1,  -1, 100,  -1, 100, 100,  -1, 100],
  [100, 100,  -1, 100, 100,  -1,  -1,  -1, 100, 100],
  [100,  -1,  -1,  -1, 100, 100, 100,  -1, 100, 100],
  [100,  -1, 100,  -1,  -1,  -1,  -1,  -1, 100, 100],
  [100,  -1,  -1,  -1, 100,  -1, 100,  -1,  -1, 100],
  [100,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1, 100],
  [100] * 10
]

def step(fwds, cnt, mz):
  news = set()
  for (x, y) in fwds:
    if mz[x+1][y] < cnt:
      mz[x+1][y] = cnt
      news.add((x+1, y))
    if mz[x-1][y] < cnt:
      mz[x-1][y] = cnt
      news.add((x-1, y))
    if mz[x][y+1] < cnt:
      mz[x][y+1] = cnt
      news.add((x, y+1))
    if mz[x][y-1] < cnt:
      mz[x][y-1] = cnt
      news.add((x, y-1))
  return news

def disp(mz):
  for row in mz:
    text = ''
    for n in row:
      if n < 100:
        text += ' {:2d}'.format(n)
      else:
        text += ' **'
    print(text)

def main():
  fwds = {(1, 8)}
  for cnt in range(15, -1, -1):
    fwds = step(fwds, cnt, maze)
  disp(maze)

if __name__ == '__main__':
  main()
