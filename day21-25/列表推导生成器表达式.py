# 列表推导
symbols = 'ABCDEFG'
codes = [ord(symbol) for symbol in symbols ]
print(codes)
print(symbols)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 67]
print(beyond_ascii)
# 利用filter和map
beyond_ascii = list(filter(lambda c: c > 67, map(ord, symbols)))
print(beyond_ascii)
# 笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# 生成器表达式
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' %(c,s) for c in colors for s in sizes):
    print(tshirt)
# 生成器表达式会逐个产生元素,节省内存空间

# 元祖的记录功能
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('NewYork', 2020, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for country, _ in traveler_ids:
    print(country)
# 元祖拆包
lat, long = lax_coordinates
print(lat, long)
# 利用*处理剩下元素
a, b, *rest = range(5)
print(*rest)
