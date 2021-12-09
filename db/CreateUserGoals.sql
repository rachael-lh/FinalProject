CREATE TABLE IF NOT EXISTS usergoals
             (
                          id              INTEGER NOT NULL AUTO_INCREMENT,
                          userid          INTEGER, 
                          goals           VARCHAR(30) NOT NULL,
                          date_started    VARCHAR(50) NOT NULL,
                          date_endgoal    VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id),
                          FOREIGN KEY (userid) REFERENCES users(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `usergoals` WRITE;
/*!40000 ALTER TABLE `usergoals` DISABLE KEYS */;
INSERT INTO `usergoals` VALUES (1,1,'Hello','12/15/2021','11/12/2021'),(2,2,'Bye','Monday','Friday');
/*!40000 ALTER TABLE `usergoals` ENABLE KEYS */;
UNLOCK TABLES;