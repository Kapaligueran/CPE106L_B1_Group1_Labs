import statistics
def Average(self):
    return statistics.mean(self)

def Median(self):
    return statistics.median(self)

def Mode(self):
    return statistics.mode(self)

scores=[33, 45, 55, 64, 87, 29, 123];
print(Average(scores));

print(Median(scores));

print(Mode(scores));

