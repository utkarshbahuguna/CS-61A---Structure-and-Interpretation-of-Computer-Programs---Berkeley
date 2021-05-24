-- https://inst.eecs.berkeley.edu/~cs61a/fa19/hw/hw10/

CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name as name, sizes.size as size FROM dogs, sizes WHERE dogs.height > sizes.min and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child as dog FROM parents, dogs WHERE parents.parent = dogs.name ORDER BY -dogs.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name as sibling1, b.name as sibling2 FROM dogs as a, dogs as b, parents as p1, parents as p2
  WHERE a.name = p1.child and b.name = p2.child and p1.parent = p2.parent and a.name < b.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sibling1 || " and " || a.sibling2 || " are " || s1.size || " siblings" FROM siblings as a, size_of_dogs as s1, size_of_dogs as s2
  WHERE a.sibling1  = s1.name and a.sibling2 = s2.name and s1.size = s2.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height. Dogs should be listed in increasing order of height within the stack.
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;
INSERT INTO stacks_helper SELECT s.dogs || ", " || d.name, s.stack_height + d.height, d.height FROM stacks_helper as s, dogs as d
  WHERE s.last_height < d.height;
INSERT INTO stacks_helper SELECT s.dogs || ", " || d.name, s.stack_height + d.height, d.height FROM stacks_helper as s, dogs as d
  WHERE s.last_height < d.height;
INSERT INTO stacks_helper SELECT s.dogs || ", " || d.name, s.stack_height + d.height, d.height FROM stacks_helper as s, dogs as d
  WHERE s.last_height < d.height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE stack_height >= 170 ORDER BY stack_height;
