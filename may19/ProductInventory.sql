use ABC;
create table ProductInventory (
    ProductID int primary key,
    ProductName varchar(100),
    Category varchar(50),
    Quantity int,
    UnitPrice decimal(10, 2),
    Supplier varchar(100),
    LastRestocked Date
);

insert into ProductInventory
(ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
values
(1, 'Laptop', 'Electronics', 20, 70000, 'TechMart', '2025-04-20'),
(2, 'Office Chair', 'Furniture', 50, 5000, 'HomeComfort', '2025-04-18'),
(3, 'Smartwatch', 'Electronics', 30, 15000, 'GadgetHub', '2025-04-22'),
(4, 'Desk Lamp', 'Lighting', 80, 1200, 'BrightLife', '2025-04-25'),
(5, 'Wireless Mouse', 'Electronics', 100, 1500, 'GadgetHub', '2025-04-30');

select * from ProductInventory;

--1. CRUD Operations:
--1.
insert into ProductInventory
(ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
values(6,'Gaming Keyboard','Electronics',40,3500,'TechMart','2025-05-01');
--2.
update ProductInventory
set Quantity=20
where ProductName='Desk Lamp';
--3.
delete from ProductInventory
where ProductID=2;
--4.
select * from ProductInventory
order by ProductName;

--2. Sorting and Filtering:
--5.
select * from ProductInventory
order by Quantity desc;

--6.
select * from ProductInventory
where Category='Electronics';

--7.
select * from ProductInventory
where Category='Electronics' and Quantity>20;

--8.
select * from ProductInventory
where Category='Electronics' or UnitPrice<2000;

--3. Aggregation and Grouping:

--9.
select sum(Quantity*UnitPrice) as totalvalue from ProductInventory;

--10.
select Category,avg(UnitPrice) as avgprice from ProductInventory
group by Category;
--11.
select count(*) as prodcount from ProductInventory
where Supplier='GadgetHub';

--4. Conditional and Pattern Matching:
--12.
select * from ProductInventory
where ProductName like 'W%';
--13.
select * from ProductInventory
where Supplier='GadgetHub' and UnitPrice>10000;
--14.
select * from ProductInventory
where UnitPrice between 1000 and 20000;

--5. Advanced Queries:
--15.
select top 3 * from ProductInventory
order by UnitPrice desc;
--16.
select * from ProductInventory
where LastRestocked >= DATEADD(DAY,-10,'2025-04-19');

--17.
select Supplier,sum(Quantity) as supplierquantity from ProductInventory
group by Supplier;

--18.
select * from ProductInventory
where Quantity<30;

--6.Join and Subqueries
--19.
select top 1 supplier,count(*) as prodcount
from ProductInventory
group by Supplier
order by prodcount desc;

--20.

select top 1 ProductName,(Quantity*UnitPrice) as stockvalue from ProductInventory
order by stockvalue desc;






















