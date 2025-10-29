CREATE TABLE sandwiches(
	sandwich_size varchar(50),
	price decimal(5,2)
);

CREATE TABLE resources(
	item varchar(50),
	amount int
);

CREATE TABLE recipes(
	sandwich_size varchar(50),
	item varchar(50),
	amount int
);


INSERT INTO sandwiches(sandwich_size, price) VALUES
	('small',1.75),
	('medium',3.25),
	('large',5.50);
	
INSERT INTO resources(item, amount) VALUES
	('bread',12),
	('ham',18),
	('cheese',24);
	
INSERT INTO recipes(sandwich_size,item, amount) VALUES
	('small','bread',2),
	('small','ham',4),
	('small','cheese',4),
	('medium','bread',4),
	('medium','ham',6),
	('medium','cheese',8),
	('large','bread',6),
	('large','ham',8),
	('large','cheese',12);
    
SELECT * FROM sys.sandwiches;
SELECT * FROM sys.resources;
SELECT * FROM sys.recipes;