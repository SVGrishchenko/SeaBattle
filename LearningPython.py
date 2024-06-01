Weight = input('Твоя вага?')
Years = 0
for x in range(1,16):
    Weight = int(Weight) + 1
    WeightMoon = Weight*0.165
    Years = Years + 1
    print( str(Years) + " Твоя вага на Місяці: " + str(WeightMoon))