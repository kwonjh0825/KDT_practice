DROP TABLE IF EXISTS articles;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(50) NOT NULL,
    userID INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO 
	users (name)
VALUES
	('권미자'), 
    ('류준하'),
    ('정영식');
    
SELECT * FROM users;    
    
INSERT INTO
	articles (title, content, userID)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2), 
    ('제목3', '내용3', 4);
    
SELECT * FROM articles;

-- ex01
SELECT
	productCode, productName, textDescription
FROM 
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;

-- ex02
SELECT
	orders.orderNumber, status, (quantityOrdered * priceEach) as totalprice
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;

-- ex03    
SELECT
	orders.orderNumber, status, SUM(quantityOrdered * priceEach) as totalSales
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY orderNumber;

-- ex04
SELECT 
	contactFirstName, orderNumber, status
FROM
	customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;
    
-- ex05
SELECT 
	contactFirstName, orderNumber, status
FROM
	customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;

-- ex06
SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber;
    
-- ex07
SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE 
	customerNumber IS NULL;
