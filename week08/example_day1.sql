-- ex01
SELECT
	lastName
FROM
	employees
ORDER BY
	lastName ASC;

-- ex02
SELECT DISTINCT
	lastName
FROM
	employees
ORDER BY
	lastName ASC;

-- ex03
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode = 1;
    
-- ex04
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != 'Sales Rep';
    
-- ex05
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode >= 3 
    AND
    jobTitle = 'Sales Rep';

-- ex06
SELECT
	lastName, firstName, officeCode, jobTitle
FROM
	employees
WHERE
	officeCode < 3 
    OR
    jobTitle = 'Sales Rep';

-- ex07
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4;

-- ex08
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode BETWEEN 1 AND 4
ORDER BY
	officeCode ASC;
    
-- ex09
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode IN (1, 3, 4);
    
-- ex10
SELECT
	lastName, firstName, officeCode
FROM
	employees
WHERE
	officeCode NOT IN (1, 3, 4);

-- ex11
SELECT
	lastName, firstName
FROM
	employees
WHERE
	lastName LIKE '%son';
    
-- ex12
SELECT
	lastName, firstName
FROM 
	employees
WHERE 
	firstName LIKE '___y';
    
-- ex13
SELECT 
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT
	7;
    
-- ex14
SELECT 
	firstName, officeCode
FROM
	employees
ORDER BY
	officeCode DESC
LIMIT
	3, 5;

-- ex15
SELECT
	country, AVG(creditLimit) AS avgOfCreditLimit
FROM 
	customers
GROUP BY
	country
ORDER BY
	avgOfCreditLimit DESC; 
	
-- ex16
SELECT 
	country, AVG(creditLimit)
FROM 
	customers
GROUP BY
	country
HAVING
	AVG(creditLimit) > 80000;