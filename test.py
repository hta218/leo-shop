import locale
locale.setlocale( locale.LC_ALL, '' )

def formatMoney(money):
  return locale \
          .currency(money, grouping=True) \
          .replace('$', '') \
          .replace('.00', 'đ') \
          .replace(',', '.') \

print(type(formatMoney(100000000)))