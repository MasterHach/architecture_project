import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX


def create_graf(a, b, this_color):
    this_day = datetime.datetime.today().date()
    #a = input("Введите дату начала прогноза (yyyy-mm-dd)\n")
    starting_date = datetime.datetime.strptime(a, '%Y-%m-%d').date()
    #b = input("Введите дату конца прогноза (yyyy-mm-dd)\n")
    ending_date = datetime.datetime.strptime(b, '%Y-%m-%d').date()
    if ending_date < starting_date:
        print('Введите даты нормально')
    if this_day > starting_date:
        print('прогноз на БУДУЩЕЕ! на прошлое сам ищи в ИНТЕРНЕТЕ')
    this_value = (ending_date - starting_date).days + 1
    #this_color = input('Введите цвет графика (red, green, black, yellow, blue)\n')
    train_data = pd.read_csv('./functional_part/bitcoin.csv')

    first = train_data['<CLOSE>'].values
    second = train_data['<DATE>'].values
    train_data['<DATE>'] = pd.to_datetime(train_data['<DATE>'], format='%Y%m%d')
    new_data = pd.DataFrame()

    # обучающая выборка будет включать данные до декабря 1959 года включительно
    train = train_data[:len(train_data) - this_value]['<CLOSE>']

    # тестовая выборка начнется с января 1960 года (по сути, один год)
    test = train_data[len(train_data) - this_value:]['<CLOSE>']

    warnings.simplefilter(action='ignore', category=Warning)

    # обучим модель с соответствующими параметрами, SARIMAX(3, 0, 0)x(0, 1, 0, 12)
    # импортируем класс модели


    # создадим объект этой модели
    model = SARIMAX(train,
                    order=(3, 0, 0),
                    seasonal_order=(0, 1, 0, 12))

    # применим метод fit
    result = model.fit()
    start = len(train_data)

    # и закончится в конце тестового
    end = len(train_data) + this_value

    # применим метод predict
    predictions = result.predict(start, end - 1)

    date_list = [starting_date + datetime.timedelta(days=x) for x in range(this_value)]
    new_data['Date'] = np.array(date_list).tolist()
    new_data['Close'] = np.array(predictions).tolist()

    sns.lineplot(data=new_data, x="Date", y="Close", color=this_color)
    sns.set(style="darkgrid")
    plt.grid()
    plt.savefig('forecast.png')
    #plt.show()

