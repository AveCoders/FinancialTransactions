# FinancialTransactions
This is a supplementary to my YouTube video on Financial Transactions Tech task

The task itself:

Data
The data provided is stored within transactions.txt and consists of 991 transactions presented in a comma separated format and spread over a month. The transactions are for multiple accounts and there are multiple types of transaction. The file has the following columns:

transactionId: String representing the id of a transaction
accountId: String representing the id of the account which made the transaction transaction
day: Integer representing the day the transaction was made on (time information was removed)
category: String representing the type of category of the transaction
transactionAmount: Double representing the value of the transaction
Output
Q1 output calculates the total transaction value for all transactions performed each day over the month. The output contains one line for each day and each line includes the day and the total value. Q2 output calculates the average value of transactions per account for each type of transaction (there are seven in total). The output presents one line per account and per category (transaction type). Each line includes the account id and the average value of the transaction type. Q3 output For each day, each account has transaction statistics calculated for five days prior (not including transactions from the day itself). The output has one line per day per account id and each line has each of the calculated statistics. The statistics are: The maximum transaction value in the previous 5 days of transactions per account The average transaction value of the previous 5 days of transactions per account The total transaction value of transactions types “AA”, “CC” and “FF” in the previous 5 days per account IMPORTANT: for Q3, the method expects the day from which you want to calculate your stats from and the size of the window.

Данные:
Файл transactions.txt хранит 991-у транзакцию, представленные в формате с разделителями-запятыми и распределенные по месяцам. Транзакции проводятся по нескольким счетам и имеют несколько типов. Файл содержит следующие столбцы:

transactionId: Строка, представляющая собой идентификатор транзакции
accountId: Строка, представляющая собой идентификатор счета, с которого была произведена транзакция
Day: Целое число, представляющее собвственно день, в который была совершена операция
category: Строка, представляющая тип категории транзакции
transactionAmount: Число, представляющее стоимость транзакции или номинально - сколько денюжек учавствовало в переводе

Выводы:
В выводе Q1 вычисляется суммарное значение транзакций для всех транзакций, совершенных за день в течение месяца. Вывод содержит одну строку для каждого дня, в каждой строке указывается день и общая стоимость. 
В выводе Q2 рассчитывается средняя стоимость транзакций по счету для каждого типа транзакций (всего их семь). В выводе представлено по одной строке на счет и на категорию (тип транзакции). Каждая строка содержит идентификатор счета и среднее значение по типу транзакции. 
Вывод Q3: Для каждого дня по каждому счету выводится статистика транзакций, рассчитанная за пять дней до этого (без учета транзакций за сам день). Вывод содержит одну строку в день для каждого идентификатора счета, в каждой строке - каждая из рассчитанных статистик. 
Статистикой являются: 
Максимальное значение транзакции за предыдущие 5 дней по счету 
Среднее значение транзакции за предыдущие 5 дней по счету 
Общее значение транзакций типов "AA", "CC" и "FF" за предыдущие 5 дней по счету ВАЖНО отметить: для Q3 в методе указывается день, с которого необходимо вычислить статистику, и размер окна (т.н. “Скользящее окно”).
