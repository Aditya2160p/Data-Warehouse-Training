use ABC;

create table EmployeeAttendance (
    AttendanceID int primary key,
    EmployeeName varchar(100),
    Department varchar(50),
    Date DATE,
    Status varchar(20),
    HoursWorked int
);

insert into EmployeeAttendance (AttendanceID, EmployeeName, Department, Date, Status, HoursWorked)
values
(1, 'John Doe', 'IT', '2025-05-01', 'Present', 8),
(2, 'Priya Singh', 'HR', '2025-05-01', 'Absent', 0),
(3, 'Ali Khan', 'IT', '2025-05-01', 'Present', 7),
(4, 'Riya Patel', 'Sales', '2025-05-01', 'Late', 6),
(5, 'David Brown', 'Marketing', '2025-05-01', 'Present', 8);

--CRUD OPERATIONS
--1.
insert into EmployeeAttendance(AttendanceID,EmployeeName,Department,Date,Status,HoursWorked)
values(6,'Neha Sharma','Finance','2025-05-01','Present',8);

select * from EmployeeAttendance;
--2.
update EmployeeAttendance
set Status='Present'
where EmployeeName='Riya Patel';
--3.
Delete from EmployeeAttendance
where EmployeeName='Priya Singh' and Date='2025-05-01';
--4.
select * from EmployeeAttendance
order by EmployeeName;

--2. SORTING AND FILTERING
--5.
select * from EmployeeAttendance
order by HoursWorked desc;
--6.
select * from EmployeeAttendance
where Department='IT';
--7.
select * from EmployeeAttendance
where Status='Present' and Department='IT';
--8.
select * from EmployeeAttendance
where Status='Absent' or Status='Late';

--3. AGGREGATION AND GROUPING
--9.
select Department,sum(HoursWorked) as TotalHours from EmployeeAttendance
group by Department;
--10.
select Department,avg(HoursWorked) as avgHoursWorked from EmployeeAttendance
group by Department;
--11.
select Status,count(*) as StatusCount from EmployeeAttendance
group by Status;

--4.Conditional and pattern matching
--12.
select * from EmployeeAttendance
where EmployeeName like 'R%';
--13.
select * from EmployeeAttendance
where HoursWorked>6 and Status='Present'; 
--14.
select * from EmployeeAttendance
where HoursWorked between 6 and 8;

--5.Advanced queries
--15.
select top 2 * from EmployeeAttendance
order by HoursWorked desc;
--16.
select * from EmployeeAttendance
where HoursWorked < (select avg(HoursWorked) as workavg  
from EmployeeAttendance);

--17.
select Status,avg(HoursWorked) as StatusAvg from EmployeeAttendance
group by Status;

--18.
select EmployeeName,count(*) as empcount from EmployeeAttendance
group by EmployeeName
having count(*)>1;
--JOINS AND SUBQUERIES
--19.
select top 1 Department,count(*) as PresentEmpCount 
from EmployeeAttendance
where Status ='Present'
group by Department
order by PresentEmpCount desc;
--20.
with maxhoursemp as (
select Department,max(HoursWorked) as maxhours from EmployeeAttendance
group by Department)
select ea.Department,ea.HoursWorked from EmployeeAttendance ea
join maxhoursemp as mhe
on ea.Department=mhe.Department and ea.HoursWorked=mhe.maxhours;