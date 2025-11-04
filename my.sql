CREATE DATABASE chandigarh_university1;

USE chandigarh_university1;

CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    fee_min INT,
    fee_max INT,
    duration_years FLOAT,
    eligibility VARCHAR(200),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
-- Departments
INSERT INTO departments (name) VALUES ('Engineering');
INSERT INTO departments (name) VALUES ('Management');
INSERT INTO departments (name) VALUES ('Pharmacy');
INSERT INTO departments (name) VALUES ('Law');
INSERT INTO departments (name) VALUES ('Arts');
INSERT INTO departments (name) VALUES ('Science');
INSERT INTO departments (name) VALUES ('Architecture');
INSERT INTO departments (name) VALUES ('Computing & IT');

-- Courses with sample data
INSERT INTO courses (name, department_id, fee_min, fee_max, duration_years, eligibility) VALUES
('B.E. Computer Science', 1, 168000, 317000, 4, 'Class 12 with PCM, CUET/JEE score'),
('MBA', 2, 220000, 340000, 2, 'Graduation, CAT/CMAT/MAT score'),
('B.Pharm', 3, 168000, 225000, 4, 'Class 12 in Science stream'),
('LLB', 4, 80000, 135000, 3, 'Graduation'),
('BFA', 5, 80000, 120000, 4, 'Class 12 any stream'),
('B.Sc. Hotel Management', 6, 100000, 180000, 3, 'Class 12 any stream'),
('B.Arch', 7, 168000, 250000, 5, 'Class 12 with Math, NATA score'),
('BCA', 8, 100000, 185000, 3, 'Class 12 in any stream, preferably with Math');
-- Additional Courses
INSERT INTO courses (name, department_id, fee_min, fee_max, duration_years, eligibility) VALUES
('B.Tech Artificial Intelligence', 1, 168000, 317000, 4, 'Class 12 with PCM, CUET/JEE score'),
('B.Tech Civil Engineering', 1, 168000, 317000, 4, 'Class 12 with PCM, CUET/JEE score'),
('M.Tech Computer Science', 1, 120000, 180000, 2, 'B.E./B.Tech in relevant field'),
('BBA (Marketing)', 2, 120000, 200000, 3, 'Class 12 in any stream'),
('BCom (Hons)', 2, 80000, 150000, 3, 'Class 12 in Commerce/Any stream'),
('MCA', 8, 100000, 185000, 2, 'Graduation with Math at 10+2 or degree level'),
('BSc (Hons) Chemistry', 6, 90000, 150000, 3, 'Class 12 with Science stream'),
('BSc Nursing', 6, 100000, 180000, 4, 'Class 12 with Biology'),
('BA LLB', 4, 100000, 135000, 5, 'Class 12 in any stream, CUET/University entrance'),
('B.Des. (Design)', 5, 120000, 200000, 4, 'Class 12 in any stream'),
('Bachelor of Optometry (B.Optom)', 3, 90000, 160000, 4, 'Class 12 in Science stream'),
('BMLT (Medical Lab Technology)', 6, 90000, 150000, 3, 'Class 12 with Biology'),
('LLM', 4, 100000, 150000, 1, 'LLB Degree'),
('MPharm (Pharmaceutics)', 3, 150000, 200000, 2, 'B.Pharm degree');
