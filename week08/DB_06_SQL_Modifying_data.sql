-- 문제 1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT NOW(),
    PRIMARY KEY (userId)
);

SHOW COLUMNS FROM users;

-- 문제 2
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES 
	('Beemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL), 
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', NULL), 
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);
    
SELECT * FROM users;

-- 문제 3
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
	('Minji', 'Kim', '2004-05-07', 'Seoul', 'Korea', NULL), 
    ('Hanni', 'Pham', '2004-10-06', 'Seoul', 'Korea', NULL),
    ('Daniel', 'Marsh', '2005-04-11', 'Seoul', 'Korea', NULL),
    ('Haerin', 'Kang', '2006-05-15', 'Seoul', 'Korea', NULL),
    ('Hyein', 'Lee', '2008-04-21', 'Seoul', 'Korea', NULL);
    
-- 문제 4
UPDATE users
SET 
	first_name='Junhyuk',
    last_name='Kwon', 
    birthday='1997-08-25'
WHERE
	userId=2;
    
-- 문제 5
UPDATE users
SET
	country='Korea'
WHERE
	country IS NULL;
    
-- 문제 6
DELETE 
FROM users
WHERE first_name='Beemo';

-- 문제 7
DELETE
FROM users
WHERE
	first_name='Kwangsoo'
    AND
    last_name='Lee';
    
-- 문제 8
DELETE 
FROM users
ORDER BY created_at DESC
LIMIT 1;
