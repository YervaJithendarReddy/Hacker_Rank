-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-18/problem
-- Difficulty: Medium
-- Max Score: 25
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

select round(abs(min(lat_n)-max(lat_n))+abs(min(long_w)-max(long_w)),4) from station
