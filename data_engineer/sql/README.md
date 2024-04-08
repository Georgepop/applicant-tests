# Тест SQL

На основе таблиц базы данных, напишите SQL код, который возвращает необходимые результаты
Пример: 

Общее количество товаров
```sql
select count (*) from items
```

## Структура данных

Используемый синтаксис: Oracle SQL или другой

| Сustomer       | Description           |
| -------------- | --------------------- |
| customer\_id   | customer unique id    |
| customer\_name | customer name         |
| country\_code  | country code ISO 3166 |

| Items             | Description       |
| ----------------- | ----------------- |
| item\_id          | item unique id    |
| item\_name        | item name         |
| item\_description | item description  |
| item\_price       | item price in USD |

| Orders       | Description                 |
| ------------ | --------------------------- |
| date\_time   | date and time of the orders |
| item\_id     | item unique id              |
| customer\_id | user unique id              |
| quantity     | number of items in order    |

| Countries     | Description           |
| ------------- | --------------------- |
| country\_code | country code          |
| country\_name | country name          |
| country\_zone | AMER, APJ, LATAM etc. |


| Сonnection\_log         | Description                           |
| ----------------------- | ------------------------------------- |
| customer\_id            | customer unique id                    |
| first\_connection\_time | date and time of the first connection |
| last\_connection\_time  | date and time of the last connection  |

## Задания

### 1) Количество покупателей из Италии и Франции

| **Country_name** | **CustomerCountDistinct** |
| ------------------------- | ----------------------------- |
| France                    | #                             |
| Italy                     | #                             |

```sql
select country_name, count(distinct customer_id)
from customer
join countries using(country_code)
where country_name in ('France','Italy')
group by country_name
```

### 2) ТОП 10 покупателей по расходам

| **Customer_name** | **Revenue** |
| ---------------------- | ----------- |
| #                      | #           |
| #                      | #           |
| #                      | #           |
| #                      | #           |
| #                      | #           |
| #                      | #           |
| #                      | #           |

```sql
select customer_name, sum(quantity*item_price)
from customer
join orders using(customer_id)
join items using(item_id)
group by customer_name
```

### 3) Общая выручка USD по странам, если нет дохода, вернуть NULL

| **Country_name** | **RevenuePerCountry** |
| ------------------------- | --------------------- |
| Italy                     | #                     |
| France                    | NULL                  |
| Mexico                    | #                     |
| Germany                   | #                     |
| Tanzania                  | #                     |

```sql
select *
from countries
left join 
(select country_code, sum(quantity*item_price) as RevenuePerCountry
from customer
join orders using(customer_id)
join items using(item_id)
group by country_code) t1 using(country_code)

```

### 4) Самый дорогой товар, купленный одним покупателем

| **Customer\_id** | **Customer\_name** | **MostExpensiveItemName** |
| ---------------- | ------------------ | ------------------------- |
| #                | #                  | #                         |
| #                | #                  | #                         |
| #                | #                  | #                         |
| #                | #                  | #                         |
| #                | #                  | #                         |
| #                | #                  | #                         |
| #                | #                  | #                         |

```sql
select * from 
(select customer_id, max(item_price) as item_price
from customer
join orders using(customer_id)
join items using(item_id)
group by customer_id) as t1
join
(select customer_id, customer_name, item_price, item_name 
from customer
join orders using(customer_id)
join items using(item_id)
) as t2
using(customer_id, item_price)
```

### 5) Ежемесячный доход

| **Month (MM format)** | **Total Revenue** |
| --------------------- | ----------------- |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |

```sql
select month(date_time), sum(quantity*item_price)
from orders
join items using(item_id)
group by month(date_time)
```

### 6) Найти дубликаты

Во время передачи данных произошел сбой, в таблице orders появилось несколько 
дубликатов (несколько результатов возвращаются для date_time + customer_id + item_id). 
Вы должны их найти и вернуть количество дубликатов.

```sql
select date_time, customer_id, item_id, count(customer_id) - 1
from orders
group by date_time, customer_id, item_id
```

### 7) Найти "важных" покупателей

Создать запрос, который найдет всех "важных" покупателей,
т.е. тех, кто совершил наибольшее количество покупок после своего первого заказа.

| **Customer\_id** | **Total Orders Count** |
| --------------------- |-------------------------------|
| #                     | #                             |
| #                     | #                             |
| #                     | #                             |
| #                     | #                             |
| #                     | #                             |
| #                     | #                             |
| #                     | #                             |

```sql
select customer_id, count(date_time)
from orders
group by customer_id
having count(date_time)> 1 
```

### 8) Найти покупателей с "ростом" за последний месяц

Написать запрос, который найдет всех клиентов,
у которых суммарная выручка за последний месяц
превышает среднюю выручку за все месяцы.

| **Customer\_id** | **Total Revenue** |
| --------------------- |-------------------|
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |
| #                     | #                 |

```sql
with q as (select month(date_time) as mm, customer_id,  sum(quantity*item_price) as rev
from orders
join items using(item_id)
group by month(date_time), customer_id),
a as (select customer_id, sum(rev) as rev, count(mm) as mmon
from q 
group by customer_id),
w as (select customer_id, rev as last_rev
from q 
where mm == month(now())-1)

select customer_id, rev
from w
join 
a using(customer_id)
where last_rev > rev/mmon

```
