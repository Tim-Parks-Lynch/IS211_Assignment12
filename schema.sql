DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS student_results;


CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL
);

CREATE TABLE quizzes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  quiz_subject TEXT NOT NULL, 
  num_questions INT NOT NULL,
  quiz_date DATETIME
);

CREATE TABLE student_results(
  student_id INTEGER NOT NULL,
  quiz_id INTEGER NOT NULL,
  grade INTEGER NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (quiz_id) REFERENCES quizzes(id),
  PRIMARY KEY(student_id, quiz_id, grade),
  CHECK (grade > 0 and grade < 101)
);

INSERT INTO 
	students(id, firstname, lastname)
VALUES
	(1, 'John', 'Smith');

INSERT INTO 
  quizzes(id, quiz_subject, num_questions, quiz_date)
VALUES
  (1, 'Python Basics', 5, "February, 5th, 2015");

INSERT INTO
  student_results(student_id, quiz_id, grade)
VALUES
  (1, 1, 85);

