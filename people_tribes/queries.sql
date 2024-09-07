-- TASK 1: for all tribes, get the tribe name, and all names of people in this tribe

-- SOLUTION 1.A

SELECT 
	   tr.name AS tribe_name, 
	   ppl.name AS person_name
FROM 
	tribes tr
INNER JOIN people_tribes ppltr ON 
	-- all members 
	tr.id = ppltr.tribe_id
INNER JOIN people ppl ON 
	-- all people 
	ppl.id = ppltr.person_id;



-- TASK 2: find people who are not in a tribe

-- 1. find all people 
-- 2. find people who are in at least one tribe
-- 3. substract 2. from 1.

-- SOLUTION A

SELECT name
FROM people
WHERE id NOT IN
(
    SELECT 
    	person_id 
    FROM 
    	(SELECT 
          	person_id, 
    	  	COUNT(*) AS n_tribes
    	FROM people_tribes
    	GROUP BY person_id
    	HAVING n_tribes > 0) AS t
 );
 
 
 -- SOLUTION B

SELECT 
	name
FROM (
    SELECT 
        ppltr.person_id AS person_id,
        ppl.name AS name 
    FROM people ppl
    -- the left join fills up with null
    -- the person_id where there's no match in the people
    LEFT JOIN people_tribes ppltr ON
        ppl.id = ppltr.person_id
) AS all_ppl
-- filtering by null gives me back the people
-- who don't have a match in the people_members,
-- so people that don't belong to any tribe
WHERE all_ppl.person_id IS NULL;



-- SOLUTION C
SELECT 
	name
FROM (
    SELECT 
    	-- no need to compute the join 
        -- multiple times on the same person_id,
    	-- it suffices only once
        DISTINCT ppltr.person_id AS person_id,
        ppl.name AS name 
    FROM people ppl
    -- the left join fills up with null
    -- the person_id where there's no match in the people
    LEFT JOIN people_tribes ppltr ON
        ppl.id = ppltr.person_id
) AS all_ppl
WHERE all_ppl.person_id IS NULL;



-- TASK 3: count how many people per tribe 

SELECT 
	tr.name AS tribe,
    -- counting this field means to consider
    -- the non-matching rows (so the tribes
    -- that have no members) to be counted as 0
    COUNT(ppltr.tribe_id) AS tot
FROM
	tribes tr
LEFT JOIN people_tribes ppltr ON
    -- the left join will fill with null the field ppltr.tribe_id
    -- if there's no matching tribe_id in the people_tribes
    -- when matched against all tribes
	tr.id = ppltr.tribe_id
GROUP BY tribe;

