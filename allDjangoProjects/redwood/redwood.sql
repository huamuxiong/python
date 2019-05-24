/*
 Navicat Premium Data Transfer

 Source Server         : leyton
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : redwood

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 17/05/2019 15:23:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for advice
-- ----------------------------
DROP TABLE IF EXISTS `advice`;
CREATE TABLE `advice`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `nickname` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `reversion` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `advice_user_id_74b39147_fk_users_id`(`user_id`) USING BTREE,
  CONSTRAINT `advice_user_id_74b39147_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add 家具', 7, 'add_redwood');
INSERT INTO `auth_permission` VALUES (26, 'Can change 家具', 7, 'change_redwood');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 家具', 7, 'delete_redwood');
INSERT INTO `auth_permission` VALUES (28, 'Can view 家具', 7, 'view_redwood');
INSERT INTO `auth_permission` VALUES (29, 'Can add 用户建议', 8, 'add_useradvice');
INSERT INTO `auth_permission` VALUES (30, 'Can change 用户建议', 8, 'change_useradvice');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 用户建议', 8, 'delete_useradvice');
INSERT INTO `auth_permission` VALUES (32, 'Can view 用户建议', 8, 'view_useradvice');
INSERT INTO `auth_permission` VALUES (33, 'Can add 收藏', 9, 'add_usercollect');
INSERT INTO `auth_permission` VALUES (34, 'Can change 收藏', 9, 'change_usercollect');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 收藏', 9, 'delete_usercollect');
INSERT INTO `auth_permission` VALUES (36, 'Can view 收藏', 9, 'view_usercollect');
INSERT INTO `auth_permission` VALUES (37, 'Can add 评论', 10, 'add_usercomment');
INSERT INTO `auth_permission` VALUES (38, 'Can change 评论', 10, 'change_usercomment');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 评论', 10, 'delete_usercomment');
INSERT INTO `auth_permission` VALUES (40, 'Can view 评论', 10, 'view_usercomment');
INSERT INTO `auth_permission` VALUES (41, 'Can add 浏览记录', 11, 'add_userhistroy');
INSERT INTO `auth_permission` VALUES (42, 'Can change 浏览记录', 11, 'change_userhistroy');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 浏览记录', 11, 'delete_userhistroy');
INSERT INTO `auth_permission` VALUES (44, 'Can view 浏览记录', 11, 'view_userhistroy');
INSERT INTO `auth_permission` VALUES (45, 'Can add 用户', 12, 'add_users');
INSERT INTO `auth_permission` VALUES (46, 'Can change 用户', 12, 'change_users');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 用户', 12, 'delete_users');
INSERT INTO `auth_permission` VALUES (48, 'Can view 用户', 12, 'view_users');
INSERT INTO `auth_permission` VALUES (49, 'Can add 新闻资讯', 13, 'add_newsinformation');
INSERT INTO `auth_permission` VALUES (50, 'Can change 新闻资讯', 13, 'change_newsinformation');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 新闻资讯', 13, 'delete_newsinformation');
INSERT INTO `auth_permission` VALUES (52, 'Can view 新闻资讯', 13, 'view_newsinformation');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$120000$7S06szDDVVbp$KEcclHTqgPmNh33cjkEuFYgIxOKP/nAt/Z7GL6aQCrs=', '2019-04-26 14:50:08.851248', 1, 'admin', '', '', 'admin@163.com', 1, 1, '2019-04-24 10:30:56.669578');
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$120000$9tDWisuehMv7$6LZuBGs8d4IDS5fRqfdejoZYnfgo3ERX77Z72MQQslA=', NULL, 0, 'goudan', '小秘huangxinxing', '阿黄', 'ahuang@163.com', 1, 1, '2019-04-26 15:02:00.000000');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES (2, 2, 13);
INSERT INTO `auth_user_user_permissions` VALUES (3, 2, 25);
INSERT INTO `auth_user_user_permissions` VALUES (4, 2, 27);
INSERT INTO `auth_user_user_permissions` VALUES (5, 2, 31);
INSERT INTO `auth_user_user_permissions` VALUES (1, 2, 38);

-- ----------------------------
-- Table structure for collection
-- ----------------------------
DROP TABLE IF EXISTS `collection`;
CREATE TABLE `collection`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `redwood_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `collection_redwood_id_878f5ea6_fk_redwood_id`(`redwood_id`) USING BTREE,
  INDEX `collection_user_id_e8aa841d_fk_users_id`(`user_id`) USING BTREE,
  CONSTRAINT `collection_redwood_id_878f5ea6_fk_redwood_id` FOREIGN KEY (`redwood_id`) REFERENCES `redwood` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `collection_user_id_e8aa841d_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `satisfied` int(11) NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `redwood_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `comment_redwood_id_337d2f52_fk_redwood_id`(`redwood_id`) USING BTREE,
  INDEX `comment_user_id_2224f9d1_fk_users_id`(`user_id`) USING BTREE,
  CONSTRAINT `comment_redwood_id_337d2f52_fk_redwood_id` FOREIGN KEY (`redwood_id`) REFERENCES `redwood` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `comment_user_id_2224f9d1_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2019-04-24 11:14:02.813217', '1', '三季度房价高', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2019-04-24 12:01:26.487550', '1', '三季度房价高', 2, '[{\"changed\": {\"fields\": [\"img\"]}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (3, '2019-04-24 12:05:47.954636', '1', '疾控中心不覆盖', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (4, '2019-04-24 19:18:06.466958', '2', '输入对方过后', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (5, '2019-04-25 17:38:05.359267', '3', 'zhangsan1', 2, '[{\"changed\": {\"fields\": [\"isActive\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (6, '2019-04-25 17:42:46.723605', '3', 'zhangsan1', 2, '[{\"changed\": {\"fields\": [\"isActive\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (7, '2019-04-25 17:43:05.182580', '3', 'zhangsan1', 2, '[{\"changed\": {\"fields\": [\"isActive\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (8, '2019-04-26 15:02:56.715568', '2', 'goudan', 1, '[{\"added\": {}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (9, '2019-04-26 15:04:42.768065', '2', 'goudan', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"is_staff\", \"user_permissions\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (10, '2019-04-26 15:06:50.366655', '2', 'goudan', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (11, '2019-04-26 21:21:03.474919', '9', '说的话是的发挥各自ＺＸＣ', 2, '[{\"changed\": {\"fields\": [\"reversion\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (12, '2019-04-26 22:38:20.063656', '9', '说的话是的发挥各自ＺＸＣ', 2, '[{\"changed\": {\"fields\": [\"reversion\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (13, '2019-04-26 23:11:29.464896', '8', '说的话是的发挥各自还不知道v吧不知道从ＥＲ', 2, '[{\"changed\": {\"fields\": [\"reversion\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (14, '2019-04-26 23:11:40.926273', '2', '是豆腐干地方', 2, '[{\"changed\": {\"fields\": [\"reversion\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (15, '2019-04-26 23:54:12.492314', '1', '的发过火发过火', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (16, '2019-04-27 00:21:02.805628', '1', '的发过火发过火对方过后是法国恢复规划法规发过火发过火是否更换是否更换是否更换是否更换', 2, '[{\"changed\": {\"fields\": [\"title\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (17, '2019-04-27 00:29:05.876516', '2', '德国大夫', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (18, '2019-04-27 00:29:15.198782', '3', '大风歌', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (19, '2019-04-27 00:29:26.308546', '4', '大风歌大风歌', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (20, '2019-04-27 00:29:38.274163', '5', '大发横财v', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (21, '2019-04-27 00:29:50.872064', '6', '挖是否', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (22, '2019-04-27 00:30:09.368558', '7', 'GGHJGHJB', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (23, '2019-04-27 00:30:16.978517', '8', 'ASFZX', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (24, '2019-04-27 00:35:00.486092', '9', '是大法官的', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (25, '2019-04-27 00:35:18.633046', '10', '撒地方为', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (26, '2019-04-27 00:35:31.107248', '11', '撒地方是否s', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (27, '2019-04-27 00:35:37.382923', '11', '撒地方是否sSDF', 2, '[{\"changed\": {\"fields\": [\"title\", \"content\", \"author\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (28, '2019-04-27 00:35:58.034245', '12', 'SDF', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (29, '2019-04-27 00:36:05.831187', '13', 'SDFH', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (30, '2019-04-27 00:36:12.701802', '14', 'WRT', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (31, '2019-04-27 00:36:20.531617', '15', 'REURTYEUTRYU', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (32, '2019-04-27 00:36:28.855740', '16', 'ASDGDFG', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (33, '2019-04-27 00:36:34.834689', '17', 'SDHGFDGHFD', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (34, '2019-04-27 00:36:43.473522', '18', 'ADGSDFG', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (35, '2019-04-27 00:36:51.103131', '19', 'RTZDF346RASDF', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (36, '2019-04-27 00:37:00.135534', '20', 'ERES', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (37, '2019-04-27 00:37:12.201600', '21', 'SADFG', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (38, '2019-04-27 01:01:10.798927', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"title\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (39, '2019-04-27 11:31:38.852594', '1', '的发过火发过火对方过后是法国恢复规划法规发过火发过火是否更换是否更换是否更换是否更换', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (40, '2019-04-27 11:43:40.883008', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (41, '2019-04-27 11:44:39.921270', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (42, '2019-04-27 11:48:47.064306', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (43, '2019-04-27 11:52:20.981524', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (44, '2019-04-27 11:52:42.928624', '21', 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (45, '2019-04-27 12:00:03.174860', '1', '的发过火发过火对方过后是法国恢复规划法规发过火发过火是否更换是否更换是否更换是否更换', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 13, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (13, 'index', 'newsinformation');
INSERT INTO `django_content_type` VALUES (7, 'index', 'redwood');
INSERT INTO `django_content_type` VALUES (8, 'index', 'useradvice');
INSERT INTO `django_content_type` VALUES (9, 'index', 'usercollect');
INSERT INTO `django_content_type` VALUES (10, 'index', 'usercomment');
INSERT INTO `django_content_type` VALUES (11, 'index', 'userhistroy');
INSERT INTO `django_content_type` VALUES (12, 'index', 'users');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-04-24 10:29:00.455875');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2019-04-24 10:29:08.162381');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2019-04-24 10:29:09.821342');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2019-04-24 10:29:09.870016');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-24 10:29:09.909630');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2019-04-24 10:29:10.892986');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2019-04-24 10:29:11.531874');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2019-04-24 10:29:12.159702');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2019-04-24 10:29:12.203012');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2019-04-24 10:29:12.865280');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2019-04-24 10:29:12.919072');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2019-04-24 10:29:12.982933');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2019-04-24 10:29:13.656859');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2019-04-24 10:29:14.353633');
INSERT INTO `django_migrations` VALUES (15, 'index', '0001_initial', '2019-04-24 10:29:21.772297');
INSERT INTO `django_migrations` VALUES (16, 'sessions', '0001_initial', '2019-04-24 10:29:22.364042');
INSERT INTO `django_migrations` VALUES (17, 'index', '0002_auto_20190424_1156', '2019-04-24 11:56:32.676177');
INSERT INTO `django_migrations` VALUES (18, 'index', '0003_redwood_state', '2019-04-24 12:18:37.012864');
INSERT INTO `django_migrations` VALUES (19, 'index', '0004_auto_20190424_1858', '2019-04-24 18:58:14.657353');
INSERT INTO `django_migrations` VALUES (20, 'index', '0005_auto_20190424_1901', '2019-04-24 19:01:24.257204');
INSERT INTO `django_migrations` VALUES (21, 'index', '0006_auto_20190424_1917', '2019-04-24 19:17:20.154917');
INSERT INTO `django_migrations` VALUES (22, 'index', '0007_auto_20190425_1529', '2019-04-25 15:29:16.770188');
INSERT INTO `django_migrations` VALUES (23, 'index', '0008_auto_20190425_2258', '2019-04-25 22:58:21.417305');
INSERT INTO `django_migrations` VALUES (24, 'index', '0009_auto_20190426_1224', '2019-04-26 12:24:13.597089');
INSERT INTO `django_migrations` VALUES (25, 'index', '0010_auto_20190426_1735', '2019-04-26 17:36:08.625617');
INSERT INTO `django_migrations` VALUES (26, 'index', '0011_auto_20190426_2040', '2019-04-26 20:40:27.925480');
INSERT INTO `django_migrations` VALUES (27, 'index', '0012_auto_20190426_2041', '2019-04-26 20:41:21.502256');
INSERT INTO `django_migrations` VALUES (28, 'index', '0013_auto_20190426_2043', '2019-04-26 20:43:44.111429');
INSERT INTO `django_migrations` VALUES (29, 'index', '0014_newsinformation', '2019-04-26 23:51:09.452739');
INSERT INTO `django_migrations` VALUES (30, 'index', '0015_newsinformation_type', '2019-04-27 01:12:12.896168');
INSERT INTO `django_migrations` VALUES (31, 'index', '0016_auto_20190427_1111', '2019-04-27 11:12:03.377490');
INSERT INTO `django_migrations` VALUES (32, 'index', '0017_auto_20190427_1527', '2019-04-27 15:27:53.387892');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('32gs45aa4abw5u402gh9qcql24aqdofg', 'ZGYzMDc2ZjNhYzkzZWIwMGUyZTljMzcwZmVjNDZiMDAwZTJkNWQ0Mzp7InVzZXJuYW1lIjoiemhhbmdzYW4ifQ==', '2019-05-09 13:11:23.376565');
INSERT INTO `django_session` VALUES ('49j89fo1t9wxkgq0n1z28xfpp7fgv6fp', 'YzUwZGM5M2U3ODVlZWRlYzQ0MTAzODExNDI2NDhlNWIxZjA2YTQ3YTp7fQ==', '2019-05-09 12:43:24.570315');
INSERT INTO `django_session` VALUES ('ifwljwp6zuq6uaiv3q4ba8rnj1ofgttq', 'YzE1NzFlYjUwOTUzZThjNjI5YTY3MjYwZTM0YTMzYWQ3MDMxMjJkYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMWJmYjg5YmNmZDkzZjBjMjQ0NDdkNThjM2ZjOTcyZThiMzAyOTc5IiwiaGVhZGltZyI6Ii9tZWRpYS9pbWFnZXMvdXNlci9tb3Jlbi5qcGciLCJpc19sb2dpbiI6MSwidXNlcl9pZCI6NCwidXNlcm5hbWUiOiJsZXl0b24ifQ==', '2019-05-11 19:59:26.102927');
INSERT INTO `django_session` VALUES ('ii8pvchenn81df4r1jmcme0frhufo3uh', 'YzUwZGM5M2U3ODVlZWRlYzQ0MTAzODExNDI2NDhlNWIxZjA2YTQ3YTp7fQ==', '2019-05-09 12:56:53.741352');
INSERT INTO `django_session` VALUES ('iu86k3m82zsv78593mewexx30v2gvm9c', 'YjFlMzU0MDliNDY1M2Y0MmE1OTc0NmVmYzQyMDY0NjA4NDY4MTA4Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMWJmYjg5YmNmZDkzZjBjMjQ0NDdkNThjM2ZjOTcyZThiMzAyOTc5IiwidXNlcm5hbWUiOiJ6aGFuZ3NhbjEiLCJoZWFkaW1nIjoiL21lZGlhL2ltYWdlcy91c2VyL21vcmVuLmpwZyJ9', '2019-05-09 17:39:08.183761');
INSERT INTO `django_session` VALUES ('kqnyv0667nj6mmpf7002kckdrvywh8es', 'MmUyNGQzODkxNjg1ZWY3MzE2NjAxZWVhZDQ1MTQ1NzBmM2I3ZThlYzp7ImlzX2xvZ2luIjoxLCJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6ImFodWFuZyJ9', '2019-05-31 12:57:37.863801');
INSERT INTO `django_session` VALUES ('oc57ouwy3ynun5rb277xpegd5j0k9v98', 'NGVmMDgwYzFkOGU4YjhhMDQ4YTYzMmU5MWVlYjE4ZDAzZWMwYTdmMDp7ImlzX2xvZ2luIjoxLCJ1c2VyX2lkIjoxMX0=', '2019-05-09 13:00:14.146141');
INSERT INTO `django_session` VALUES ('ogfaxwzus47fq2md0mmakv94nr5gwib7', 'NmRjMWZkYjUwMDJhNjNmN2I2ZTdkNmRhZjBkM2JiYWVlNmJkYjQ1ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMWJmYjg5YmNmZDkzZjBjMjQ0NDdkNThjM2ZjOTcyZThiMzAyOTc5IiwiaXNfbG9naW4iOjB9', '2019-05-09 12:27:16.765238');
INSERT INTO `django_session` VALUES ('u0cjbl5jeywmi75ki4sc0wnf5nlt7r4l', 'MGIxN2MyNjkxNDUyNjc3YjM4OTM1YTNmMjY4YzdmZDk3Y2MxMjcxNDp7InVzZXJuYW1lIjoibGV5dG9uIiwiaGVhZGltZyI6Ii9tZWRpYS9pbWFnZXMvdXNlci9tb3Jlbi5qcGciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTFiZmI4OWJjZmQ5M2YwYzI0NDQ3ZDU4YzNmYzk3MmU4YjMwMjk3OSJ9', '2019-05-09 13:59:06.822396');
INSERT INTO `django_session` VALUES ('uiblocbxoqbkj8efe9xflamxqwtnjqwe', 'ZjI2MDY1MmM3OTFkMmIzZGVhNTc0Y2YzOTgyNTNlY2RiMDE4YzQ1Mzp7ImlzX2xvZ2luIjowfQ==', '2019-05-09 12:41:28.944793');

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `redwood_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `history_redwood_id_c3624024_fk_redwood_id`(`redwood_id`) USING BTREE,
  INDEX `history_user_id_6457e0b2_fk_users_id`(`user_id`) USING BTREE,
  CONSTRAINT `history_redwood_id_c3624024_fk_redwood_id` FOREIGN KEY (`redwood_id`) REFERENCES `redwood` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `history_user_id_6457e0b2_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 224 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES (230, '2019-05-17 15:21:23.005049', 289, 6);

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `author` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES (1, '的发过火发过火对方过后是法国恢复规划法规发过火发过火是否更换是否更换是否更换是否更换', '华盛顿凤凰高楼大厦六点十分火锅连锁店反垄断法老地方联合国东方化工水电费海盗路飞劳动法和老古董复合弓东方红电话东方红东方红科技安装的空间发挥VB现场报名你放开\r\n价格或者可继续发挥GV剪烛西窗安居客的成长性检查空间相册不变是可进行传播开酒吧健康发展杰克逊不能看现场\r\n\r\n        老师肯定会发两个史莱克的复合管理考核得分高.\r\n\r\n       塑料袋返回给老师叫对方过后能力的说法收到货啥的购房考虑好不舍得离开公司的股份和你唠嗑水电费回来的酸辣粉 大数据时代立刻就很难受了贷款购房弄好了控制大V\r\n你不来卡hi欧洲训练和归纳吕浩发电量可不好这两款V领咖啡壶招待费脑子里想看是年华的复合弓招待费大富豪管理控制V领或者打开发展规划注下拉框博格华纳\r\n\r\n      流口水的哈伦裤展现出了富豪ID你最初效率可能干哈儿童脏乱差 达萨罗发货过来看大V会尽快咯啊对你好答复爱对方过后自动if有能力中心车库玫瑰红我让人很不自信 了深刻的风格和精力结合\r\n\r\n    克鲁赛德海格力斯地方联合各安咯或者联系仓库规划离开的说法或建立深V回家客厅q  \r\n\r\n     uoz;xngo;ndlbzcxnvh上课了梵蒂冈胡波我相册在v 拉克丝就更好了空心菜是拿回来看过日本 \r\n\r\n\r\n    拉克丝发过来吧空心菜V领看不舒服服在大V你回来 心理健康东城是回不了家卡的条件 离开的很干净了净资产续回来看吧\r\n\r\n             是的规范化老子检测率考核乐山大佛 单联开关复活节拉开打造成是很难了这次可循环了', '十多个', '2019-04-26 23:54:12.488311');
INSERT INTO `news` VALUES (2, '德国大夫', '德国大夫', '大风歌', '2019-04-27 00:29:05.874514');
INSERT INTO `news` VALUES (3, '大风歌', '二徒弟', '多个', '2019-04-27 00:29:15.196782');
INSERT INTO `news` VALUES (4, '大风歌大风歌', '哇塞多带感', '多个', '2019-04-27 00:29:26.306576');
INSERT INTO `news` VALUES (5, '大发横财v', '胡扯', '阿法狗', '2019-04-27 00:29:38.272267');
INSERT INTO `news` VALUES (6, '挖是否', '手续费CD分尬SDG S', '大风歌', '2019-04-27 00:29:50.871064');
INSERT INTO `news` VALUES (7, 'GGHJGHJB', 'ASDAD ASGFZSG XC ASG S', '阿法狗', '2019-04-27 00:30:09.367559');
INSERT INTO `news` VALUES (8, 'ASFZX', '是打发斯蒂芬', '暗室逢灯', '2019-04-27 00:30:16.976517');
INSERT INTO `news` VALUES (9, '是大法官的', '撒地方', '十多个', '2019-04-27 00:35:00.484089');
INSERT INTO `news` VALUES (10, '撒地方为', '撒地方', '阿法狗', '2019-04-27 00:35:18.631045');
INSERT INTO `news` VALUES (11, '撒地方是否sSDF', '是 撒地方SF', '暗室逢灯SDF', '2019-04-27 00:35:31.105745');
INSERT INTO `news` VALUES (12, 'SDF', 'SDF', 'SDF', '2019-04-27 00:35:58.032741');
INSERT INTO `news` VALUES (13, 'SDFH', 'SDFG DFGDF', '多个', '2019-04-27 00:36:05.828187');
INSERT INTO `news` VALUES (14, 'WRT', 'ASFG', '阿法狗', '2019-04-27 00:36:12.699799');
INSERT INTO `news` VALUES (15, 'REURTYEUTRYU', 'GSDHGHJGHFKFGHK', 'ASFSD', '2019-04-27 00:36:20.530628');
INSERT INTO `news` VALUES (16, 'ASDGDFG', 'ASDGDXCGZXCVG', '多个', '2019-04-27 00:36:28.854739');
INSERT INTO `news` VALUES (17, 'SDHGFDGHFD', 'GGFHJGHJ', 'GHJGHJ', '2019-04-27 00:36:34.832688');
INSERT INTO `news` VALUES (18, 'ADGSDFG', 'SDFGSDFVZXCVAXCAGADSFGASDF', 'QEWTG', '2019-04-27 00:36:43.472542');
INSERT INTO `news` VALUES (19, 'RTZDF346RASDF', 'SDFGAFG', 'AGASDFG', '2019-04-27 00:36:51.102131');
INSERT INTO `news` VALUES (20, 'ERES', 'DZXG', 'DFGF', '2019-04-27 00:37:00.134534');
INSERT INTO `news` VALUES (21, 'SADFG斯蒂芬告诉对方过后收到货都是收到货都是都是上帝电话都是地方哈地方哈卡斯比高考装修风格阿萨德咖啡馆包括在进行封闭空间工作服卡士大夫高标准口谐辞给', '收到货是的法规和是的法国恢复规划安徽省变得更即可发表在科学界卡的房价高个\r\n\r\n      塑料袋和贵金属大V韩国进口了和豆腐干不回家了打开发货管理接口的复合弓爱对方过后\r\n\r\n来得及开发和高科技在消费空间级大神发红包高科技先参考价格的放开价格折扣进行采购', '暗室逢灯', '2019-04-27 00:37:12.199601');

-- ----------------------------
-- Table structure for redwood
-- ----------------------------
DROP TABLE IF EXISTS `redwood`;
CREATE TABLE `redwood`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `price` double NOT NULL,
  `type` int(11) NOT NULL,
  `img` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 195 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of redwood
-- ----------------------------
INSERT INTO `redwood` VALUES (195, '名人汇馆 传统中式 国色天香大床床双人床1.8米明清仿古刺猬紫檀婚床红木家具', 23040, 0, 'images/redwood/7zGkd6wb15cL6015QN19sG678ULsj.jpg', '2019-05-17 15:09:36.049337', 1);
INSERT INTO `redwood` VALUES (196, '吉迪盆 传统中式 缅甸花梨木贵妃床红木家具新中式明清古典大果紫檀家具红木贵妃床', 19800, 0, 'images/redwood/5dM606Nh718HtT5H97F3mNLTK6x1M.jpg', '2019-05-17 15:09:36.114849', 1);
INSERT INTO `redwood` VALUES (197, '名人汇馆 新中式 一心一意大床 红木家具刺猬紫檀  双人大床婚床 1.8米床+2床头柜', 22640, 1, 'images/redwood/5Z46d9C75X6P1uEbfwL4JNtM18f50.jpg', '2019-05-17 15:09:36.120837', 1);
INSERT INTO `redwood` VALUES (198, '名人汇馆 传统中式 和谐沙发  非洲刺猬紫檀 古典榫卯  沙发六件套  客厅 ', 37620, 0, 'images/redwood/i1me78t931xecmh6Z55W6Csw0nT55.jpg', '2019-05-17 15:09:36.127326', 1);
INSERT INTO `redwood` VALUES (199, '仿古明清系列 中式风格 福禄绵延 兰亭序红木大床 非洲刺猬紫檀 卧室三件套（1.8米床+2*床头柜）', 31152, 2, 'images/redwood/qZ9t1jS8e5526nY5t761S0DTaPH6G.jpg', '2019-05-17 15:09:36.132816', 1);
INSERT INTO `redwood` VALUES (200, '仿古明清系列 中式风格 福云绵绵   吉祥如意 金如意大床 卧室三件套（1.8米床+2*床头柜）烫蜡工艺 天然环保', 25960, 2, 'images/redwood/FZchB77Z55iA7w6j68g9L1fDQ110V.jpg', '2019-05-17 15:09:36.138307', 1);
INSERT INTO `redwood` VALUES (201, '吉迪盆 传统中式 老挝大红酸枝 中式古典 交趾黄檀红木家具 客厅雕花锦绣电视柜', 64320, 0, 'images/redwood/b70DE5u68agdUI9Z9162FEtJx105u.jpg', '2019-05-17 15:09:36.143299', 1);
INSERT INTO `redwood` VALUES (202, '吉迪盆 传统中式 缅甸花梨木书桌 中式古典大果紫檀红木家具 书房雕花书桌椅组合', 41500, 0, 'images/redwood/91An620i5C8w5CtwOKT7XdCn0260Q.jpg', '2019-05-17 15:09:36.147790', 1);
INSERT INTO `redwood` VALUES (203, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 客厅玻璃酒柜储物柜 ', 39000, 0, 'images/redwood/qXSSp895c6H5aj766Yk1XX2u0x19y.jpg', '2019-05-17 15:09:36.151782', 1);
INSERT INTO `redwood` VALUES (204, '吉迪盆 传统中式 【新品促销】缅甸花梨木书桌 中式古典大果紫檀红木家具 书房丘比特书桌', 37000, 0, 'images/redwood/95HF3Ia08A0MGpMA0Ed1n72f5P6Q6.jpg', '2019-05-17 15:09:36.156771', 1);
INSERT INTO `redwood` VALUES (205, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 书房两联戴帽书柜组合', 36220, 0, 'images/redwood/FLFv54TU9H116l2o1CQ06D5XH7t8G.jpg', '2019-05-17 15:09:36.161263', 1);
INSERT INTO `redwood` VALUES (206, '吉迪盆 传统中式 缅甸花梨木沙发 中式古典 大果紫檀红木家具 客厅国色天香沙发组合【1+2+3】', 82000, 0, 'images/redwood/Oy1ts59528Iez96kjhKj0V4s76tg0.jpg', '2019-05-17 15:09:36.165755', 1);
INSERT INTO `redwood` VALUES (207, '吉迪盆 新中式 【新品促销】老挝红酸枝家具红木博古架新中式明清古典巴里黄檀红木家具古典博古架', 72000, 1, 'images/redwood/53BS4xH6RMAnd7025c9bz66WqOY81.jpg', '2019-05-17 15:09:36.171743', 1);
INSERT INTO `redwood` VALUES (208, '吉迪盆 新中式 【新品促销】老挝红酸枝餐桌新中式明清古典花枝红木家具圆台如意餐桌椅7件套', 72000, 1, 'images/redwood/E76vZ04u5h58XNe2TK7L6ff1A9te5.jpg', '2019-05-17 15:09:36.180228', 1);
INSERT INTO `redwood` VALUES (209, '名人汇馆 传统中式 团团圆圆电视柜 非洲刺猬紫檀 红木家具  客厅电视柜', 9200, 0, 'images/redwood/CG8Li8p5s96xmg7E091lD2re61uS5.jpg', '2019-05-17 15:09:36.187214', 1);
INSERT INTO `redwood` VALUES (210, '吉迪盆 传统中式 老挝大红酸枝 中式古典 交趾黄檀 红木家具 茶室休闲手工檀雕红木茶棚 ', 55980, 0, 'images/redwood/85n8i5mzPMu79y2oC7d1I6o0k8Ed6.jpg', '2019-05-17 15:09:36.193702', 1);
INSERT INTO `redwood` VALUES (211, '吉迪盆 传统中式 缅甸花梨木书柜 大果紫檀 中式古典红木家具 书房明清古典新中式三组合书柜', 52700, 0, 'images/redwood/tkW99Gc8n15xKUl7d9M52DD70M6K6.jpg', '2019-05-17 15:09:36.199192', 1);
INSERT INTO `redwood` VALUES (212, '吉迪盆 传统中式 缅甸花梨木书柜 中式古典大果紫檀红木家具 书房雕花三联无帽书柜', 49890, 0, 'images/redwood/1iyl75l30X6y6WcCx0L5vo8j41d9t.jpg', '2019-05-17 15:09:36.209672', 1);
INSERT INTO `redwood` VALUES (213, '吉迪盆 传统中式 缅甸花梨木博古架 中式古典大果紫檀红木家具 客厅直脚博古架花架装饰架组合', 46700, 0, 'images/redwood/kGRSP2ILnm57N9D1806sx5a1yB836.jpg', '2019-05-17 15:09:36.214165', 1);
INSERT INTO `redwood` VALUES (214, '吉迪盆 传统中式 【新品促销】老挝红酸枝电视柜红木家具红木电视柜新中式明清古典红木宝座电视柜', 44000, 0, 'images/redwood/a518JxxFp5wCk339NS2566e0yrjz7.jpg', '2019-05-17 15:09:36.218157', 1);
INSERT INTO `redwood` VALUES (215, '吉迪盆 传统中式 缅甸花梨木书桌 中式古典大果紫檀红木家具 书房梅兰竹菊雕花书桌椅组合', 45800, 0, 'images/redwood/EeEnnNx02R6875Xr7n63hGX0k59T1.jpg', '2019-05-17 15:09:36.224148', 1);
INSERT INTO `redwood` VALUES (216, '吉迪盆 传统中式 【新品促销】老挝红酸枝电视柜红木家具红木电视柜新中式明清古典巴里黄檀红木电视柜', 39600, 0, 'images/redwood/6nO5xUA985j7Vw3Wy0yIn196bhV04.jpg', '2019-05-17 15:09:36.235125', 1);
INSERT INTO `redwood` VALUES (217, '吉迪盆 传统中式 缅甸花梨木书桌 中式古典大果紫檀红木家具 书房檀雕书桌椅组合', 34800, 0, 'images/redwood/K81y3v7hiUu0X205KHg64r6M59Jft.jpg', '2019-05-17 15:09:36.240117', 1);
INSERT INTO `redwood` VALUES (218, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 餐厅中式风格明式餐厅7件套 ', 31800, 0, 'images/redwood/JK60v1MstVFR6875S54mvU638F9Wc.jpg', '2019-05-17 15:09:36.246604', 1);
INSERT INTO `redwood` VALUES (219, '吉迪盆 传统中式 【新品促销】老挝红酸枝餐桌新中式明清古典花枝红木家具厂款明式餐桌椅7件套', 68400, 0, 'images/redwood/26Z5586Yx74Kdo5ahD9uK4e0pGQW1.jpg', '2019-05-17 15:09:36.260079', 1);
INSERT INTO `redwood` VALUES (220, '吉迪盆 传统中式 【新品促销】老挝红酸枝三组合电视柜红木家具红木电视柜新中式明清古典巴里黄檀红木三米电视柜', 52000, 0, 'images/redwood/DZ5KE8S7uTu669690d1JYR4juyl57.jpg', '2019-05-17 15:09:36.268563', 1);
INSERT INTO `redwood` VALUES (221, '吉迪盆 传统中式 【新品促销】缅甸花梨木家具红木餐桌新中式明清古典大果紫檀红木家具琴素圆桌7件套', 32400, 0, 'images/redwood/6ch5563qH8yBt9WFm47sNMB1L60f7.jpg', '2019-05-17 15:09:36.274054', 1);
INSERT INTO `redwood` VALUES (222, '仿古明清系列 中式风格 红木家具★典藏臻品 非洲进口刺猬紫檀 象头如意中式雕花餐台11件套(1.58米圆餐台+10餐椅)', 25500, 2, 'images/redwood/3rDq645pcbw8Zq76se91C87N0cn5c.jpg', '2019-05-17 15:09:36.280541', 1);
INSERT INTO `redwood` VALUES (223, '仿古明清系列 中式风格 红木家具★典藏臻品 非洲刺猬紫檀 象头如意中式雕花餐台九件套(1.38米圆餐台+8餐椅) （1.38米圆餐台不带转盘 如需带转盘需加价1200元）', 22000, 2, 'images/redwood/6jbEWG7tGd694ls0J14R4x5wp9t85.jpg', '2019-05-17 15:09:36.288028', 1);
INSERT INTO `redwood` VALUES (224, '仿古明清系列 中式风格 （非洲刺猬紫檀） 纯手工打造中欧结合设计雕花 敦实厚重 四门衣柜', 33748, 2, 'images/redwood/N01pSp9dp68X3jN0q6dw7ra5C9n55.jpg', '2019-05-17 15:09:36.293019', 1);
INSERT INTO `redwood` VALUES (225, '仿古明清系列 中式风格 （非洲刺猬紫檀） 五福博古架 经典组合博古架', 16688, 2, 'images/redwood/hM60rwR7q15nQ54ZnM5V809znxJ86.jpg', '2019-05-17 15:09:36.303998', 1);
INSERT INTO `redwood` VALUES (226, '仿古明清系列 中式风格 非洲刺猬紫檀 典藏臻品 象头如意餐桌七件套(1.28米圆餐台+6餐椅，不带转盘，若加带转盘则需另加价1200元）', 20249, 2, 'images/redwood/E156jpn9aS5O4l81Nh6N0xFY75M0m.jpg', '2019-05-17 15:09:36.311483', 1);
INSERT INTO `redwood` VALUES (227, '仿古明清系列 中式风格 非洲刺猬紫檀 雅致生活 五福临门 荷花茶台六件套（1*荷花茶台+5*文福茶椅）', 18188, 2, 'images/redwood/A2Jv67E9eZT81Yqz7b1kz555Cq06G.jpg', '2019-05-17 15:09:36.315975', 1);
INSERT INTO `redwood` VALUES (228, '仿古明清系列 中式风格 非洲刺猬紫檀 典藏臻品 椅背镂空美雕 吉祥如意长方餐桌七件套（1方餐台+6*餐椅）', 17650, 2, 'images/redwood/17o5LY655lEJBTQ0M019PO46JdHT8.jpg', '2019-05-17 15:09:36.320966', 1);
INSERT INTO `redwood` VALUES (229, '仿古明清系列 中式风格 （非洲刺猬紫檀）四季花红木书柜 四门双抽书柜 组合书柜', 16616, 2, 'images/redwood/k665K1H84N9deJ57x5x9DnfRUJP00.jpg', '2019-05-17 15:09:36.329950', 1);
INSERT INTO `redwood` VALUES (230, '仿古明清系列 中式风格 非洲刺猬紫檀 雅致生活 腰型茶台六件套（1*腰型茶台+5*茶椅）', 15580, 2, 'images/redwood/5quO0385ug95S8k7QnprO61tTi5h6.jpg', '2019-05-17 15:09:36.334440', 1);
INSERT INTO `redwood` VALUES (231, '仿古明清系列 中式风格 (红木刺猬紫檀）雅致生活 宝鼎茶台六件套（1*茶台+5*茶椅）', 14280, 2, 'images/redwood/Pgdb65P6un16a651Kc87O0OC9jS5f.jpg', '2019-05-17 15:09:36.339431', 1);
INSERT INTO `redwood` VALUES (232, '仿古明清系列 中式风格 非洲刺猬紫檀 弯脚办公台 明清官帽椅 书房2件套（1*办公台+1*官帽椅）', 17650, 2, 'images/redwood/xC1GT5087aWm16IWjm0z5t69k66sB.jpg', '2019-05-17 15:09:36.344921', 1);
INSERT INTO `redwood` VALUES (233, '仿古明清系列 中式风格 非洲刺猬紫檀 中式典雅 红木双圆门书柜 四门双抽书柜 手工雕组合书柜（2个两门双抽书柜）', 16616, 2, 'images/redwood/CV6bS7689dU1H7ed54G0DuOIcu566.jpg', '2019-05-17 15:09:36.349413', 1);
INSERT INTO `redwood` VALUES (234, '仿古明清系列 中式风格 （红木刺猬紫檀）上乘之作 功夫茶几 茶水架 茶水台 ', 2288, 2, 'images/redwood/r9iUY26NyY9F068DF1j7WO6h5YC55.jpg', '2019-05-17 15:09:36.353905', 1);
INSERT INTO `redwood` VALUES (235, '仿古明清系列 中式风格 （非洲刺猬紫檀）山水浮雕  古香古色  红木山水五斗柜  五抽储物柜', 9086, 2, 'images/redwood/BBI051Py9Y7G7om8a15l4q6A1NQ6w.jpg', '2019-05-17 15:09:36.361890', 1);
INSERT INTO `redwood` VALUES (236, '仿古明清系列 中式风格 （非洲刺猬紫檀）用料厚实 豪华富贵电视柜 四抽储物地柜 1.98米电视柜', 8188, 2, 'images/redwood/9hqHyIi9As57Y7r6t586tL0172yiQ.jpg', '2019-05-17 15:09:36.365883', 1);
INSERT INTO `redwood` VALUES (237, '仿古明清系列 中式风格 梅兰竹菊 非洲刺猬紫檀 四季花红木电视柜 双抽四门储物地柜 1.8米电视柜', 8999, 2, 'images/redwood/U6L7GSuo5sR2K64y85iu70bd109uR.jpg', '2019-05-17 15:09:36.370873', 1);
INSERT INTO `redwood` VALUES (238, '名人汇馆 传统中式 七星伴月餐台 红木家具 刺猬紫檀  品质生活 餐厅套装', 18480, 0, 'images/redwood/DcxqG955hPU2A01NZp7Z6Kwx05876.jpg', '2019-05-17 15:09:36.377360', 1);
INSERT INTO `redwood` VALUES (239, '吉迪盆 传统中式 老挝大红酸枝 中式古典 交趾黄檀 红木家具 客厅休闲小方桌5件套', 49200, 0, 'images/redwood/4tqYtW15063p6GZk7yj879m6j5rTH.jpg', '2019-05-17 15:09:36.381852', 1);
INSERT INTO `redwood` VALUES (240, '吉迪盆 传统中式 【新品促销】老挝红酸枝圈椅红木家具新中式明清古典巴里黄檀家具红木皇宫椅三件套', 31500, 0, 'images/redwood/75te8a60365t7G0WpJqC1FgodfB97.jpg', '2019-05-17 15:09:36.387344', 1);
INSERT INTO `redwood` VALUES (241, '吉迪盆 传统中式 【新品促销】老挝红酸枝家具茶水柜红木家具茶叶柜新中式明式风格老挝花枝茶水柜', 23000, 0, 'images/redwood/8zE5177d696izTzCBB758pgwI50Ux.jpg', '2019-05-17 15:09:36.392333', 1);
INSERT INTO `redwood` VALUES (242, '吉迪盆 传统中式 缅甸花梨木电视柜红木家具红木电视柜新中式明清古典大果紫檀红木电视柜', 17500, 0, 'images/redwood/5F68ZYe11vn70Y57Q9c7kpcqpb6p9.jpg', '2019-05-17 15:09:36.397323', 1);
INSERT INTO `redwood` VALUES (243, '吉迪盆 传统中式 缅甸花梨木皇宫椅 中式古典大果紫檀红木家具 客厅中式风格皇宫椅休闲3件套 ', 16900, 0, 'images/redwood/78vgM5JAjPk056qWB1p7A8k9u1R69.jpg', '2019-05-17 15:09:36.401318', 1);
INSERT INTO `redwood` VALUES (244, '吉迪盆 传统中式 缅甸花梨木家具红木餐边柜明清古典大果紫檀红木家具玄关缅甸花梨木供桌', 14800, 0, 'images/redwood/108GzUtcV6BAmYG8hQq75c05L9566.jpg', '2019-05-17 15:09:36.405807', 1);
INSERT INTO `redwood` VALUES (245, '吉迪盆 传统中式 缅甸花梨木圈椅红木家具新中式明清古典大果紫檀家具红木圈椅三件套', 14250, 0, 'images/redwood/D18f586c3Z163Tkx5I0MkmnK9vm7F.jpg', '2019-05-17 15:09:36.410798', 1);
INSERT INTO `redwood` VALUES (246, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 客厅休闲红木小方桌5件套', 10672, 0, 'images/redwood/278UF8b1QcQ1E53EjG0w65CR6YF9F.jpg', '2019-05-17 15:09:36.415789', 1);
INSERT INTO `redwood` VALUES (247, '吉迪盆 传统中式 缅甸花梨木衣帽架 中式古典大果紫檀红木家具 卧室休闲简洁衣帽架 ', 7360, 0, 'images/redwood/5dQbe918BOY8Ef36r06wD8buXs750.jpg', '2019-05-17 15:09:36.420281', 1);
INSERT INTO `redwood` VALUES (248, '仿古明清系列 中式风格 （红木刺猬紫檀）红木家具 四出头官帽椅 3件套（2官帽椅+1花几）', 5980, 2, 'images/redwood/43K68W1cBXwQYRFSDp89E6d57650x.jpg', '2019-05-17 15:09:36.425772', 1);
INSERT INTO `redwood` VALUES (249, '吉迪盆 传统中式 【新品促销】缅甸花梨木小靠椅 中式古典大果紫檀红木家具 客厅休闲小官帽椅', 1400, 0, 'images/redwood/W4kj5917lFE5No66E4s8EOK80AlG4.jpg', '2019-05-17 15:09:36.430263', 1);
INSERT INTO `redwood` VALUES (250, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 客厅中式风格休闲小方凳', 750, 0, 'images/redwood/N6w54z6oZ6t8Ktuw781nB095T5yzV.jpg', '2019-05-17 15:09:36.435253', 1);
INSERT INTO `redwood` VALUES (251, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 客厅中式风格百鸟朝凤罗汉床3件套 ', 34669, 0, 'images/redwood/IQ95796nK8B6CRBY8tpn1IyR504J6.jpg', '2019-05-17 15:09:36.440751', 1);
INSERT INTO `redwood` VALUES (252, '吉迪盆 新中式 【新品促销】缅甸花梨木小方凳红木家具全榫卯结构可拆卸换鞋凳儿童凳大果紫檀家具红木富贵小方凳', 680, 1, 'images/redwood/AT80VHeB15AQ6Z67971iHxI85g9kc.jpg', '2019-05-17 15:09:36.445734', 1);
INSERT INTO `redwood` VALUES (253, '仿古明清系列 中式风格 （非洲刺猬紫檀）传统中式经典之作 双圆门组合间厅柜 组合博古架', 22066, 2, 'images/redwood/v62iR7w8oT15AQu967mghgPt7v508.jpg', '2019-05-17 15:09:36.450725', 1);
INSERT INTO `redwood` VALUES (254, '仿古明清系列 中式风格 （非洲刺猬紫檀）老工匠纯手工打造欧式深浮雕雕花 梳妆台套装【妆台+妆镜+妆凳】', 9086, 2, 'images/redwood/8865N8a1QSI6RefnC19FKOM570Pg8.jpg', '2019-05-17 15:09:36.459213', 1);
INSERT INTO `redwood` VALUES (255, '仿古明清系列 中式风格 （非洲刺猬紫檀）红木餐边柜 四抽餐边柜', 11682, 2, 'images/redwood/6J5LcS1996FLRj8ju85QaCk7XE057.jpg', '2019-05-17 15:09:36.464201', 1);
INSERT INTO `redwood` VALUES (256, '仿古明清系列 中式风格 （非洲刺猬紫檀）富贵花开 鹊鸟报喜  红木餐边柜  三抽餐边柜 ', 9086, 2, 'images/redwood/yh96A2f0557NY7jKv1zm6S9m08jAy.jpg', '2019-05-17 15:09:36.468691', 1);
INSERT INTO `redwood` VALUES (257, '仿古明清系列 中式风格 （非洲刺猬紫檀 ）玉堂和平 瓶花透雕 素雅玲珑  夫妻椅3件套【2椅+1方几】 ', 3899, 2, 'images/redwood/Mu917m0856Dh4CgFxLR1H9qy5F0p6.jpg', '2019-05-17 15:09:36.476177', 1);
INSERT INTO `redwood` VALUES (258, '仿古明清系列 中式风格 （红木刺猬紫檀）明清圈椅三件套（2圈椅+1花几）', 5980, 2, 'images/redwood/8hCBrTiT87F10V91fVE8m56K5Zd69.jpg', '2019-05-17 15:09:36.486160', 1);
INSERT INTO `redwood` VALUES (259, '仿古明清系列 中式风格 （红木刺猬紫檀） 浮生闲  雅致意生活  红木豪华摇椅 ', 5971, 2, 'images/redwood/4Hi999PQG6bM5g0Zzb87uD2J61IT5.jpg', '2019-05-17 15:09:36.491651', 1);
INSERT INTO `redwood` VALUES (260, '仿古明清系列 中式风格 （红木刺猬紫檀）古法传承  榫卯结合  坚固实用  五龙戏珠 龙头衣帽架', 1988, 2, 'images/redwood/b9E4M55K06iz4T7oba6H9A98FGB1u.jpg', '2019-05-17 15:09:36.496141', 1);
INSERT INTO `redwood` VALUES (261, '仿古明清系列 中式风格 （红木刺猬紫檀） 古典绣墩 小巧玲珑  品质坚固  实用百搭精品鼓凳', 900, 2, 'images/redwood/0YjTGxJ86150Z7906JPx6xI95sHxV.jpg', '2019-05-17 15:09:36.500133', 1);
INSERT INTO `redwood` VALUES (262, '仿古明清系列 中式风格 （红木刺猬紫檀）轻巧造型  简单实用  经典臻品  红木小方凳', 399, 2, 'images/redwood/17WLz560yl6956VmMJy7Ag987szmh.jpg', '2019-05-17 15:09:36.505124', 1);
INSERT INTO `redwood` VALUES (263, '仿古明清系列 中式风格 （红木刺猬紫檀） 玉堂和平  瓶花透雕  简古设计  情侣椅三件套（2*椅+1*圆几） ', 3899, 2, 'images/redwood/C81gp956SH596fmA8WR67PXI5YDR0.jpg', '2019-05-17 15:09:36.512110', 1);
INSERT INTO `redwood` VALUES (264, '吉迪盆 传统中式 老挝大红酸枝 中式古典 大红酸枝老料交趾黄檀精品红木家具客厅龙瑞沙发11件套', 1680000, 0, 'images/redwood/0Wd9cey5hJ1h6qXA6Q6Ao695J98u7.jpg', '2019-05-17 15:09:36.531075', 1);
INSERT INTO `redwood` VALUES (265, '吉迪盆 传统中式 老挝大红酸枝 中式古典 交趾黄檀精品红木家具客厅龙瑞沙发13件套', 757900, 0, 'images/redwood/G70pq6v4B95K1PuQ1N0T8kbA567wz.jpg', '2019-05-17 15:09:36.535068', 1);
INSERT INTO `redwood` VALUES (266, '吉迪盆 传统中式 老挝花枝木 中式古典巴里黄檀红木家具 客厅清式雕花象头沙发10件套', 288310, 0, 'images/redwood/Q7BWofFWm1665870buF5nZ04hMf39.jpg', '2019-05-17 15:09:36.540558', 1);
INSERT INTO `redwood` VALUES (267, '吉迪盆 传统中式 【新品促销】老挝红酸枝木沙发 中式古典 巴里黄檀红木家具 客厅老挝花枝如意沙发组合10件套', 260000, 0, 'images/redwood/f97gvV9PKQU70zdOxw280BP5U1965.jpg', '2019-05-17 15:09:36.544551', 1);
INSERT INTO `redwood` VALUES (268, '吉迪盆 传统中式 【新品促销】老挝红酸枝木沙发 中式古典 巴里黄檀红木家具 客厅老挝花枝宝座沙发组合11件套', 248000, 0, 'images/redwood/76t1c890wR7qHx5e3FpQJ5gc2w60g.jpg', '2019-05-17 15:09:36.549042', 1);
INSERT INTO `redwood` VALUES (269, '吉迪盆 传统中式 缅甸花梨木 大果紫檀 中式古典红木家具 客厅高端霸气龙瑞沙发11件套', 117880, 0, 'images/redwood/T6vbu01138z5TaK3s57qiT97ZyY7y.jpg', '2019-05-17 15:09:36.553534', 1);
INSERT INTO `redwood` VALUES (270, '吉迪盆 传统中式 【新品促销】缅甸花梨木沙发 中式古典 大果紫檀红木家具 客厅如意沙发组合11件套', 111600, 0, 'images/redwood/lwfXhj2857rK0UX6Dc71g5380dba9.jpg', '2019-05-17 15:09:36.558027', 1);
INSERT INTO `redwood` VALUES (271, '吉迪盆 传统中式 【新品促销】缅甸花梨木沙发 中式古典 大果紫檀红木家具 客厅宝座沙发组合11件套', 110000, 0, 'images/redwood/eHw5lVxp52R1cA907K4F8JU637S7V.jpg', '2019-05-17 15:09:36.563016', 1);
INSERT INTO `redwood` VALUES (272, '吉迪盆 传统中式 缅甸花梨木 中式古典大果紫檀红木家具 客厅手工雕花小屏风', 34680, 0, 'images/redwood/y357gW1DIUE9b7AO53860CNiC6m1Y.jpg', '2019-05-17 15:09:36.567508', 1);
INSERT INTO `redwood` VALUES (273, '吉迪盆 传统中式 【新品促销】缅甸花梨木沙发 中式古典 大果紫檀红木家具 客厅和谐沙发组合【1+1+3】', 65000, 0, 'images/redwood/Vq39sgT51775UgeDhU08A93p46UQc.jpg', '2019-05-17 15:09:36.572998', 1);
INSERT INTO `redwood` VALUES (274, '吉迪盆 传统中式 缅甸花梨木沙发 中式古典大果紫檀红木家具 客厅财源滚滚红木沙发7件套', 65980, 0, 'images/redwood/585y3yV1ZP0Uzu5eN7SXwow97610G.jpg', '2019-05-17 15:09:36.577489', 1);
INSERT INTO `redwood` VALUES (275, '吉迪盆 新中式 缅甸花梨木家具茶水柜红木家具茶叶柜新中式明式风格大果紫檀茶台', 4780, 1, 'images/redwood/5lY756537NRVpU76f90bVvI8cJZ1K.jpg', '2019-05-17 15:09:36.581982', 1);
INSERT INTO `redwood` VALUES (276, '吉迪盆 新中式 【新品促销】缅甸花梨木家具花架红木家具落地花几新中式明式风格大果紫檀花架古典花架', 1998, 1, 'images/redwood/e1Bw7Dbebj565bR339e08Kf1r76xo.jpg', '2019-05-17 15:09:36.585975', 1);
INSERT INTO `redwood` VALUES (277, '吉迪盆 新中式 缅甸花梨木家具茶盘红木家具茶具新中式明式风格大果紫檀茶海【不含烧水壶】', 2570, 1, 'images/redwood/91h0U6LU8qlq73tx95vMFI7Jz50N6.jpg', '2019-05-17 15:09:36.591962', 1);
INSERT INTO `redwood` VALUES (278, '吉迪盆 传统中式 缅甸花梨木大床 中式古典 大果紫檀红木家具 卧室中国风富豪红木床（1.8米床+2床头柜）', 44712, 0, 'images/redwood/5SNK76S1eHQIFD098H7J3JDYO3745.jpg', '2019-05-17 15:09:36.595456', 1);
INSERT INTO `redwood` VALUES (279, '吉迪盆 传统中式 缅甸花梨木 中式古典 大果紫檀红木家具 卧室中式风格吉祥竹节檀雕红木床三件套（1.8米床+2床头柜）', 48890, 0, 'images/redwood/6WFUOL58697YA7d5B07J93ywkXQ1A.jpg', '2019-05-17 15:09:36.599948', 1);
INSERT INTO `redwood` VALUES (280, '吉迪盆 传统中式 缅甸花梨木 中式古典 大果紫檀红木家具 卧室中式风格吉祥孔雀檀雕红木床三件套（1.8米床+2床头柜）', 46368, 0, 'images/redwood/R1MsildW65D9cs974G0GDx7450Vl8.jpg', '2019-05-17 15:09:36.605938', 1);
INSERT INTO `redwood` VALUES (281, '仿古明清系列 中式风格 （红木刺猬紫檀）新品上架 中式古典手工雕花 财源滚滚沙发六件套（1+2+3+茶几+2方几）', 46208, 2, 'images/redwood/Wx767E0pS5f9sW51I24Lc1zmjc8e6.jpg', '2019-05-17 15:09:36.610928', 1);
INSERT INTO `redwood` VALUES (282, '仿古明清系列 中式风格 五福临门 招财进宝 非洲巴西花梨木 中式象头如意红木沙发十件套（1*三人位+4*单人位+1*茶几+2*角几+2*方几）', 51688, 2, 'images/redwood/t58nRhBS1Qv07fa5c3N7C5sk4f697.jpg', '2019-05-17 15:09:36.615917', 1);
INSERT INTO `redwood` VALUES (283, '仿古明清系列 中式风格 福寿平安 松鹤长春 兰亭序沙发 非洲刺猬紫檀 客厅六件套（单人位+双人位+三人位+茶几+2*角几）', 46992, 2, 'images/redwood/d2i9A4leZfbt5q7075r5n18O5HoT6.jpg', '2019-05-17 15:09:36.619910', 1);
INSERT INTO `redwood` VALUES (284, '名人汇馆 中式风格 典藏臻品 吉祥如意  金如意沙发 非洲刺猬紫檀 客厅六件套  生漆工艺  高贵典雅', 44132, 2, 'images/redwood/0D7bTn68kudYie5UVS76M4745Tm19.jpg', '2019-05-17 15:09:36.625899', 1);
INSERT INTO `redwood` VALUES (285, '仿古明清系列 中式风格 典藏臻品 明清皇宫椅 非洲刺猬紫檀 客厅八件套（1*三人位+4*单人位+1*茶几+2*边几）', 38950, 2, 'images/redwood/5fADv67xO08lPi4157LaUPZi2P689.jpg', '2019-05-17 15:09:36.629892', 1);
INSERT INTO `redwood` VALUES (286, '仿古明清系列 中式风格 吉祥透雕 曲尺沙发 非洲刺猬紫檀 客厅六件套（单人位+双人位+三人位+茶几+2*角几）', 31152, 2, 'images/redwood/e058qq53vLT1D69MacaNL1570T7yh.jpg', '2019-05-17 15:09:36.634383', 1);
INSERT INTO `redwood` VALUES (287, '仿古明清系列 中式风格 （红木刺猬紫檀） 典藏臻品 手工雕花 富贵吉祥 金钱花几  红木花几 花架', 999, 2, 'images/redwood/iVPG07FSAvMAfO55528f195q36x7J.jpg', '2019-05-17 15:09:36.639375', 1);
INSERT INTO `redwood` VALUES (288, '仿古明清系列 中式风格 （非洲刺猬紫檀）造型典雅 美观精致 古香古色 花几 六角香几', 3116, 2, 'images/redwood/JmeCm08WN59piL158W0iqI5q5a677.jpg', '2019-05-17 15:09:36.644365', 1);
INSERT INTO `redwood` VALUES (289, '仿古明清系列 中式风格 （非洲刺猬紫檀）古韵生香 清风雅致 半月台 装饰台  一对拍两', 6500, 2, 'images/redwood/15O56AG8r76uihU480ep57qP9OldR.jpg', '2019-05-17 15:09:36.648856', 1);
INSERT INTO `redwood` VALUES (290, '仿古明清系列 中式风格 （红木刺猬紫檀）榫卯工艺  坚固实用  古香韵色 镂空透雕 典雅精致  红木花架   灯笼花几 ', 1500, 2, 'images/redwood/l0952tDaLpg97iRs87nH5dad6715Y.png', '2019-05-17 15:09:36.652848', 1);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `headimg` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `birthday` datetime(6) DEFAULT NULL,
  `gender` int(11) NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (3, 'zhangsan1', 'pbkdf2_sha256$120000$1o26WQ9TSBnU$lk1uoqtopuH1csYL0ObKA5KVkQA2QgytmuMx92pwEIQ=', '163@163.com', 'images/user/moren.jpg', 0, '2019-04-25 13:48:33.044351', '2019-05-17 12:59:39.000000', 1, NULL);
INSERT INTO `users` VALUES (4, 'leyton', 'pbkdf2_sha256$120000$iuuzSOQvI6B9$RgjxNYKj14aDWtlfXxPobC0urDW3O7PpJ5yG6ILqV0g=', 'leyton@protonmail.com', 'images/user/oqrf225Zn7UuT0Z51v3lo5e631F6e.jpg', 1, '2019-04-25 13:54:36.024257', '2222-12-12 00:00:00.000000', 2, '15132784561');
INSERT INTO `users` VALUES (5, 'huangxinxing', 'pbkdf2_sha256$120000$7hBPJ2Wh85H8$wzL3oIqjag0wuzqCxmpTD0JijoHgOALe7B1hYfAM4m8=', '123@123.COM', 'images/user/1QW97sXZtJH7VZW65NGU5922I6c91.jpg', 1, '2019-04-26 11:25:59.135778', '9999-02-28 00:00:00.000000', 1, '15132237887');
INSERT INTO `users` VALUES (6, 'ahuang', 'pbkdf2_sha256$150000$aF2pvRj7GHNf$VW1T6XTzcP1fi8UBO8mZKaN19+gfLACcXpGoJ+Aj6bg=', '1@1.com', 'images/user/5JTZD051gPUg581srd08h9Sb776YT.jpg', 1, '2019-05-17 12:57:25.532850', '2015-05-05 00:00:00.000000', 2, '15132455456');

SET FOREIGN_KEY_CHECKS = 1;
