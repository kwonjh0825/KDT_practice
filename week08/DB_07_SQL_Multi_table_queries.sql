SHOW COLUMNS FROM employees;
SHOW COLUMNS FROM offices;
SHOW COLUMNS FROM orderdetails;
SHOW COLUMNS FROM orders;
SHOW COLUMNS FROM products;

-- 문제 1
SELECT 
	employeeNumber, lastName, firstName, city
FROM
	employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY 
	employeeNumber ASC;
    
-- 문제 2
SELECT 
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY 
	customerNumber DESC;
    
-- 문제 3
SELECT 
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
RIGHT JOIN offices
	on customers.city = offices.city
ORDER BY 
	customerNumber DESC;
    
-- 문제 4
SELECT 
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 5

-- 문제 2번은 customers 테이블에 city를 기준으로 offices 테이블을 left join 한 결과로
-- (customers.city = offices.city OR offices.city IS NULL) 의 조건을 만족하는 레코드들을 결과로 도출한다

-- 문제 3번은 customers 테이블에 city를 기준으로 offices 테이블을 right join 한 결과로
-- (customers.city = offices.city OR customers.city IS NULL)의 조건을 만족하는 레코드들을 결과로 도출한다

-- 문제 4번은 customers 테이블에 city를 기준으로 offices 테이블을 inner join 한 결과로
-- (customers.city = offices.city) 의 조건을 만족하는 레코드들을 결과로 도출한다. 

-- join 의 종류에 따라 도출해야 하는 조건이 달라지기 때문에 세 가지의 문제 결과가 모두 다르게 도출된다. 

-- 문제 6
(SELECT 
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
)
UNION
(SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
)
ORDER BY
	customerNumber DESC;
    
-- 문제 7
SELECT 
	orderdetails.orderNumber, orderDate
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber ASC;
    
-- 문제 8
SELECT
	orderNumber, orderdetails.productCode, productName
FROM
	orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber ASC;
    
-- 문제 9
SELECT 
	orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderdetails.orderNumber ASC;
