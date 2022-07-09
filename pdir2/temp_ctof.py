temps_c = [0,30,45,67,100]
def zceltofah(list):
    temps_f = []
    for i in list:
        temp_converted = (9*i/5) + 32
        temps_f.append(temp_converted)
    print("original list with celcius temperatures",temps_c)
    print("The list with temparatures in fahrenheit is ",temps_f)
zceltofah(temps_c)


