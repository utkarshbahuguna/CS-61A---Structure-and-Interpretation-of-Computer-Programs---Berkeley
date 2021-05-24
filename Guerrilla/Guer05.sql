-- https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/guer05.pdf

-- 2.1
SELECT name, age FROM people WHERE age <= 26;

-- 2.2
SELECT poster, time FROM posts WHERE time < 230;

-- 2.3
SELECT likes.name FROM posts, likes WHERE posts.post_id = likes.post_id and posts.poster = likes.name;

-- 2.4
CREATE TABLE friends AS
    SELECT a.friend1, b.friend1 FROM requests as a, requests as b WHERE a.friend1 = b.friend2 and a.friend2 = b.friend1 and a.friend1 < b.friend1;

-- 2.5
SELECT friend1 FROM friends GROUP BY friend1 HAVING count(*) >= 4;

-- 2.6
SELECT state, COUNT(*) as num_friends FROM friends, people WHERE friends.friend1 = "Will" and people.name = friends.friend2 GROUP BY people.state;

-- 2.7
SELECT posts.text FROM posts, likes WHERE posts.post_id = likes.post_id GROUP BY posts.post_id HAVING MIN(likes.time - posts.time) <= 2;

-- 2.8
SELECT a.name, b.name FROM people as a, people as b WHERE a.hobby = b.hobby and a.name < b.name;

-- 2.9
SELECT state, COUNT(*) as population FROM people GROUP BY state ORDER BY -population;

-- 2.10
INSERT INTO requests VALUES ("Denero", "Hilfy");

-- 2.11
INSERT INTO requests SELECT "Denero", name FROM likes WHERE post_id = 349;

-- 2.12
UPDATE people SET hobby = "CS" WHERE name = "Joe";

-- 2.13
CREATE TABLE num_likes AS
    SELECT posts.poster as name, posts.post_id, COUNT(*) as number FROM posts, likes where posts.post_id = likes.post_id GROUP BY post_id;

-- 2.14
DELETE FROM num_likes WHERE name = "Carolyn" and number < 4;

-- 2.15
CREATE TABLE privacy(names, visibility DEFAULT "everyone");

-- 2.16
INSERT INTO privacy VALUES ("Hermish");