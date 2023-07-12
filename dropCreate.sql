
DROP TABLE IF EXISTS `characters`;
DROP TABLE IF EXISTS `player`;
DROP TABLE IF EXISTS `game`;
DROP TABLE IF EXISTS `player_game`;
DROP TABLE IF EXISTS `player_attendance`;
DROP TABLE IF EXISTS `tournament`;
DROP TABLE IF EXISTS `club_officer`;

--SET FOREIGN_KEY_CHECKS = 1;



-- create all tables with primary and foreign key constraints.
-- Table: characters
CREATE TABLE characters (
	CharacterNumber int NOT NULL,
	CharacterName tinytext,
	PRIMARY KEY (CharacterNumber)
);

-- Table: player
CREATE TABLE player (
	ComputingID tinytext NOT NULL,
	FirstName tinytext,
	LastName tinytext,
	ScreenName tinytext,
	SchoolYear int,
	CharacterNumber int,
	PRIMARY KEY (ComputingID),
	FOREIGN KEY (CharacterNumber) REFERENCES characters(CharacterNumber)
);

-- Table: game
CREATE TABLE game (
	GameID int NOT NULL,
	Duration int,
	Winner tinytext,
	Loser tinytext,
	TourneyNum int,
	PRIMARY KEY (GameID),
	FOREIGN KEY (TourneyNum) REFERENCES tournament(TourneyNum),
	FOREIGN KEY (Winner) REFERENCES player(ComputingID),
	FOREIGN KEY (Loser) REFERENCES player(ComputingID)
);

-- Table: player_attendance
CREATE TABLE player_attendance (
	PlayerAttendanceID int NOT NULL,
	ComputingID tinytext,
	TourneyNum int,
	PRIMARY KEY (PlayerAttendanceID),
	FOREIGN KEY (ComputingID) REFERENCES player(ComputingID),
	FOREIGN KEY (TourneyNum) REFERENCES tournament(TourneyNum)
);

-- Table: tournament
CREATE TABLE tournament (
	TourneyNum int NOT NULL,
	Participants int,
	TourneyDate DATE,
	Location tinytext,
	FirstPlace tinytext,
	SecondPlace tinytext,
	ThirdPlace tinytext,
	OfficerID int,
	PRIMARY KEY (TourneyNum)
	FOREIGN KEY (OfficerID) REFERENCES club_officer(OfficerID)
	);

-- Table: club_officer
CREATE TABLE club_officer (
        OfficerID int NOT NULL,
	ComputingID tinytext,	     
	FirstName tinytext,
	LastName tinytext,
	Number tinytext,
	Email tinytext,
	SchoolYear int,
	PRIMARY KEY (OfficerID),
	FOREIGN KEY (ComputingID) REFERENCES player(ComputingID)
);
