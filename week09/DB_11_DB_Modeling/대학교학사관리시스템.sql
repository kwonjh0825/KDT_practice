CREATE TABLE `Students` (
	`student_id`	INT	NOT NULL,
	`department`	VARCHAR(100)	NOT NULL,
	`phone_number`	VARCHAR(100)	NULL,
	`email_address`	VARCHAR(100)	NULL
);

CREATE TABLE `Untitled` (
	`professor_id`	INT	NOT NULL,
	`department`	VARCHAR(100)	NOT NULL,
	`phone_number`	VARCHAR(100)	NULL,
	`email_address`	VARCHAR(100)	NULL
);

CREATE TABLE `Lecture` (
	`lecture_code`	INT	NOT NULL,
	`professor_id2`	INT	NOT NULL,
	`major`	VARCHAR(100)	NULL,
	`semester_id`	INT	NOT NULL
);

CREATE TABLE `Untitled2` (
	`student_id`	INT	NOT NULL,
	`lecture_code`	INT	NOT NULL,
	`professor_id2`	INT	NOT NULL
);

ALTER TABLE `Students` ADD CONSTRAINT `PK_STUDENTS` PRIMARY KEY (
	`student_id`
);

ALTER TABLE `Untitled` ADD CONSTRAINT `PK_UNTITLED` PRIMARY KEY (
	`professor_id`
);

ALTER TABLE `Lecture` ADD CONSTRAINT `PK_LECTURE` PRIMARY KEY (
	`lecture_code`,
	`professor_id2`
);

ALTER TABLE `Untitled2` ADD CONSTRAINT `PK_UNTITLED2` PRIMARY KEY (
	`student_id`
);

ALTER TABLE `Lecture` ADD CONSTRAINT `FK_Untitled_TO_Lecture_1` FOREIGN KEY (
	`professor_id2`
)
REFERENCES `Untitled` (
	`professor_id`
);

ALTER TABLE `Untitled2` ADD CONSTRAINT `FK_Students_TO_Untitled2_1` FOREIGN KEY (
	`student_id`
)
REFERENCES `Students` (
	`student_id`
);

