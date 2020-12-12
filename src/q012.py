# 年齢あてゲームで、Aさんの年齢が「０歳以上１００歳未満」の１００通り考えられるとします。
# それを「Yes / Noで答えられる質問を繰り返すことで当てたいとします。
# ６回の質問で確実に当てることは可能でしょうか。また７回の質問で確実に当てることは可能でしょうか。

from sys import argv

age_low, age_high = 0, 100

def reply(age, times):
  answer = ''
  low, high = age_low, age_high
  mid = (low + high) // 2
  if age < 0 or 100 <= age:
    return low, high, answer
  for _ in range(times):
    answer += 'under {:d}? '.format(mid)
    if age < mid:
      high = mid
      answer += 'Yes -> '
    else:
      low = mid
      answer += 'No  -> '
    mid = (low + high) // 2
#  print("{:d} <= AGE < {:d}".format(low, high))
  return low, high, answer

def judge(age, times=6):
  low, high, text = reply(age, times)
  if low + 1 == high:
    print(text + 'Age: {:d}!'.format(low))
  else:
    print(text + '{:d} <= Age < {:d}'.format(low, high))

def main():
  if len(argv) == 1:
    age, times = 20, 6
  elif len(argv) == 2:
    age, times = int(argv[1]), 6
  else:
    age, times = int(argv[1]), int(argv[2])
  print("Age: {:d}, Times: {:d}".format(age, times))
  judge(age, times)

if __name__ == '__main__':
  main()
