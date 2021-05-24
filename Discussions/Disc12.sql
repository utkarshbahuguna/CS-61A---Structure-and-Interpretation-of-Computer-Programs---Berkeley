-- https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc12.pdf

-- 2.1
SELECT name FROM records WHERE supervisor = 'Olvier Warbucks'

-- 2.2
SELECT * FROM records WHERE name = supervisor

-- 2.3
SELECT name FROM records WHERE salary > 50000 ORDER BY name

-- 3.1
SELECT m.day, m.time FROM records AS employee, meetings AS m
WHERE employee.supervisor = 'Oliver Warbucks' and employee.division = m.division GROUP BY m.day, m.time

-- 3.2
SELECT employee.name FROM records as employee, records as supervisor WHERE employee.supervisor = supervisor.name and employee.division <> supervisor.division

-- 3.3
SELECT a.name, b.name FROM records as a, records as b, meetings as m1, meetings as m2
WHERE a.division = m1.division and b.division = m2.division and m1.day = m2.day and m1.time = m2.time and a.name < b.name

-- 4.1
SELECT supervisor, sum(salary) as total_salaries FROM records GROUP BY supervisor

-- 4.2
SELECT m.day FROM records as employee, meetings as m WHERE employee.division = m.division GROUP BY m.day HAVING count(employee.name) < 5

-- 4.3
SELECT a.division FROM records as a, records as b WHERE a.division = b.division and a.name < b.name
GROUP BY a.division HAVING count(a.name) > 1 and a.salary + b.salary < 100000

-- 5.1
CREATE TABLE num_taught AS
SELECT professor, course, COUNT(semester) as count FROM courses GROUP BY professor, course

-- 5.2
SELECT a.professor, b.professor, a.count FROM num_taught as a, num_taught as b WHERE a.course = b.course and a.count = b.count and a.professor < b.professor

-- 5.3
SELECT a.professor, b.professor FROM courses as a, courses as b WHERE a.course = b.course and a.semester = b.semester and a.name < b.name
GROUP BY a.professor, b.professor, a.course HAVING COUNT(*) > 1

