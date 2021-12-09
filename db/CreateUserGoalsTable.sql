CREATE TABLE IF NOT EXISTS User_Goals
             (
                          id              INTEGER NOT NULL AUTO_INCREMENT,
                          _id             INTEGER NOT NULL,
                          Goal            VARCHAR(30) NOT NULL,
                          Date_Started    VARCHAR(50) NOT NULL,
                          Date_Endgoal    VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `User_Goals` WRITE;
/*!40000 ALTER TABLE `User_Goals` DISABLE KEYS */;
INSERT INTO `User_Goals` VALUES (1,1,'Finish project work','06/12/2021','10/12/2021'),(2,2,'Revise for AZ900 test','05/12/2021','15/12/2021');
/*!40000 ALTER TABLE `User_Goals` ENABLE KEYS */;
UNLOCK TABLES;