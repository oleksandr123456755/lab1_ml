import pandas as pd
import matplotlib.pyplot as plt
k=19
print('1. Відкрити та зчитати файл з даними.')
data = pd.read_csv('Vehicle_Sales.csv')

print('2. Визначити та вивести кількість записів та кількість полів у кожному записі.')
data_size = data.shape
print(f'К-сть записів: {data_size[0]}. К-сть полів: {data_size[1]}')

print('3. Вивести k+7 перших записів.')
print(data.iloc[:k+7])
print('3. Вивести 5К-3 останніх записів.')
print(data.tail(5*k-3))

print('4. Визначити та вивести тип полів кожного запису.')
print(data.dtypes)

data['Total Sales New']=data['Total Sales New'].str[1:].astype(int)
data['Total Sales Used']=data['Total Sales Used'].str[1:].astype(int)
print("Покажемо, що типи останніх двох полів змінені на числові:")
print('3. Вивести k+7 перших записів (знову).')
print(data.iloc[:k+7])
print('4. Визначити та вивести тип полів кожного запису.')
print(data.dtypes)

print("""6. Ввести нові поля: 
a. Сумарний обсяг продаж автомобілів (нових та б/в) у кожний
період; (Total sales volume )
b. Сумарний дохід від продажу автомобілів (нових та б/в) у кожний
період; (Total income)
c. Різницю в обсязі продаж нових та б/в автомобілів у кожній
період. (the difference )""")
data['Total Sales Volume']=data['New']+data['Used']  # нове поле -Сумарний обсяг продаж автомобілів 
                                                     #нових та б/в) у кожний період;  

data['Total income']=data['Total Sales New']+data['Total Sales Used'] # нове поле - Сумарний дохід від продажу автомобілів (нових та б/в) у кожний
                                                                    #період;
data['The Difference']=abs(data['New']-data['Used'])

print("""Змінити порядок розташування полів таким чином: Рік, Місяць, 
Сумарний дохід, Дохід від продажу нових автомобілів, Дохід від
продажу б/в автомобілів, Сумарний обсяг продаж, Обсяг продаж нових
автомобілів, Обсяг продаж б/в автомобілів, Різниця між обсягами
продаж нових та б/в автомобілів.""")
data=data[['Year', 'Month', 'Total income', 'Total Sales New', 'Total Sales Used', 'Total Sales Volume', 'New', 'Used', 'The Difference' ]]

print("""8. Визначити та вивести: 
a. Рік та місяць, у які нових автомобілів було продано менше за б/в; 
b. Рік та місяць, коли сумарний дохід був мінімальним; 
c. Рік та місяць, коли було продано найбільше б/в авто.""")
list1=data[data['New']<data['Used']]
print(list1[['Year', 'Month']])
l2=data[data['Total income']==data['Total income'].min()]
print(l2[['Year', 'Month']])

l3=data[data['Used']==data['Used'].max()]
print(l3[['Year', 'Month']])

print("""9. Визначити та вивести: 
a. Сумарний обсяг продажу транспортних засобів за кожен рік; 
b. Середній дохід від продажу б/в транспортних засобів в місяці М, 
де М – це порядковий номер у списку підгрупи за абеткою. """)
m=7 # липень
sum=data.groupby(['Year'])['Total Sales Volume'].sum()
print(sum)






jul_data = data[(data['Month'] == 'JUL')]['Total Sales Used'].mean()
count_jul=data[(data['Month'] == 'JUL')].count()

print("Середній дохід від продажу б/в транспортних засобів в місяці JUL:", jul_data)

print("""10. Побудувати стовпчикову діаграму обсягу продаж нових авто у
році 2010.""")



sales_2010_new = data[(data['Year'] == 2010)]

# Побудова стовпчикової діаграми
plt.figure(figsize=(6, 5))
plt.bar(sales_2010_new['Month'], sales_2010_new['New'], color='skyblue')
plt.xlabel('Місяць')
plt.ylabel('Обсяг продажів')
plt.title('Обсяг продажів нових авто у 2010 році')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("""11. Побудувати кругову діаграму сумарного обсягу продаж за кожен
рік. """)


sales_by_year = data.groupby('Year')['Total Sales Volume'].sum()

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(sales_by_year, labels=sales_by_year.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Сумарний обсяг продаж за кожен рік')
plt.show()

print("""12. Побудувати на одному графіку: 
a. Сумарний дохід від продажу нових авто; 
b. Сумарний дохід від продажу старих авто. """)



new_car_sales = data.groupby('Month')['Total Sales New'].sum()
used_car_sales = data.groupby('Month')['Total Sales Used'].sum()

plt.figure(figsize=(6, 5))
plt.plot(new_car_sales.index, new_car_sales.values, label='Нові авто', marker='o')
plt.plot(used_car_sales.index, used_car_sales.values, label='Старі авто', marker='x')
plt.xlabel('Місяць')
plt.ylabel('Сумарний дохід від продажу')
plt.title('Сумарний дохід від продажу нових та старих авто за місяць')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
