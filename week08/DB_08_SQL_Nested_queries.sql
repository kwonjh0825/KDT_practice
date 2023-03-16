SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM orderdetails;


-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY MSRP ASC;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY customerNumber ASC;

-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM (
	SELECT productCode, productName, productLine, MSRP
    FROM products
    WHERE productLine = 'Classic Cars'
) AS subtable
WHERE MSRP = (
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = 'Classic Cars'
);

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = 'Motorcycles'
);

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE COUNT(country) = (
 	SELECT COUNT(country) AS cnt
	FROM customers
    GROUP BY country
    ORDER BY cnt DESC
    LIMIT 1
)
ORDER BY customerNumber ASC;

-- 문제 5
SELECT customerNumber, customerName, count(*) AS order_count
FROM orders
INNER JOIN customers
	USING (customerNumber)
GROUP BY (customerNumber)
HAVING order_count = (
	SELECT count(*) as order_count
    FROM orders
    GROUP BY customerNumber
    ORDER BY order_count DESC
    LIMIT 1
);

-- 문제 6
SELECT productCode, productName
FROM orderdetails
INNER JOIN orders
	USING (orderNumber)
INNER JOIN products
	USING (productCode)
WHERE YEAR(orderDate) = '2004'
GROUP BY productCode
ORDER BY productCode DESC;

-- 문제 6(EXISTS 활용)
SELECT DISTINCT productCode, productName
FROM orderdetails
INNER JOIN products
	USING (productCode)
WHERE EXISTS(
	SELECT *
    FROM orders
    WHERE YEAR(orderDate) = 2004
)
ORDER BY productCode DESC;