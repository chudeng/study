'''
with open('./매수종목1.txt', mode='w', encoding='utf-8', newline="") as stock:
    stock.write('005930\n')
    stock.write('005380\n')
    stock.write('035420')

with open('./매수종목2.txt', mode='w', encoding='utf-8', newline="") as stock:
    stock.write('005930 삼성전자\n')
    stock.write('005380 현대차\n')
    stock.write('035420 NAVER')

with open('./매수종목1.txt', mode='r', encoding='utf-8') as stock:
    stock_code = []
    lines = stock.readlines()
    for line in lines:
        code = line.strip()
        stock_code.append(code)
    print(stock_code)

with open('./매수종목2.txt', mode='r', encoding='utf-8') as stock:
    stock_info = {}
    lines = stock.readlines()
    for line in lines:
        code = line.strip()
        keys, values = code.split(" ")
        stock_info[keys] = values
    print(stock_info)

per = ['10.31', '', '8.00']
new_per = []
for i in per:
    try:
        i = float(i)
        print(i)
    except:
        i = 0
        print(i)
    new_per.append(i)
print(new_per, type(new_per))


data = [1,2,3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as message:
        print(message)

'''
per = ['10.31', '', '8.00']

for i in per:
    try:
        print(float(i))
    except:
        print('예외발생')
    else:
        print('예외없음')
    finally:
        print('처리완료~')