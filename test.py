btc = int(input('Введите цену биткоина: '))
your_btc = float(input('Введите количество Ваше биткоинов: '))
my_btc = btc * your_btc
usd = 24.64
price_sale_btc = my_btc * usd
price_inUSD = price_sale_btc / usd
print("Общая сумма продажи: ",round(price_sale_btc, 2), "UAH")
print("В валюте", round(price_inUSD,2), 'USD')
