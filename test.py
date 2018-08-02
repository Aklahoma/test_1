btc = int(input('Введите цену биткоина: '))
mybtc = btc * 0.016877
usd = 26.09
cash = (mybtc * usd) - 6484.16
a = mybtc * usd
b = cash/usd
print("Общая сумма продажи: ",round(a, 2), "UAH")
print("Минус вложения: ", round(cash,2),"UAH")
print("В валюте", round(b,2), 'USD')