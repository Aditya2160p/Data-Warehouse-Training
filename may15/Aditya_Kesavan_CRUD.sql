create database ABC;
use ABC;

--Table Creation
create table ProductTable(
ProductID int primary key,
ProductName varchar(100),
Category varchar(100),
Price int,
StockQuantity int,
Supplier varchar(100)
);
INSERT INTO ProductTable (ProductID, ProductName, Category, Price, StockQuantity, Supplier) VALUES
(1, 'Laptop', 'Electronics', 70000, 50, 'TechMart'),
(2, 'Office Chair', 'Furniture', 5000, 100, 'HomeComfort'),
(3, 'Smartwatch', 'Electronics', 15000, 200, 'GadgetHub'),
(4, 'Desk Lamp', 'Lighting', 1200, 300, 'BrightLife'),
(5, 'Wireless Mouse', 'Electronics', 1500, 250, 'GadgetHub');

select * from ProductTable;
--CRUD Operation

--1.
insert into ProductTable(ProductID, ProductName, Category, Price, StockQuantity, Supplier)
values (6, 'Gaming Keyboard', 'Electronics', 3500, 150, 'TechMart');

--2.
update ProductTable
set price=price+price*0.10
where Category='Electronics';

--3.
delete from ProductTable
where ProductID=4;

--4.
select * from ProductTable
order by price desc;

--Sorting and Filtering

--5.
select * from ProductTable
order by StockQuantity;

--6.
select * from ProductTable
where Category='Electronics';

--7.
select * from ProductTable
where Category='Electronics' and price>5000;

--8.
select * from ProductTable
where Category='Electronics' or price<2000;

--Aggregation and Grouping

--9.
select sum(Price*StockQuantity) as TotalStockValue
from ProductTable;

--10.
select Category,avg(price) as AvgProdPrice from ProductTable
group by Category;

--11.
select count(*) as GadgetHubProducts from ProductTable
where Supplier='GadgetHub';

--Conditional and Pattern Matching

--12.
select * from ProductTable
where ProductName like '%Wireless%';

--13.
select * from ProductTable
where Supplier='TechMart' or Supplier='GadgetHub';

--14.
select * from ProductTable
where price between 1000 and 20000;

--Advanced Queries:

--15.
select * from ProductTable
where StockQuantity > (
select avg(StockQuantity) FROM ProductTable
);
--16.
select top 3 * from ProductTable
order by price desc;
--17.
select Supplier, count(*) as Occurrences
from ProductTable
group by Supplier
having count(*) > 1;
--18.
select
Category, 
count(*) AS TotalProducts,
sum(Price * StockQuantity) as TotalStockValue
from ProductTable
group by Category;

--Joins and Subqueries
--19.
select top 1 count(*),Supplier as higest from ProductTable
group by Supplier
order by higest desc;
--20.
select * from ProductTable p
where p.price =(
select max(price) from ProductTable
where p.Category=Category);




