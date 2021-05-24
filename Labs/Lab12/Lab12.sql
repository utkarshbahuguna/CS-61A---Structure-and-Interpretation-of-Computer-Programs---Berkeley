.read fa19data.sql

-- https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab12/

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest, time LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


-- Optional Questions


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;

CREATE TABLE fa19favpets AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa19dog AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet HAVING pet = "dog";


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, COUNT(*) as count FROM students WHERE seven = '7' GROUP BY instructor;


