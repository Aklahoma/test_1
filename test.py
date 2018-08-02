btc = int(input('Введите цену биткоина: '))
mybtc = btc * 0.016877
usd = 24.64
cash = (mybtc * usd) - 5000
a = mybtc * usd
b = cash/usd
print("Общая сумма продажи: ",round(a, 2), "UAH")
print("Минус вложения: ", round(cash,2),"UAH")
print("В валюте", round(b,2), 'USD')
