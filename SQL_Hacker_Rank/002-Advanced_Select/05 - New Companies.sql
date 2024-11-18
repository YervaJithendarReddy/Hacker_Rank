-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/the-company/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================


/*
Enter your query here.
*/
select c.company_code,c.founder,count(Distinct l.lead_manager_code),count(Distinct s.senior_manager_code),count(Distinct m.manager_code),count(Distinct e.employee_code) from company c
join Lead_manager l
on c.company_code = l.company_code
join senior_manager s
on c.company_code = s.company_code
join manager m
on c.company_code = m.company_code
join employee e
on c.company_code = e.company_code
group by c.company_code,c.founder
order by c.company_code

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication
-- COUNT() used to return the number of rows in a table
