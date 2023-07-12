-- Table: character 
INSERT INTO characters
VALUES (1, 'Bayonetta');
INSERT INTO characters
VALUES (2, 'Ness');
INSERT INTO characters
VALUES (3, 'Steve');
INSERT INTO characters
VALUES (4, 'Sora');
INSERT INTO characters
VALUES (5, 'Bowser');
INSERT INTO characters
VALUES (6, 'Random');
INSERT INTO characters
VALUES (7, 'Link');
INSERT INTO characters
VALUES (8, 'Hero');
INSERT INTO characters
VALUES (9, 'Rob');
INSERT INTO characters
VALUES (10, 'Cloud');


-- Table: player
INSERT INTO player
VALUES ('jtg8se', 'Jordan', 'Goode', 'jordan456',4,1);
INSERT INTO player
VALUES ('sg2vp', 'Shourya','Gupta','majutsushi',3,2);
INSERT INTO player
VALUES ('eh2vu', 'Ethan','Hartley','ethan',4,3);
INSERT INTO player
VALUES ('sh3rt', 'Sophia', 'Harrington', 'sophie',2,4);
INSERT INTO player
VALUES ('bw2yz', 'Benjamin','Walker','benji',3,5);
INSERT INTO player
VALUES ('om5wt', 'Olivia','Morgan','olivia',2,6);
INSERT INTO player
VALUES ('gl3tp', 'Gabriel', 'Lawson', 'gabby',1,7);
INSERT INTO player
VALUES ('aw5pr', 'Ava','West','ava22',2,8);
INSERT INTO player
VALUES ('np8rq', 'Noah','Price','noah',3,9);
INSERT INTO player
VALUES ('joan', 'Joan','Darwin','joan',3,10);

-- Table: game
INSERT INTO game 
VALUES (123, 60, 'jtg8se','jgk2qq',1);
INSERT INTO game 
VALUES (124, 60, 'joan','jgk2qq',1);
INSERT INTO game 
VALUES (125, 60, 'jtg8se','joan',2);

INSERT INTO game
VALUES (126, 60, 'aw5pr','jgk2qq',2);
INSERT INTO game
VALUES (127, 60, 'np8rq','sg2vp',3);
INSERT INTO game
VALUES (128, 60, 'jtg8se','bw2yz',3);
INSERT INTO game
VALUES (129, 60, 'np8rq','jgk2qq',4);
INSERT INTO game
VALUES (130, 60, 'eh2vu','sg2vp',4);
INSERT INTO game
VALUES (131, 60, 'np8rq','joan',1);
INSERT INTO game
VALUES (132, 60, 'aw5pr','jgk2qq',2);
INSERT INTO game
VALUES (133, 60, 'joan','jgk2qq',3);
INSERT INTO game
VALUES (134, 60, 'bw2yz','joan',4);




-- Table: tournament
INSERT INTO tournament 
VALUES (1, 20, '2023-7-1','Rice Hall','jtg8se','bw2yz','jgk2qq',1);
INSERT INTO tournament 
VALUES (2, 20, '2023-7-8','Newcomb','np8rq','jtg8se','joan',1);
INSERT INTO tournament
VALUES (3, 20, '2023-6-10','Rice Hall','jtg8se','eh2vu','jgk2qq',1);
INSERT INTO tournament
VALUES (4, 20, '2023-6-17','Olsson Hall','jgk2qq','aw5pr','sg2vp',1);

-- Table: club_officer
INSERT INTO club_officer
VALUES (1, 'jtg8se', 'Jordan','Goode','4345551234','jtg8se@virginia.edu',4);

-- Table: player_attendance
INSERT INTO player_attendance
VALUES (1, 'jgk2qq', 1);
INSERT INTO player_attendance
VALUES (2, 'jtg8se',1);
INSERT INTO player_attendance
VALUES (3, 'joan',1);
INSERT INTO player_attendance
VALUES (4, 'jgk2qq',2);
INSERT INTO player_attendance
VALUES (5, 'jtg8se',2);
INSERT INTO player_attendance
VALUES (6, 'joan',2);
