class stock:
    def __init__(self, name, code, PER, PBR, DevidendRate):
        self.name = name
        self.code = code
        self.PER = float(PER)
        self.PBR = float(PBR)
        self.DevidendRate = float(DevidendRate)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_PER(self, PER):
        self.PER = PER

    def set_PBR(self, PBR):
        self.PBR = PBR

    def set_DevidendRate(self, DR):
        self.DevidendRate = DR

    def get_name(self):
        return (self.name)

    def get_code(self):
        return (self.code)

    def get_rest(self):
        return (self.PER, self.PBR, self.DevidendRate)


stock_list= []
SS = stock("Samsung", "005930", 15.79, 1.33, 2.83)
HD = stock("Hyundai", "005380", 8.7, 0.35, 4.27)
LG = stock("LG", "066570", 317.34, 0.69, 1.37)

samsung = 50000
stock = 10
print(samsung * stock)

stock_list.append(SS)
stock_list.append(HD)
stock_list.append(LG)
for i in stock_list:
    print (f"Code: {i.name}\t PER: {i.PER}")



