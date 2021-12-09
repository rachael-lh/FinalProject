CREATE TABLE IF NOT EXISTS users
             (
                          full_name       VARCHAR(30) NOT NULL,
--                         email           VARCHAR(50) NOT NULL,
                          user_password   VARCHAR(150) NOT NULL,
                          PRIMARY KEY (full_name)
--                          UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Ben','password'),('Luke','password2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;