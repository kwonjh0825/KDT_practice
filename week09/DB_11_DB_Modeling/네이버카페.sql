CREATE TABLE `Users` (
	`user_id`	VARCHAR(20)	NOT NULL,
	`user_birthday`	DATE	NOT NULL,
	`user_password`	VARCHAR(20)	NOT NULL
);

CREATE TABLE `Cafes` (
	`cafe_id`	INT	NOT NULL,
	`cafe_name`	VARCHAR(20)	NOT NULL,
	`cafe_createdAt`	DATETIME	NOT NULL,
	`cafe_level`	INT	NOT NULL
);

CREATE TABLE `cafe_members` (
	`cafe_id`	INT	NOT NULL,
	`user_id`	VARCHAR(20)	NOT NULL,
	`join_date`	DATE	NOT NULL,
	`count_article`	INT	NOT NULL	DEFAULT 0,
	`count_comment`	INT	NOT NULL	DEFAULT 0
);

CREATE TABLE `articles` (
	`article_id`	INT	NOT NULL,
	`user_id`	VARCHAR(20)	NOT NULL,
	`article_title`	VARCHAR(100)	NOT NULL,
	`article_createdAt`	DATETIME	NOT NULL
);

ALTER TABLE `Users` ADD CONSTRAINT `PK_USERS` PRIMARY KEY (
	`user_id`
);

ALTER TABLE `Cafes` ADD CONSTRAINT `PK_CAFES` PRIMARY KEY (
	`cafe_id`
);

ALTER TABLE `articles` ADD CONSTRAINT `PK_ARTICLES` PRIMARY KEY (
	`article_id`
);

