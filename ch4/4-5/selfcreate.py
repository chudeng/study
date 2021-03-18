import random
import bisect
import collections

# 당뇨병 진단기준
# fbs: 공복혈당, ogt: 경구포도당부하 2시간 후 혈당
def calc_bmi(fbs, ogt):
    if fbs < 100 and ogt < 140: return '정상'
    elif 100 <= fbs <= 125 or 140 <= ogt <= 200: return '주의'
    elif 125 < fbs <= 350 or 200 < ogt <= 350: return '당뇨'

def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0
    for i in weights:
        cumsum += i
        result.append(cumsum/total)
    return result

def choice(bsrate, weights):
    assert len(bsrate) == len(weights)
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return bsrate[idx]

# 출력 파일 준비하기
fp = open('glucose.csv', 'w', encoding='utf-8')
fp.write('공복혈당,경구포도당부하 2시간 후 혈당,현재상태\r\n')
# 상태 가중치 주기
weights = [0.65, 0.2, 0.15]
bsrate = ['정상', '주의', '당뇨']
cnt = {'정상': 0, '주의': 0, '당뇨': 0}
counts = collections.defaultdict(int)
# 가중치에 따라 무작위 데이터 생성하기
for i in range(200):
    if choice(bsrate, weights) == '정상':
        fbs = random.randint(70, 99)
        ogt = random.randint(70, 139)
        label = calc_bmi(fbs, ogt)
        cnt[label] += 1
        fp.write('{0},{1},{2}\r\n'.format(fbs, ogt, label))
    elif choice(bsrate, weights) == '주의':
        fbs = random.randint(100, 125)
        ogt = random.randint(140, 200)
        label = calc_bmi(fbs, ogt)
        cnt[label] += 1
        fp.write('{0},{1},{2}\r\n'.format(fbs, ogt, label))
    elif choice(bsrate, weights) == '당뇨':
        fbs = random.randint(126, 350)
        ogt = random.randint(201, 350)
        label = calc_bmi(fbs, ogt)
        cnt[label] += 1
        fp.write('{0},{1},{2}\r\n'.format(fbs, ogt, label))
    counts[choice(bsrate, weights)] += 1
    print(counts, cnt)
fp.close()
print('source rate', counts)
print('normalized rate', cnt)
