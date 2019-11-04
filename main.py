# The program to solve the typical economic exercises connected with finding the equilibrium positions on the market

import math

print('Эта программа поможет Вам в решении простейших экономических задач, в которых даны функции покупателя и '
      'и продавца и нужно найти равновесную цену и объём')

qd = input('Введите линейную функцию спроса в формате a - bP : ')
qs = input('Введите линейную функцию предложения в формате c + dP : ')
qdf = qd.replace(' ', '')
qsf = qs.replace(' ', '')
qdms = qdf.find('-')
qsms = qsf.find('-')

while qdms == 0 or qsms == 0:
      print('Ошибка, введите данные повторно')
      qd = input('Введите линейную функцию спроса в формате a - bP : ')
      qs = input('Введите линейную функцию предложения в формате c + dP : ')
      qdf = qd.replace(' ', '')
      qsf = qs.replace(' ', '')
      qdms = qdf.find('-')
      qsms = qsf.find('-')


lnqdf = len(qdf)
lnqsf = len(qsf)
qsps = qsf.find('+')

qda = int(qdf[0:qdms])
if qdf[qdms + 1:lnqdf] == 'p':
      qdb = 1
else:
      qdb = int(qdf[qdms + 1:lnqdf - 1])

qsc = int(qsf[0:qsps])
if qsf[qsps + 1:lnqsf] == 'p':
      qsd = 1
else:
      qsd = int(qsf[qsps + 1:lnqsf - 1])

pe = math.ceil(qda - qsc)/(qdb + qsd)
qe = qda - qdb * pe

print('\n', end='')
print('При заданных условиях равновесная цена равна', pe, 'а равновесный объём', qe)