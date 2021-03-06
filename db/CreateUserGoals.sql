CREATE TABLE IF NOT EXISTS usergoals
             (
                          id              INTEGER NOT NULL AUTO_INCREMENT,
                          goals           VARCHAR(100) NOT NULL,
                          date_started    VARCHAR(50) NOT NULL,
                          date_endgoal    VARCHAR(150) NOT NULL,
                          username        VARCHAR(30) NOT NULL,
                          PRIMARY KEY (id),
                          FOREIGN KEY (username) REFERENCES users(full_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `usergoals` WRITE;
/*!40000 ALTER TABLE `usergoals` DISABLE KEYS */;
INSERT INTO `usergoals` VALUES (1,'Create jenkins docker image','01/12/2021','07/12/2021','Ben'),(2,'Finish project','10/11/2021','10/12/2021','Luke');
/*!40000 ALTER TABLE `usergoals` ENABLE KEYS */;
UNLOCK TABLES;