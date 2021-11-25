-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: aser
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity` (
  `time` datetime NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

LOCK TABLES `activity` WRITE;
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES ('2021-11-20 18:00:00','2021ASer冬日祭'),('2022-05-23 21:01:37','ASer春日祭');
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `name` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `Authority` int NOT NULL DEFAULT '3',
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('RT','pbkdf2:sha256:260000$MCJrNGSvKFZlBtTK$17ba8da28d66effdd1a855132e0b4e6337ac49a426a58d4e5dd9ab2ccee83346',0,1);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anime_news`
--

DROP TABLE IF EXISTS `anime_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anime_news` (
  `name` varchar(50) DEFAULT NULL,
  `index` int NOT NULL AUTO_INCREMENT,
  `content` text,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `img_path` varchar(60) DEFAULT NULL,
  `img_path_small` varchar(80) DEFAULT NULL,
  `introduction` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`index`),
  UNIQUE KEY `anime_news_index_uindex` (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anime_news`
--

LOCK TABLES `anime_news` WRITE;
/*!40000 ALTER TABLE `anime_news` DISABLE KEYS */;
INSERT INTO `anime_news` VALUES ('「罗宾」第10期变体封面公开',1,'\n        <section className=\"atl\">\n            <div className=\"article\">\n                <div className=\"hd\">\n                    <h1 className=\"title\">\n                        「罗宾」第10期变体封面公开\n                    </h1>\n                    <div className=\"info\">\n   <span className=\"tag\">\n    动漫\n   </span>\n                        <span className=\"author\">资讯速递</span>\n                        <span className=\"ico\">\n    ▪\n   </span>\n                        <span className=\"time\">\n    2021-11-12 15:03:22\n   </span>\n                    </div>\n                </div>\n                <div className=\"bd\">\n                    <p>原文出处：<a rel=\"nofollow\" href=\"http://acg.178.com/202111/430700602839.html\" target=\"_blank\">http://acg.178.com/202111/430700602839.html</a>\n                    </p>\n\n                    <p>\n                        近日，DC漫画公开了「罗宾」第10期的变体封面，此次变体封面由画师Nikola Čižmešija独家绘制，登场人物为「罗宾」。本期将于2021年1月发布。\n                    </p>\n                    <p style=\"text-align:center\">\n                        <img alt=\"\" referrerPolicy=\"no-referrer\"\n                             src=\"https://pic.rmb.bdstatic.com/bjh/d5f21ef104891a3113afd3f725b81faa.jpeg\"/>\n                    </p>\n                </div>\n            </div>\n\n        </section>\n','2021-11-12','15:03:22','../static/images/news/1big.png','../static/images/news/1small.jpeg','请大家点击查看'),('Fate Zero开播十周年纪念插画介绍PV',2,'<section class=\"atl\">\n              <div class=\"article\">\n <div class=\"hd\">\n  <h1 class=\"title\">\n   「Fate/Zero」开播十周年纪念插画介绍PV公开\n  </h1>\n  <div class=\"info\">\n   <span class=\"tag\">\n    动漫\n   </span>\n   <span class=\"author\">资讯速递</span>\n   <span class=\"ico\">\n    ▪\n   </span>\n   <span class=\"time\">\n    2021-11-12 14:47:29\n   </span>\n  </div>\n </div>\n <div class=\"bd\">\n<p>原文出处：<a rel=\"nofollow\" href=\"http://acg.178.com/202111/430699649128.html\" target=\"_blank\">http://acg.178.com/202111/430699649128.html</a></p>\n\n  <p>\n   ufotable官方公开了动画「Fate/Zero」开播十周年纪念插画介绍PV。十周年特别企划将贩售包括Q版角色亚力克板、角色与场景原画线稿、角色勋章等周边。\n  </p>\n  <p style=\"text-align: center;\">\n   <a href=\"https://www.bilibili.com/video/BV14h411t718\" rel=\"nofollow\">\n    动画「Fate/Zero」开播十周年纪念插画介绍PV\n   </a>\n  </p>\n  <p style=\"text-align:center\">\n   <img alt=\"\" referrerpolicy=\"no-referrer\" src=\"https://pic.rmb.bdstatic.com/bjh/3353759c09027280250dbb7be0e87a71.jpeg\"/>\n  </p>\n  <p style=\"text-align:center\">\n   <img alt=\"\" referrerpolicy=\"no-referrer\" src=\"https://pic.rmb.bdstatic.com/bjh/debb16cb54fce1b643f82a67b9f6d60d.jpeg\"/>\n  </p>\n  <p style=\"text-align:center\">\n   <img alt=\"\" referrerpolicy=\"no-referrer\" src=\"https://pic.rmb.bdstatic.com/bjh/465d025b6a00402eb11f2fc7606e347e.jpeg\"/>\n  </p>\n  <p style=\"text-align:center\">\n  </p>\n  <p>\n   「Fate/Zero」是根据TYPE-MOON旗下「Fate」系列游戏改编的电视动画，由ufotable制作。本作讲述了冬木市聚集了众多英灵而开展的圣杯之战，故事线位于动画「Fate/Stay Night」之前。\n  </p>\n </div>\n</div>\n\n            </section>','2021-11-12','14:47:29','../static/images/news/2big.png','../static/images/news/2small.png','请大家点击查看'),('U35「白沙的水族馆」新绘公开',4,'<section class=\"atl\">\n              <div class=\"article\">\n <div class=\"hd\">\n  <h1 class=\"title\">\n   U35「白沙的水族馆」新绘公开\n  </h1>\n  <div class=\"info\">\n   <span class=\"tag\">\n    动漫\n   </span>\n   <span class=\"author\">资讯速递</span>\n   <span class=\"ico\">\n    ▪\n   </span>\n   <span class=\"time\">\n    2021-11-12 12:01:40\n   </span>\n  </div>\n </div>\n <div class=\"bd\">\n<p>原文出处：<a rel=\"nofollow\" href=\"http://acg.178.com/202111/430689700026.html\" target=\"_blank\">http://acg.178.com/202111/430689700026.html</a></p>\n\n  <p>\n   近日，TV动画「白沙的水族馆」角色原案的插画师U35老师公开了最新绘制。\n  </p>\n  <p style=\"text-align:center\">\n   <img alt=\"\" referrerpolicy=\"no-referrer\" src=\"https://pic.rmb.bdstatic.com/bjh/1d3853c9962f4fe38ba861240da88f45.jpeg\"/>\n  </p>\n  <p>\n   同时，插画师U35老师还公开了第19话的应援绘。\n  </p>\n  <p style=\"text-align:center\">\n   <img alt=\"\" referrerpolicy=\"no-referrer\" src=\"https://pic.rmb.bdstatic.com/bjh/2c4b2ae5a268b22969f1f212806b55a2.jpeg\"/>\n  </p>\n  <p>\n   「白沙水族馆」以冲绳南城市的一家将要闭馆的海洋馆为舞台，讲述了代理馆长海咲野括和在东京失去了梦想的原偶像宫泽风花相遇后发生的故事。\n  </p>\n </div>\n</div>\n\n            </section>\n','2021-11-12','12:01:40','../static/images/news/3big.png','../static/images/news/3small.jpeg','请大家点击查看');
/*!40000 ALTER TABLE `anime_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `name` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `id` int DEFAULT NULL,
  `message` varchar(600) DEFAULT NULL,
  `avatar` varchar(50) DEFAULT '../static/images/gravatar.png',
  `index_` int NOT NULL AUTO_INCREMENT,
  `type` int DEFAULT NULL,
  PRIMARY KEY (`index_`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES ('2','280844012@qq.com',1,'..','../static/images/avatar/1.png',1,1),('RT','280844012@qq.com',1,'这是ASer动漫社','../static/images/avatar/2.png',2,1),('RTzld','ayjadxlz@mails.jlnu.edu.cn',1,'wu','../static/images/avatar/16.png',3,1),('RTzld','ayjadxlz@mails.jlnu.edu.cn',1,'wu','../static/images/avatar/16.png',4,1),('h598','1741346659@qq.com',1,'22255','../static/images/avatar/11.png',5,1),('h598','1741346659@qq.com',1,'22255','../static/images/avatar/11.png',6,1),('RTzld','280844012@qq.con',2,'22211','../static/images/avatar/8.png',7,1),('RTzld','280844012@qq.con',2,'22211','../static/images/avatar/8.png',8,1),('RTzld','2300746003@qq.com',1,'qqqq','../static/images/avatar/19.png',9,1),('RTzld','2300746003@qq.com',1,'qqqq','../static/images/avatar/19.png',10,1),('王昊','2300746003@qq.com',1,'111222','../static/images/avatar/19.png',11,1),('王昊','280844012@qq.com',1,'553348uij','../static/images/avatar/1.png',12,1),('王昊','2300746003@qq.com',1,'667822','../static/images/avatar/19.png',13,1),('gxr','2659307910@qq.com',1,'我是憨憨！！！','../static/images/avatar/1.png',14,1),('王昊','280844012@qq.com',1,'2assdaasdasdx','../static/images/avatar/1.png',15,1),('1222','2166093656@qq.com',1,'11122w1','../static/images/avatar/14.png',16,1),('RTzld','2300746003@qq.com',3,'121221','../static/images/avatar/19.png',17,1),('RTzld','1741346659@qq.com',1,'6666666','../static/images/avatar/14.png',18,2),('RT','280844012@qq.com',1,'暂无','../static/images/avatar/1.png',19,1),('yy','2602125@qq.com',2,'wu','../static/images/avatar/2.png',20,2),('王昊','280844012@qq.com',3,'52125','../static/images/avatar/1.png',21,1);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `name` varchar(30) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `content` varchar(600) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `img_path` varchar(50) DEFAULT '../static/images/none.png',
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`name`),
  UNIQUE KEY `events_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES ('2021冬日祭','7501','无','2021-11-20','18:00:00','../static/images/none.png',3),('2021冬日祭排练','11307','无','2021-11-06','13:00:00','../static/images/none.png',1),('wu','11307','wu','2021-11-07','12:00:00','../static/images/none.png',2),('春日','7501','暂无','2022-06-02','12:04:00','../static/images/event/5.jpg',4);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minister`
--

DROP TABLE IF EXISTS `minister`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `minister` (
  `name` varchar(20) NOT NULL,
  `img_path` varchar(50) DEFAULT '../static/images/none.png',
  `department` varchar(10) DEFAULT NULL,
  `introduction` varchar(600) DEFAULT NULL,
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minister`
--

LOCK TABLES `minister` WRITE;
/*!40000 ALTER TABLE `minister` DISABLE KEYS */;
INSERT INTO `minister` VALUES ('日天','../static/images/temp/staff-img-1.jpg','后期','淞淞的老父亲，淞淞已经欠了好几次女装了，日天一直想知道他该怎么解决问题',5),('淞淞','../static/images/temp/staff-img-2.jpg','社长','犯下了傲慢之罪，不能完成我们大家的心愿',1),('小西','../static/images/none.png','宅舞','淞淞的一生之敌',2),('情陌','../static/images/member/6.jpg','后勤','wu1',4),('方方','../static/images/member/saturation.png','后勤','暂无',4);
/*!40000 ALTER TABLE `minister` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `story`
--

DROP TABLE IF EXISTS `story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `story` (
  `name` varchar(30) DEFAULT NULL,
  `img_path` varchar(60) DEFAULT NULL,
  `content` text,
  `index` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`index`),
  UNIQUE KEY `story_index_uindex` (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story`
--

LOCK TABLES `story` WRITE;
/*!40000 ALTER TABLE `story` DISABLE KEYS */;
INSERT INTO `story` VALUES ('2018','../static/images/story/2018.JPG','无\n',1),('2019','../static/images/story/2019.jpg','无',2),('2020','../static/images/story/2020.jpg','无',3),('1','../static/images/story/1.jpg','无',4),('2','../static/images/story/2.jpeg','无',5),('3','../static/images/story/3.jpg','无',6),('4','../static/images/story/4.jpeg','无',7),('5','../static/images/story/5.jpg','无',8),('6','../static/images/story/6.jpeg','无',9);
/*!40000 ALTER TABLE `story` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suggestion`
--

DROP TABLE IF EXISTS `suggestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suggestion` (
  `index` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `message` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suggestion`
--

LOCK TABLES `suggestion` WRITE;
/*!40000 ALTER TABLE `suggestion` DISABLE KEYS */;
INSERT INTO `suggestion` VALUES (12,'RTzld','2300746003@qq.com','111s'),(13,'王昊','2300746003@qq.com','2255'),(14,'12138','3618386561@qq.com','2222'),(15,'王昊','280844012@qq.com','111saAW`11'),(16,'帅气的崔杰','michaelchui007@gmail.com','崔杰好帅哦！！！'),(17,'帅气的崔杰','michaelchui007@gmail.com','崔杰好帅哦！！！'),(18,'RTzld','280844012@qq.com','52112'),(19,'王昊','280844012@qq.com','asdsdds'),(20,'王昊','280844012@qq.com','1122121'),(21,'王昊','280844012@qq.com','550255');
/*!40000 ALTER TABLE `suggestion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-25  8:45:48
