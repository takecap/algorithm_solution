# 年齢あてゲームで、Aさんの年齢が２０歳以上３６歳未満のそれぞれの場合について、
# 二分探索法によって年齢を当てるまでの流れを求めてください。

age_low, age_high = 20, 36

def reply(age):
  answer = ''
  low, high= age_low, age_high
  mid = (low + high) // 2
  while high - low > 2:
    answer += 'under {:d}? '.format(mid)
    if age < mid:
      high = mid
      answer += 'Yes -> '
    else:
      low = mid
      answer += 'No  -> '
    mid = (low + high) // 2
  
  answer += 'under {:d}? '.format(mid)
  if age < mid:
    answer += 'Yes -> Age: {:d}!'.format(low)
  else:
    answer += 'No  -> Age: {:d}!'.format(high-1)
  return answer

def main():
  for age in range(age_low, age_high):
    print(reply(age))

if __name__ == '__main__':
  main()
