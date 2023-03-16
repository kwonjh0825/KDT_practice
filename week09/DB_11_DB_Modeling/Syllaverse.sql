CREATE TABLE `Lectures` (
	`lecture_id`	INT	NOT NULL,
	`lecture_date`	DATE	NULL,
	`lecture_name`	VARCHAR(100)	NULL
);

CREATE TABLE `Assignments` (
	`assignment_id`	INT	NOT NULL,
	`assignment_name`	VARCHAR(100)	NULL,
	`assignment_content`	VARCHAR(10000)	NULL,
	`assignment_deadline`	DATETIME	NOT NULL
);

CREATE TABLE `Surveys` (
	`survey_id`	INT	NOT NULL,
	`survey_name`	VARCHAR(100)	NOT NULL,
	`survey_content`	VARCHAR(1000)	NOT NULL,
	`survey_deadline`	DATETIME	NULL
);

ALTER TABLE `Lectures` ADD CONSTRAINT `PK_LECTURES` PRIMARY KEY (
	`lecture_id`
);

ALTER TABLE `Assignments` ADD CONSTRAINT `PK_ASSIGNMENTS` PRIMARY KEY (
	`assignment_id`
);

ALTER TABLE `Surveys` ADD CONSTRAINT `PK_SURVEYS` PRIMARY KEY (
	`survey_id`
);

