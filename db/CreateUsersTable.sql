CREATE TABLE IF NOT EXISTS Users
             (
                          id              INTEGER NOT NULL AUTO_INCREMENT,
                          full_name       VARCHAR(30) NOT NULL,
                          email           VARCHAR(50) NOT NULL,
                          user_password   VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Ben','test@test7.com','password'),(2,'Luke','test@test.com','password2');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;