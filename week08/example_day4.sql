SELECT * FROM payments;
SELECT * FROM employees;
SELECT * FROM offices;
SELECT * FROM orders;
SELECT * FROM customers;


-- ex01
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);
    
-- ex02
SELECT lastName, firstName
FROM employees
WHERE officecode IN (
	SELECT officeCode
    FROM offices
    WHERE country = 'USA'
);

-- ex03
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT customerNumber
    FROM orders
);

-- ex04
SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT customers.customerNumber, amount, contactFirstName
    FROM payments
    INNER JOIN customers
		ON payments.customerNumber = customers.customerNumber
) AS subtable
WHERE amount = (
	SELECT MAX(amount) FROM payments
);

-- ex05
SELECT 
	customerNumber, CustomerName
FROM
	customers
WHERE EXISTS (
	SELECT *
    FROM orders
	WHERE customers.customerNumber = orders.customerNumber
);

-- ex06
SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT * 
    FROM offices
    WHERE city = 'Paris' AND
    offices.officeCode = employees.officeCode
);

-- ex07
SELECT contactFirstName, creditLimit, 
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END AS grade
FROM customers;

-- ex08
SELECT orderNumber, status, 
	CASE
		WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END as details
FROM orders;