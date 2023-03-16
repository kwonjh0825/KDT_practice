SELECT lastName FROM employees;

SELECT lastName, firstName FROM employees;

SELECT * FROM employees;

SELECT firstName AS 이름 FROM employees;

SELECT productCode, (quantityOrdered * priceEach) AS '주문총액' FROM orderdetails;

SELECT firstName FROM employees ORDER BY firstName;

SELECT firstName FROM employees ORDER BY firstName DESC;

SELECT lastName, firstName FROM employees ORDER BY lastName DESC, firstName; 

SELECT productCode, (quantityOrdered * priceEach) AS totalSales FROM orderdetails ORDER BY totalSales DESC

