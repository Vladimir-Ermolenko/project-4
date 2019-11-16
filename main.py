# The program to solve the typical economic exercises connected with finding the equilibrium positions on the market

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

pe = round((qda - qsc) / (qdb + qsd), 1)
qe = round(qda - qdb * pe, 1)

print('\n', end='')
if pe >= 0 and qe >=0:
    print('При заданных условиях равновесная цена равна', pe, 'а равновесный объём', qe)
elif pe >= 0 and qe < 0:
    print('Ошибка в условиях задачи')
elif pe < 0 and qe >= 0:
    print('Ошибка в условиях задачи')
else:
    print('Ошибка в условиях задачи')