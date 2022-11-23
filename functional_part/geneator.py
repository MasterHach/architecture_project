import datetime
import re
from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
import os
from matplotlib import rcParams


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
    #train_data = pd.read_csv('bitcoin.csv')
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
    ax = sns.lineplot(data=new_data, x="Date", y="Close", color=this_color)
    rcParams['figure.figsize'] = 11.7, 10
    sns.set_style("darkgrid", {
        "ytick.major.size": 0.1,
        "ytick.minor.size": 0.05,
        'grid.linestyle': '--'
    })
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)

    # plt.grid(True)
    # plt.rcParams['figure.figsize'] = (14, 7)
    # plt.rcParams['font.size'] = '10'
    # plt.subplots_adjust(wspace=0, hspace=0)
    # plt.gca().xaxis.set_major_locator(MaxNLocator(prune='lower'))
    #plt.show()
    #lolkek = ''
    #mass = os.listdir(path='G:/Games/architecture_project/functional_part')
    # mass = os.listdir(path='./media')
    # for x in mass:
    #     if x.startswith('forecast'):
    #         lolkek = re.findall(r'\d+', x, flags=re.ASCII)
    # if not lolkek:
    #     plt.savefig('./media/forecast1.png', dpi=1000)
    #     return 'forecast1.png'
    # else:
    #     my_number = int(lolkek[0]) + 1
    #     plt.savefig(f'./media/forecast{my_number}.png', dpi=1000)
    #     return f'forecast{my_number}.png'
    plt.savefig(f'./media/forecast.png', dpi=1000)
    plt.clf()
    return 'forecast.png'


# create_graf('2022-11-20', '2022-12-25', 'red')
