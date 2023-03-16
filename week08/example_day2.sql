CREATE TABLE examples (
	examID INT AUTO_INCREMENT,	
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY(examID)
);

SHOW COLUMNS FROM examples;

-- ex01

ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;
    
-- ex02
ALTER TABLE
	examples
ADD
	age INT NOT NULL,
ADD
    address VARCHAR(100) NOT NULL;
    
-- ex03
ALTER TABLE
	examples 
MODIFY 
	address VARCHAR(50) NOT NULL;
    
-- ex04
ALTER TABLE
	examples
MODIFY 
	lastName VARCHAR(10) NOT NULL, 
MODIFY
    firstName VARCHAR(10) NOT NULL;
    
-- ex05
ALTER TABLE
	examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;
    
-- ex06
ALTER TABLE
	examples
DROP COLUMN
	address;
	
CREATE TABLE articles (
	id INT AUTO_INCREMENT, 
    title VARCHAR(100) NOT NULL, 
    content VARCHAR(200) NOT NULL, 
    createdAt DATE NOT NULL, 
    PRIMARY KEY (id)
);

-- ex07
INSERT INTO articles
VALUES (NULL,'hello', 'world', '2000-01-01');

SELECT * FROM articles;

-- ex08
INSERT INTO articles
VALUES 
	(NULL, 'title1', 'content1', '1900-01-01'), 
	(NULL, 'title2', 'content2', '1800-01-01'), 
    (NULL, 'title3', 'content3', '1700-01-01');
    
-- ex09
INSERT INTO articles
VALUES (NULL, 'mytitle', 'mycontent', CURDATE());

-- ex10
UPDATE articles
SET title='newTitle'
WHERE id = 1;

-- ex11
UPDATE articles
SET 
	title='newTitle2', 
    content='newContent2'
WHERE id = 2;

-- ex12
UPDATE articles
SET
	content=REPLACE(content, 'content', 'TEST');
    
-- ex13
DELETE 
FROM articles
WHERE id = 1;

-- ex14
DELETE
FROM articles
ORDER BY createdAt DESC
LIMIT 2;