CREATE TABLE people (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE tribes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

-- this table is a combination of people and tribes,
-- which can be interpreted as members
-- so one person can be belong to many tribes,
-- and one tribe can have many people 
CREATE TABLE people_tribes (
    -- it cannot be null because 
    -- if the member exists, then a specific person
    -- must exist
    person_id INT NOT NULL,
    tribe_id INT NOT NULL,
    join_date DATE,
    PRIMARY KEY (person_id, tribe_id),
    -- when the person is deleted, delete all the members
    -- associated to that person
    FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    -- when the tribe is deleted, delete all the members
    -- associated to that tribe
    FOREIGN KEY (tribe_id) REFERENCES tribes(id) ON DELETE CASCADE
);
