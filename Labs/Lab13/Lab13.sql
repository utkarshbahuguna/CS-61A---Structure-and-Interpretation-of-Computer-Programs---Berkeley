.read data.sql


-- https://inst.eecs.berkeley.edu/~cs61a/fa19/lab/lab13/


-- Give Interest
UPDATE accounts SET amount = amount * 1.02;


-- Split Accounts
CREATE TABLE split_accounts (name, amount);
INSERT INTO split_accounts SELECT name || "'s Saving Account", amount/2 FROM accounts;
INSERT INTO split_accounts SELECT name || "'s Checking Account", amount/2 FROM accounts;

DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts AS
  SELECT * FROM split_accounts;

DROP TABLE IF EXISTS split_accounts;

-- Whoops!
DROP TABLE IF EXISTS accounts;


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price FROM products GROUP BY category;

CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) as min_price FROM inventory GROUP BY item;

CREATE TABLE shopping_list AS
  SELECT products.name, lowest_prices.store FROM products, lowest_prices
  WHERE products.name = lowest_prices.item GROUP BY products.category HAVING MAX(products.MSRP / products.rating);

CREATE TABLE total_bandwidth AS
  SELECT SUM(stores.Mbs) FROM stores, shopping_list WHERE stores.store = shopping_list.store;
