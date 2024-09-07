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


-- add people
INSERT INTO people
(name)
VALUES
('Giuseppe'),
('Adriana'),
('Dalia'),
('Armando'),
('Riccardo'),
('Giovanni'),
('Francesco'),
('Maria Angela'),
('Galadriel'),
('Elinor');


-- add tribes
INSERT INTO tribes
(name)
VALUES
('Micenei'),
('Sumeri'),
('Etruschi'),
('Bruzi'),
('Occitani'),
('Franchi'),
('Sassoni'),
('Iberici'),
('Romani'),
('Galli');


-- add members 
INSERT INTO people_tribes
(person_id, tribe_id, join_date)
VALUES
(1, 3, '2024-09-01'),
(2, 5, '2024-09-02'),
(5, 3, '2024-09-03'),
(4, 5, '2024-09-04'),
(6, 3, '2024-09-05'),
(5, 2, '2024-09-06'),
(2, 3, '2024-09-07'),
(3, 2, '2024-09-08'),
(6, 6, '2024-09-09'),
(6, 5, '2024-09-10'),
(7, 2, '2024-09-11'),
(3, 6, '2024-09-12'),
(7, 7, '2024-09-12'),
(8, 1, '2024-09-12'),
(8, 4, '2024-09-12'),
(7, 4, '2024-09-12');
