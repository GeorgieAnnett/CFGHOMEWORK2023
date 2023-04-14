### QUESTION 1


```` 
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info(
movie_ID INT,
movie_name VARCHAR(50),
movie_length VARCHAR(50),
age_rating VARCHAR(5),
PRIMARY KEY(Movie_ID)
);

drop table movie_info;

CREATE TABLE screens (
Screen_ID INT,
Four_K BOOLEAN
);

CREATE TABLE showings (
Showing_ID INT,
Movie_ID INT,
Screen_ID INT,
Start_Time VARCHAR(50),
Available_Seats INT
);

drop table showings;

```` 
### QUESTION 2

```` 
USE foundation_assessment_ii;

 INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
 VALUES 
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");
 
 INSERT INTO screens(screen_ID, four_k)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);
  
 INSERT INTO showings(showing_ID, movie_ID,screen_ID, start_time, available_seats)
 VALUES 
  (1, 1, 2, '12:00:00', 10), 
  (2, 1, 2, '17:00:00', 23), 
  (3, 2, 9, '10:30:00', 30), 
  (4, 3, 1, '07:00:00', 38), 
  (5, 3, 5, '10:00:00', 26), 
  (6, 3, 1, '17:00:00', 5), 
  (7, 3, 1, '19:00:00', 0), 
  (8, 3, 5, '14:00:00', 2), 
  (9, 4, 9, '20:00:00', 14), 
  (10, 4, 9, '23:00:00', 23), 
  (11, 5, 6, '09:30:00', 30), 
  (12, 5, 6, '12:30:00', 7), 
  (13, 5, 6, '14:30:00', 0), 
  (14, 5, 6, '15:20:00', 0), 
  (15, 6, 10, '10:00:00', 32), 
  (16, 6, 10, '13:30:00', 25), 
  (17, 6, 10, '17:00:00', 14), 
  (18, 7, 7, '12:00:00', 36), 
  (19, 8, 4, '15:00:00', 24), 
  (20, 9, 3, '17:00:00', 0);

SELECT m.movie_name, s.Start_Time
FROM showings as s 
INNER JOIN movie_info as m
ON s.Movie_ID = m.movie_id
WHERE start_time >'12:00:00' AND available_seats >= 1
ORDER BY s.Start_Time;

```` 
### QUESTION 3
```` 
SELECT m.movie_name 
FROM movie_info AS m
INNER JOIN showings AS s 
ON m.movie_id = s.movie_id
GROUP BY m.movie_name
HAVING COUNT(*) = (
SELECT COUNT(*) 
FROM showings
GROUP BY movie_id
ORDER BY COUNT(*) DESC
LIMIT 1
);


````