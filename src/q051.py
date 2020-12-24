# N 日間の夏休みがあり、i 日目に海で泳ぐ幸福度は a_i、虫取りする幸福度は b_i、宿題をする幸福度は c_i で与えられるとします。
# それぞれの日について、これらの３つの行動のうちのいずれかを行います。ただし２日連続で同じ行動はしないものとします。
# N 日間の幸福度の最大値を O(N) で求めるアルゴリズムを設計してください。
# (AtCoder Educational DP Contest C - Vacation)

k = int(input())
happy = []
for _ in range(k):
  happy.append(list(map(int, input().split())))

values = [[0, 0, 0] for _ in range(k)]
values[0] = happy[0]
for j in range(1, k):
  h = happy[j]
  pre = values[j-1]
  for i in range(3):
    v1 = pre[(i+1) % 3] + h[i]
    v2 = pre[(i+2) % 3] + h[i]
    values[j][i] = max(v1, v2)

print(max(values[-1]))
