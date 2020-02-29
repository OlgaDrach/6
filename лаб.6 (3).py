#За s-назвою місяця визначити відповідну пору року.(Драч Ольга 122_Д)

while True:
    while True:
            try:
                s = int(input('month:'))
                break
            except:
                print('Тільки числа')
    while s < 0 or s > 13:
        s = int(input('Введіть введіть вірний номер місяця!'))
        class mounth(Enum):
            January = 1
            February = 2
            March = 3
            April = 4
            May = 5
            June = 6
            July = 7
            August = 8
            September = 9
            October = 10
            November = 11
            December = 12
        class season(Enum):
            Winter = 1
            Spring = 2
            Summer = 3
            Autumn = 4
    if s == mounth.January.value or s == mounth.February.value or s == mounth.December.value:
        print(season.Winter.name)
    elif s == mounth.March.value or s == mounth.April.value or s == mounth.May.value:
        print(season.Spring.name)
    elif s == mounth.June.value or s == mounth.July.value or s == mounth.August.value:
        print(season.Summer.name)
    elif s == mounth.September.value or s == mounth.October.value or s == mounth.November.value:
        print(season.Autumn.name)
    result = input('Хочете ще раз ввести місяць? Якщо так натисніть 1, а якщо ні будь яку іншу кнопку')
    if result == '1':
        continue
    else:
          break
