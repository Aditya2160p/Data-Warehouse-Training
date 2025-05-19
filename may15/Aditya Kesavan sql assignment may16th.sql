use ABC;
create table Book (
    BookID int primary key,
    Title varchar(100),
    Author varchar(100),
    Genre varchar(50),
    Price int,
    PublishedYear int,
    Stock int
);

insert into Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock) values
(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 50),
(2, 'Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 500, 2011, 30),
(3, 'Atomic Habits', 'James Clear', 'Self-Help', 400, 2018, 25),
(4, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Personal Finance', 350, 1997, 20),
(5, 'The Lean Startup', 'Eric Ries', 'Business', 450, 2011, 15);

select* from Book;
--1.CRUD OPERATIONS

--1.
insert into Book (BookID,Title,Author,Genre,Price,PublishedYear,Stock)values
(6,'Deep Work','Cal Newport','Self-Help',420,2016,35);

--2.
update Book
set Price=Price+50
where Genre='Self-Help';

--3.
delete from Book
where BookID=4;

--4.
select * from Book
order by Title;

--2. Sorting and Filtering

--5.
select * from Book
order by Price desc;

--6.
select * from Book
where Genre='Fiction';

--7.
select * from Book
where Genre='Self-Help' and Price>400;

--8.
select * from Book
where Genre='Fiction' or PublishedYear>2000;

--3.Aggregation and grouping

--9.
select sum(Price * Stock) as totalstockvalue from Book;

--10.
select Genre,avg(Price) as avg_price from Book
group by Genre;

--11.
select count(*) from Book
where Author='Paulo Coelho';

--4.Conditional and pattern matching

--12.
select * from Book
where Title like '%The%';

--13.
select * from Book
where Author='Yuval Noah Harari' and price<600;

--14.
select * from Book
where Price between 300 and 500;

--4. CONDITIONAL AND PATTERN MATCHING

--15.
select top 3 * from Book
order by Price desc;

--16.
select * from Book
where PublishedYear<2000;

--17.
select Genre,count(*) from Book
group by Genre;

--18.
select Title,count(*) as bcount from Book
group by Title
having count(*)>1;

--6.Join and Subqueries
--19.
select top 1 Author,count(*) as tot_books from Book
group by Author
order by tot_books desc;

--20.
select b.Genre, b.Title, b.Author, b.PublishedYear
from Book b
join (
    select Genre,min(PublishedYear) as earlyyear
    from Book
    group by Genre
) as early
on b.Genre = early.Genre and b.PublishedYear = early.earlyyear;

