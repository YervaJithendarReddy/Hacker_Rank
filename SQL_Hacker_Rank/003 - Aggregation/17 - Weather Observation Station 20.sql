-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-20/problem
-- Difficulty: Medium
-- Max Score: 40
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

select round(lat_n,4) from station s
where (select count(lat_n) from station where lat_n < s.lat_n)=
        (select count(lat_n) from station where lat_n>s.lat_n)
