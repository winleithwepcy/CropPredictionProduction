-- SQLite
CREATE TABLE surveydata (
id INTEGER PRIMARY KEY NOT NULL,
soiltype CHAR(150),
croptype CHAR(150),
seedquality CHAR(150),
seedrate INTEGER,
fertilizertype CHAR(150),
manuretype CHAR(150),
landpreparation CHAR(150),
sowingtype CHAR(150),
fertilizeramt INTEGER,
herbicideamt  INTEGER,
insecticideamt INTEGER,
manureamt INTEGER,
address CHAR(150)
);

ALTER TABLE surveydata
RENAME TO survey;

 