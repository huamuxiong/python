/*
 Navicat Premium Data Transfer

 Source Server         : leyton
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : renthouse

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 20/05/2019 20:02:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for advice
-- ----------------------------
DROP TABLE IF EXISTS `advice`;
CREATE TABLE `advice`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `advices` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `reversion` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `add_time` datetime(6) DEFAULT NULL,
  `userA_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `advice_userA_id_697600f2_fk_user_id`(`userA_id`) USING BTREE,
  CONSTRAINT `advice_userA_id_697600f2_fk_user_id` FOREIGN KEY (`userA_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of advice
-- ----------------------------
INSERT INTO `advice` VALUES (1, '是个很反感', '1@122.com', '<p><img src=\"http://img.baidu.com/hi/jx2/j_0005.gif\"/></p><p style=\"line-height: 16px;\"><img src=\"http://127.0.0.1:8000/static/ueditor/dialogs/attachment/fileTypeImages/icon_doc.gif\"/><a style=\"font-size:12px; color:#0066cc;\" href=\"/media/advices/ueditor/20190520194643.docx\" title=\"40次指导.docx\">40次指导.docx</a></p><p>19:46:49℡2019-05-20</p><hr/><p><img width=\"530\" height=\"340\" src=\"http://api.map.baidu.com/staticimage?center=116.404,39.915&zoom=10&width=530&height=340&markers=116.404,39.915\"/></p><p style=\"display:none;\"><br/></p>', '好', '2019-05-19 15:32:02.078720', 10);

-- ----------------------------
-- Table structure for agent
-- ----------------------------
DROP TABLE IF EXISTS `agent`;
CREATE TABLE `agent`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relname` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `identity` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `workage` int(11) NOT NULL,
  `isTelephone` tinyint(1) NOT NULL,
  `img` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `userAgent_id` int(11) NOT NULL,
  `villageAgent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `userAgent_id`(`userAgent_id`) USING BTREE,
  UNIQUE INDEX `agent_userAgent_id_ae1d6853_uniq`(`userAgent_id`) USING BTREE,
  INDEX `agent_villageAgent_id_997e11e0_fk_village_id`(`villageAgent_id`) USING BTREE,
  CONSTRAINT `agent_userAgent_id_ae1d6853_fk_user_id` FOREIGN KEY (`userAgent_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `agent_villageAgent_id_997e11e0_fk_village_id` FOREIGN KEY (`villageAgent_id`) REFERENCES `village` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 93 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
INSERT INTO `auth_permission` VALUES (25, 'Can add Bookmark', 7, 'add_bookmark');
INSERT INTO `auth_permission` VALUES (26, 'Can change Bookmark', 7, 'change_bookmark');
INSERT INTO `auth_permission` VALUES (27, 'Can delete Bookmark', 7, 'delete_bookmark');
INSERT INTO `auth_permission` VALUES (28, 'Can view Bookmark', 7, 'view_bookmark');
INSERT INTO `auth_permission` VALUES (29, 'Can add User Setting', 8, 'add_usersettings');
INSERT INTO `auth_permission` VALUES (30, 'Can change User Setting', 8, 'change_usersettings');
INSERT INTO `auth_permission` VALUES (31, 'Can delete User Setting', 8, 'delete_usersettings');
INSERT INTO `auth_permission` VALUES (32, 'Can view User Setting', 8, 'view_usersettings');
INSERT INTO `auth_permission` VALUES (33, 'Can add User Widget', 9, 'add_userwidget');
INSERT INTO `auth_permission` VALUES (34, 'Can change User Widget', 9, 'change_userwidget');
INSERT INTO `auth_permission` VALUES (35, 'Can delete User Widget', 9, 'delete_userwidget');
INSERT INTO `auth_permission` VALUES (36, 'Can view User Widget', 9, 'view_userwidget');
INSERT INTO `auth_permission` VALUES (37, 'Can add log entry', 10, 'add_log');
INSERT INTO `auth_permission` VALUES (38, 'Can change log entry', 10, 'change_log');
INSERT INTO `auth_permission` VALUES (39, 'Can delete log entry', 10, 'delete_log');
INSERT INTO `auth_permission` VALUES (40, 'Can view log entry', 10, 'view_log');
INSERT INTO `auth_permission` VALUES (41, 'Can add 邮箱验证码', 11, 'add_emailpro');
INSERT INTO `auth_permission` VALUES (42, 'Can change 邮箱验证码', 11, 'change_emailpro');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 邮箱验证码', 11, 'delete_emailpro');
INSERT INTO `auth_permission` VALUES (44, 'Can view 邮箱验证码', 11, 'view_emailpro');
INSERT INTO `auth_permission` VALUES (45, 'Can add 新闻资讯', 12, 'add_newsinformation');
INSERT INTO `auth_permission` VALUES (46, 'Can change 新闻资讯', 12, 'change_newsinformation');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 新闻资讯', 12, 'delete_newsinformation');
INSERT INTO `auth_permission` VALUES (48, 'Can view 新闻资讯', 12, 'view_newsinformation');
INSERT INTO `auth_permission` VALUES (49, 'Can add 用户信息', 13, 'add_user');
INSERT INTO `auth_permission` VALUES (50, 'Can change 用户信息', 13, 'change_user');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 用户信息', 13, 'delete_user');
INSERT INTO `auth_permission` VALUES (52, 'Can view 用户信息', 13, 'view_user');
INSERT INTO `auth_permission` VALUES (53, 'Can add 地区', 14, 'add_village');
INSERT INTO `auth_permission` VALUES (54, 'Can change 地区', 14, 'change_village');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 地区', 14, 'delete_village');
INSERT INTO `auth_permission` VALUES (56, 'Can view 地区', 14, 'view_village');
INSERT INTO `auth_permission` VALUES (57, 'Can add 浏览记录', 15, 'add_userhistory');
INSERT INTO `auth_permission` VALUES (58, 'Can change 浏览记录', 15, 'change_userhistory');
INSERT INTO `auth_permission` VALUES (59, 'Can delete 浏览记录', 15, 'delete_userhistory');
INSERT INTO `auth_permission` VALUES (60, 'Can view 浏览记录', 15, 'view_userhistory');
INSERT INTO `auth_permission` VALUES (61, 'Can add 关注', 16, 'add_userfocus');
INSERT INTO `auth_permission` VALUES (62, 'Can change 关注', 16, 'change_userfocus');
INSERT INTO `auth_permission` VALUES (63, 'Can delete 关注', 16, 'delete_userfocus');
INSERT INTO `auth_permission` VALUES (64, 'Can view 关注', 16, 'view_userfocus');
INSERT INTO `auth_permission` VALUES (65, 'Can add 评论', 17, 'add_usercomment');
INSERT INTO `auth_permission` VALUES (66, 'Can change 评论', 17, 'change_usercomment');
INSERT INTO `auth_permission` VALUES (67, 'Can delete 评论', 17, 'delete_usercomment');
INSERT INTO `auth_permission` VALUES (68, 'Can view 评论', 17, 'view_usercomment');
INSERT INTO `auth_permission` VALUES (69, 'Can add 申诉建议', 18, 'add_useradvice');
INSERT INTO `auth_permission` VALUES (70, 'Can change 申诉建议', 18, 'change_useradvice');
INSERT INTO `auth_permission` VALUES (71, 'Can delete 申诉建议', 18, 'delete_useradvice');
INSERT INTO `auth_permission` VALUES (72, 'Can view 申诉建议', 18, 'view_useradvice');
INSERT INTO `auth_permission` VALUES (73, 'Can add 指定购房', 19, 'add_specifythepurchase');
INSERT INTO `auth_permission` VALUES (74, 'Can change 指定购房', 19, 'change_specifythepurchase');
INSERT INTO `auth_permission` VALUES (75, 'Can delete 指定购房', 19, 'delete_specifythepurchase');
INSERT INTO `auth_permission` VALUES (76, 'Can view 指定购房', 19, 'view_specifythepurchase');
INSERT INTO `auth_permission` VALUES (77, 'Can add 用户发布信息', 20, 'add_release');
INSERT INTO `auth_permission` VALUES (78, 'Can change 用户发布信息', 20, 'change_release');
INSERT INTO `auth_permission` VALUES (79, 'Can delete 用户发布信息', 20, 'delete_release');
INSERT INTO `auth_permission` VALUES (80, 'Can view 用户发布信息', 20, 'view_release');
INSERT INTO `auth_permission` VALUES (81, 'Can add 地区位置', 21, 'add_location');
INSERT INTO `auth_permission` VALUES (82, 'Can change 地区位置', 21, 'change_location');
INSERT INTO `auth_permission` VALUES (83, 'Can delete 地区位置', 21, 'delete_location');
INSERT INTO `auth_permission` VALUES (84, 'Can view 地区位置', 21, 'view_location');
INSERT INTO `auth_permission` VALUES (85, 'Can add 经纪人信息', 22, 'add_useragent');
INSERT INTO `auth_permission` VALUES (86, 'Can change 经纪人信息', 22, 'change_useragent');
INSERT INTO `auth_permission` VALUES (87, 'Can delete 经纪人信息', 22, 'delete_useragent');
INSERT INTO `auth_permission` VALUES (88, 'Can view 经纪人信息', 22, 'view_useragent');
INSERT INTO `auth_permission` VALUES (89, 'Can add 租房', 23, 'add_houseinfo');
INSERT INTO `auth_permission` VALUES (90, 'Can change 租房', 23, 'change_houseinfo');
INSERT INTO `auth_permission` VALUES (91, 'Can delete 租房', 23, 'delete_houseinfo');
INSERT INTO `auth_permission` VALUES (92, 'Can view 租房', 23, 'view_houseinfo');

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
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$150000$BIQUNuCBNrOI$dgnhm7fHIbTnn4gHI8BCDr0doB2mtxQcn+2O1EMTk9I=', '2019-05-20 00:12:00.651947', 1, 'leyton', '', '', 'leyton01@protonmail.com', 1, 1, '2019-05-20 00:06:07.375907');

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `satisfied` int(11) NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `house_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `comment_house_id_db227d0f_fk_houseinfo_id`(`house_id`) USING BTREE,
  INDEX `comment_user_id_2224f9d1_fk_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `comment_house_id_db227d0f_fk_houseinfo_id` FOREIGN KEY (`house_id`) REFERENCES `houseinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `comment_user_id_2224f9d1_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (23, 'homelink', 'houseinfo');
INSERT INTO `django_content_type` VALUES (11, 'index', 'emailpro');
INSERT INTO `django_content_type` VALUES (21, 'index', 'location');
INSERT INTO `django_content_type` VALUES (12, 'index', 'newsinformation');
INSERT INTO `django_content_type` VALUES (20, 'index', 'release');
INSERT INTO `django_content_type` VALUES (19, 'index', 'specifythepurchase');
INSERT INTO `django_content_type` VALUES (13, 'index', 'user');
INSERT INTO `django_content_type` VALUES (18, 'index', 'useradvice');
INSERT INTO `django_content_type` VALUES (22, 'index', 'useragent');
INSERT INTO `django_content_type` VALUES (17, 'index', 'usercomment');
INSERT INTO `django_content_type` VALUES (16, 'index', 'userfocus');
INSERT INTO `django_content_type` VALUES (15, 'index', 'userhistory');
INSERT INTO `django_content_type` VALUES (14, 'index', 'village');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES (10, 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES (8, 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES (9, 'xadmin', 'userwidget');

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
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-05-18 20:40:25.259895');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2019-05-18 20:40:25.621687');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2019-05-18 20:40:26.140387');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2019-05-18 20:40:26.246328');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2019-05-18 20:40:26.259320');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2019-05-18 20:40:26.353267');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2019-05-18 20:40:26.403238');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2019-05-18 20:40:26.465203');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2019-05-18 20:40:26.479196');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2019-05-18 20:40:26.529167');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2019-05-18 20:40:26.534162');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2019-05-18 20:40:26.546155');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2019-05-18 20:40:26.602123');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2019-05-18 20:40:26.658093');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2019-05-18 20:40:26.714062');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2019-05-18 20:40:26.729053');
INSERT INTO `django_migrations` VALUES (17, 'homelink', '0001_initial', '2019-05-18 20:40:26.773030');
INSERT INTO `django_migrations` VALUES (18, 'index', '0001_initial', '2019-05-18 20:40:27.245913');
INSERT INTO `django_migrations` VALUES (19, 'homelink', '0002_auto_20190518_2040', '2019-05-18 20:40:28.151401');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2019-05-18 20:40:28.279326');
INSERT INTO `django_migrations` VALUES (21, 'xadmin', '0001_initial', '2019-05-18 20:40:28.410272');
INSERT INTO `django_migrations` VALUES (22, 'xadmin', '0002_log', '2019-05-18 20:40:28.638139');
INSERT INTO `django_migrations` VALUES (23, 'xadmin', '0003_auto_20160715_0100', '2019-05-18 20:40:28.871085');
INSERT INTO `django_migrations` VALUES (24, 'index', '0002_auto_20190518_2120', '2019-05-18 21:20:32.632795');
INSERT INTO `django_migrations` VALUES (25, 'index', '0003_auto_20190520_1024', '2019-05-20 10:24:34.720553');
INSERT INTO `django_migrations` VALUES (26, 'index', '0004_auto_20190520_1612', '2019-05-20 16:12:55.701398');
INSERT INTO `django_migrations` VALUES (27, 'index', '0005_auto_20190520_1613', '2019-05-20 16:13:57.660483');

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
INSERT INTO `django_session` VALUES ('i7q1gdgeqzx7ngkqjuddkym1g7dccv1p', 'MDE5ODY2M2JiNThkMGJjOGVlYWVkYzg1NDJhYjdkOTE5OTZmOTFhZTp7fQ==', '2019-06-01 23:51:35.159241');
INSERT INTO `django_session` VALUES ('plutwetwae2yeo4cewyp17o8jaiwk2mo', 'NGU5ZGYwN2I1ZmZiYWU0MTZlMGJlMGNiMGE4M2MxMWRlMDNlNzk4Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NzJjMTc2NmYwNjY4MzgxY2EyMjQ3ZjBjM2FiMTE3MTMzNzU2OTc1IiwiTElTVF9RVUVSWSI6W1siaW5kZXgiLCJ1c2VyYWR2aWNlIl0sIiJdLCJ1c2VyX2lkIjoxMCwidXNlcm5hbWUiOiJsZXl0b24iLCJpc0xvZ2luIjoxLCJoZWFkUG9ydHJhaXQiOiIvc3RhdGljL2ltYWdlcy9ndWFueXUuanBnIn0=', '2019-06-03 19:48:25.831965');
INSERT INTO `django_session` VALUES ('t82gmvn96vh4ukmt9i82lhhdenmqvyu7', 'ODhiNGI0YjhhNGU5ZTdkY2U0NDlhYTcxMmQzNzFmMDQ5YzAwMTZmZDp7InVzZXJfaWQiOjgsInVzZXJuYW1lIjoiaHVhbXV4aW9uZyIsImlzTG9naW4iOjEsImhlYWRQb3J0cmFpdCI6Ii9zdGF0aWMvaW1hZ2VzL2d1YW55dS5qcGcifQ==', '2019-06-01 23:52:15.532341');

-- ----------------------------
-- Table structure for emailpro
-- ----------------------------
DROP TABLE IF EXISTS `emailpro`;
CREATE TABLE `emailpro`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `send_type` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `send_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of emailpro
-- ----------------------------
INSERT INTO `emailpro` VALUES (1, 'BspfxU3IPRTFXEmt', 'huamuxiong_2018@163.com', 'register', '2019-05-18 21:21:13.026205');
INSERT INTO `emailpro` VALUES (2, 'CuSlbQSytyhB722i', 'huamuxiong_2018@163.com', 'register', '2019-05-18 21:29:50.905004');
INSERT INTO `emailpro` VALUES (3, '09JoI4yky0nCHfr0', 'leyton01@protonmail.com', 'register', '2019-05-18 21:42:32.411439');
INSERT INTO `emailpro` VALUES (4, '5bbDEKG5pgPUs8uu', 'leyton01@protonmail.com', 'register', '2019-05-18 22:15:24.311656');
INSERT INTO `emailpro` VALUES (5, 'LTMTwHbEQaIwJUe3', 'huamuxiong_2018@163.com', 'register', '2019-05-18 22:27:33.805650');
INSERT INTO `emailpro` VALUES (6, '84HmZpy3Pst2wmvs', 'huamuxiong_2018@163.com', 'forget', '2019-05-18 22:52:58.676689');
INSERT INTO `emailpro` VALUES (7, 'eM1jJoFHLyUBBtRh', 'huamuxiong_2018@163.com', 'forget', '2019-05-18 23:13:05.516775');
INSERT INTO `emailpro` VALUES (8, 'P36VaRZol3F1eM3t', 'leyton01@protonmail.com', 'register', '2019-05-19 00:47:25.772084');
INSERT INTO `emailpro` VALUES (9, '1LM4Vr9gGtjHuxn6', 'leyton01@protonmail.com', 'register', '2019-05-19 15:31:20.980508');

-- ----------------------------
-- Table structure for focus
-- ----------------------------
DROP TABLE IF EXISTS `focus`;
CREATE TABLE `focus`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `houseF_id` int(11) NOT NULL,
  `userF_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `focus_houseF_id_a0302ea0_fk_houseinfo_id`(`houseF_id`) USING BTREE,
  INDEX `focus_userF_id_5adeb515_fk_user_id`(`userF_id`) USING BTREE,
  CONSTRAINT `focus_houseF_id_a0302ea0_fk_houseinfo_id` FOREIGN KEY (`houseF_id`) REFERENCES `houseinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `focus_userF_id_5adeb515_fk_user_id` FOREIGN KEY (`userF_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) DEFAULT NULL,
  `houseH_id` int(11) NOT NULL,
  `userH_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `history_houseH_id_e1e12c16_fk_houseinfo_id`(`houseH_id`) USING BTREE,
  INDEX `history_userH_id_6dd15bac_fk_user_id`(`userH_id`) USING BTREE,
  CONSTRAINT `history_houseH_id_e1e12c16_fk_houseinfo_id` FOREIGN KEY (`houseH_id`) REFERENCES `houseinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `history_userH_id_6dd15bac_fk_user_id` FOREIGN KEY (`userH_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for houseinfo
-- ----------------------------
DROP TABLE IF EXISTS `houseinfo`;
CREATE TABLE `houseinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `bedroom` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `area` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `direction` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `floor` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `unit_price` int(11) NOT NULL,
  `message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `img_address` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userid` int(11) NOT NULL,
  `release_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isFabu` tinyint(1) NOT NULL,
  `add_date` datetime(6) NOT NULL,
  `mod_date` datetime(6) NOT NULL,
  `location_id` int(11) DEFAULT NULL,
  `village_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `houseinfo_location_id_9857a34d_fk_location_id`(`location_id`) USING BTREE,
  INDEX `houseinfo_village_id_7d24de1a_fk_village_id`(`village_id`) USING BTREE,
  CONSTRAINT `houseinfo_location_id_9857a34d_fk_location_id` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `houseinfo_village_id_7d24de1a_fk_village_id` FOREIGN KEY (`village_id`) REFERENCES `village` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of houseinfo
-- ----------------------------
INSERT INTO `houseinfo` VALUES (1, '整租·中粮万科长阳半岛 2室1厅 南', '2室1厅1卫', '87', '南', '低楼层（15层）', 5200, '无', '/static/renthouseImg/dc57GsoI418GKD2128853XfdPah7l.jpg', 1, '1个月前发布', 1, '2019-05-19 10:51:30.089401', '2019-05-19 10:51:30.089401', 41, 13);
INSERT INTO `houseinfo` VALUES (2, '整租·五和万科长阳天地 2室1厅 南', '2室1厅1卫', '81', '南', '中楼层（21层）', 5200, '无', '/static/renthouseImg/F7U1qk58SmnJyIS5U3520884doD2x.jpg', 1, '2个月前发布', 1, '2019-05-19 10:51:30.095399', '2019-05-19 10:51:30.095399', 41, 13);
INSERT INTO `houseinfo` VALUES (3, '整租·吴店西里 2室1厅 南/北', '2室1厅1卫', '114', '南 北', '低楼层（6层）', 6000, '无', '/static/renthouseImg/f8W5yf1Bf2nqpB145nyzB85432Bm8.jpg', 1, '7个月前发布', 1, '2019-05-19 10:51:30.098394', '2019-05-19 10:51:30.098394', 40, 13);
INSERT INTO `houseinfo` VALUES (4, '原香小镇二区 2室1厅 南/北', '2室1厅1卫', '89', '南 北', '低楼层（6层）', 5500, '无', '/static/renthouseImg/Wr92v8AuG5dW1L83H02mCX20eK45g.jpg', 1, '17天前发布', 1, '2019-05-19 10:51:30.104392', '2019-05-19 10:51:30.104392', 41, 13);
INSERT INTO `houseinfo` VALUES (5, '整租·中粮万科长阳半岛 2室1厅 南', '2室1厅1卫', '87', '南', '低楼层（15层）', 5200, '无', '/static/renthouseImg/v10Oslxga2N5F2P8r15kK6h35K55G.jpg', 1, '1个月前发布', 1, '2019-05-19 11:13:28.215314', '2019-05-19 11:13:28.215314', 41, 13);
INSERT INTO `houseinfo` VALUES (6, '整租·五和万科长阳天地 2室1厅 南', '2室1厅1卫', '81', '南', '中楼层（21层）', 5200, '无', '/static/renthouseImg/L15o1Uev08aDZg6y5J5853C2WqVO5.jpg', 1, '2个月前发布', 1, '2019-05-19 11:13:28.222281', '2019-05-19 11:13:28.222281', 41, 13);
INSERT INTO `houseinfo` VALUES (7, '整租·吴店西里 2室1厅 南/北', '2室1厅1卫', '114', '南 北', '低楼层（6层）', 6000, '无', '/static/renthouseImg/R68Kw30kM5F6jsK2QN51K53JN7r5v.jpg', 1, '7个月前发布', 1, '2019-05-19 11:13:28.228277', '2019-05-19 11:13:28.228277', 40, 13);
INSERT INTO `houseinfo` VALUES (8, '原香小镇二区 2室1厅 南/北', '2室1厅1卫', '89', '南 北', '低楼层（6层）', 5500, '无', '/static/renthouseImg/1MvF07yW02631m5S5Ol8m5Ee9gqHp.jpg', 1, '17天前发布', 1, '2019-05-19 11:13:28.238279', '2019-05-19 11:13:28.238279', 41, 13);
INSERT INTO `houseinfo` VALUES (9, '苏园小区 3室1厅 东/西', '3室1厅1卫', '208', '东 西', '低楼层（5层）', 15000, '无', '/static/renthouseImg/aPECX53653VmWB5V8J1SD621o1WZ7.jpg', 1, '13天前发布', 1, '2019-05-19 11:13:37.998319', '2019-05-19 11:13:37.998319', 40, 13);
INSERT INTO `houseinfo` VALUES (10, '长阳半岛怡和路6号院 3室2厅 南/北', '3室2厅2卫', '165', '南 北', '中楼层（15层）', 9300, '无', '/static/renthouseImg/8t6X3245j55G1viS10TtzOVsm5mZ7.jpg', 1, '23天前发布', 1, '2019-05-19 11:13:38.002296', '2019-05-19 11:13:38.002296', 41, 13);
INSERT INTO `houseinfo` VALUES (11, '整租·长阳半岛怡和路8号院 3室1厅 南/北', '3室1厅2卫', '165', '南 北', '中楼层（15层）', 8300, '无', '/static/renthouseImg/Zk503N25u1C8i1K8PMv58D7jXe6zT.jpg', 1, '7天前发布', 1, '2019-05-19 11:13:38.005313', '2019-05-19 11:13:38.005313', 41, 13);
INSERT INTO `houseinfo` VALUES (12, '拱辰南大街 2室1厅 南/北', '2室1厅1卫', '74', '南 北', '低楼层（6层）', 2800, '无', '/static/renthouseImg/9NwZO133KhP65PrWT522pX83te50Q.jpg', 1, '23天前发布', 1, '2019-05-19 11:14:51.110847', '2019-05-19 11:14:51.110847', 40, 13);
INSERT INTO `houseinfo` VALUES (13, '整租·西潞昊宏家园 2室1厅 东/西', '2室1厅1卫', '80', '东 西', '高楼层（6层）', 2700, '无', '/static/renthouseImg/MU2rsUa3HoM891hz45n85m3o9I6D5.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.114898', '2019-05-19 11:14:51.114898', 40, 13);
INSERT INTO `houseinfo` VALUES (14, '整租·建设巷小区 2室1厅 南/北', '2室1厅1卫', '56', '南 北', '中楼层（6层）', 2500, '无', '/static/renthouseImg/15568aJV3c5Wp6fY3Zo2EBJW1m9G8.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.117840', '2019-05-19 11:14:51.117840', 40, 13);
INSERT INTO `houseinfo` VALUES (15, '四合巷小区 2室1厅 南', '2室1厅1卫', '57', '南', '高楼层（6层）', 2200, '无', '/static/renthouseImg/0T5yVI1T548SH8mqA6432oZIYc0n5.jpg', 1, '16天前发布', 1, '2019-05-19 11:14:51.121822', '2019-05-19 11:14:51.121822', 40, 13);
INSERT INTO `houseinfo` VALUES (16, '整租·佳世苑小区 2室1厅 南/北', '2室1厅2卫', '96', '南 北', '高楼层（6层）', 3000, '无', '/static/renthouseImg/82Nd434sHwMV5sQlw56D0I8215hnz.jpg', 1, '8天前发布', 1, '2019-05-19 11:14:51.125835', '2019-05-19 11:14:51.125835', 40, 13);
INSERT INTO `houseinfo` VALUES (17, '整租·体育场路26号院 2室1厅 南/北', '2室1厅1卫', '52', '南 北', '高楼层（5层）', 2300, '无', '/static/renthouseImg/vFdSv3o26dKWz535F45FDL18805ZU.jpg', 1, '2天前发布', 1, '2019-05-19 11:14:51.128834', '2019-05-19 11:14:51.128834', 40, 13);
INSERT INTO `houseinfo` VALUES (18, '伟业嘉园西里 2室1厅 复式 南', '2室1厅1卫', '53', '南', '中楼层（5层）', 2750, '无', '/static/renthouseImg/oQ455b42Pk8Y651oeng8jTOcg3d10.jpg', 1, '2个月前发布', 1, '2019-05-19 11:14:51.131832', '2019-05-19 11:14:51.131832', 40, 13);
INSERT INTO `houseinfo` VALUES (19, '整租·四合巷小区 2室1厅 南', '2室1厅1卫', '57', '南', '高楼层（6层）', 2300, '无', '/static/renthouseImg/3uN4Nd2g5R81pt0755v11a6qHsFRQ.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.133888', '2019-05-19 11:14:51.133888', 40, 13);
INSERT INTO `houseinfo` VALUES (20, '整租·四合巷小区 2室2厅 南/北', '2室2厅1卫', '65', '南 北', '高楼层（6层）', 2000, '无', '/static/renthouseImg/R8ymAt2D5h113T5W3493jY5LpMy6q.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.137817', '2019-05-19 11:14:51.137817', 40, 13);
INSERT INTO `houseinfo` VALUES (21, '整租·行宫园三里 2室1厅 东/西', '2室1厅1卫', '78', '东 西', '高楼层（6层）', 2500, '无', '/static/renthouseImg/12US85f14yN6x4VLn55gIY5P7pG3a.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.140829', '2019-05-19 11:14:51.140829', 40, 13);
INSERT INTO `houseinfo` VALUES (22, '花园巷小区 2室1厅 南/北', '2室1厅1卫', '72', '南 北', '中楼层（6层）', 2600, '无', '/static/renthouseImg/5W35Zr4MjFeh87NW1657Ka1XL1O2a.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.142810', '2019-05-19 11:14:51.142810', 40, 13);
INSERT INTO `houseinfo` VALUES (23, '西潞园二里 2室1厅 南/北', '2室1厅1卫', '72', '南 北', '低楼层（6层）', 2500, '无', '/static/renthouseImg/w51r2S4J1b5JrC328Q6Wz52v4LAyB.jpg', 1, '10天前发布', 1, '2019-05-19 11:14:51.144880', '2019-05-19 11:14:51.144880', 40, 13);
INSERT INTO `houseinfo` VALUES (24, '四合巷小区 2室1厅 南/北', '2室1厅1卫', '65', '南 北', '低楼层（6层）', 2700, '无', '/static/renthouseImg/BN2D4b5RLoKQf25DTLwi21k825636.jpg', 1, '3天前发布', 1, '2019-05-19 11:14:51.147888', '2019-05-19 11:14:51.147888', 40, 13);
INSERT INTO `houseinfo` VALUES (25, '行宫园三里 2室1厅 南', '2室1厅1卫', '71', '南', '低楼层（6层）', 2700, '无', '/static/renthouseImg/M5kJ821d2G6uL3g45N5L5y4GIGjb6.jpg', 1, '1天前发布', 1, '2019-05-19 11:14:51.150821', '2019-05-19 11:14:51.150821', 40, 13);
INSERT INTO `houseinfo` VALUES (26, '整租·吴店东里 2室1厅 南/北', '2室1厅1卫', '91', '南 北', '中楼层（6层）', 2800, '无', '/static/renthouseImg/yj21epVJK2P8u95xi83z06fZZ554l.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.153809', '2019-05-19 11:14:51.153809', 40, 13);
INSERT INTO `houseinfo` VALUES (27, '整租·行宫园三里 2室1厅 南/北', '2室1厅1卫', '66', '南 北', '高楼层（6层）', 2200, '无', '/static/renthouseImg/hI0FXdocx43801iP5zcI5y20a3D65.jpg', 1, '2个月前发布', 1, '2019-05-19 11:14:51.156818', '2019-05-19 11:14:51.156818', 40, 13);
INSERT INTO `houseinfo` VALUES (28, '整租·行宫园一里 2室1厅 东/西', '2室1厅1卫', '61', '东 西', '中楼层（6层）', 2500, '无', '/static/renthouseImg/XqD5cv03386p2x5eK44yRpC81R5jo.jpg', 1, '2个月前发布', 1, '2019-05-19 11:14:51.158813', '2019-05-19 11:14:51.158813', 40, 13);
INSERT INTO `houseinfo` VALUES (29, '碧桂园小区C区 2室1厅 西北', '2室1厅1卫', '92', '西北', '高楼层（16层）', 2800, '无', '/static/renthouseImg/5QQ64D4M3Mmem13nZr256G5T8Naw7.jpg', 1, '24天前发布', 1, '2019-05-19 11:14:51.161856', '2019-05-19 11:14:51.161856', 41, 13);
INSERT INTO `houseinfo` VALUES (30, '整租·行宫园二里 2室1厅 南/北', '2室1厅1卫', '66', '南 北', '高楼层（6层）', 2200, '无', '/static/renthouseImg/fM3SP51Hq8hq4720VYu58b53BVk6t.jpg', 1, '1个月前发布', 1, '2019-05-19 11:14:51.164800', '2019-05-19 11:14:51.164800', 40, 13);
INSERT INTO `houseinfo` VALUES (31, '行宫园四里 2室1厅 南/北', '2室1厅1卫', '86', '南 北', '低楼层（6层）', 2800, '无', '/static/renthouseImg/UB54PyOE7V643p5h1245Vyi4AEE8U.jpg', 1, '13天前发布', 1, '2019-05-19 11:14:51.167798', '2019-05-19 11:14:51.167798', 40, 13);

-- ----------------------------
-- Table structure for location
-- ----------------------------
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `villageLocation_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `location_villageLocation_id_2f69e788_fk_village_id`(`villageLocation_id`) USING BTREE,
  CONSTRAINT `location_villageLocation_id_2f69e788_fk_village_id` FOREIGN KEY (`villageLocation_id`) REFERENCES `village` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of location
-- ----------------------------
INSERT INTO `location` VALUES (19, '滨河西区', 4);
INSERT INTO `location` VALUES (20, '大峪', 4);
INSERT INTO `location` VALUES (21, '冯村', 4);
INSERT INTO `location` VALUES (22, '城子', 4);
INSERT INTO `location` VALUES (23, '门头沟其他', 4);
INSERT INTO `location` VALUES (24, '和平里', 5);
INSERT INTO `location` VALUES (25, '永定门', 5);
INSERT INTO `location` VALUES (26, '月坛', 6);
INSERT INTO `location` VALUES (27, '木樨地', 6);
INSERT INTO `location` VALUES (28, '长椿街', 6);
INSERT INTO `location` VALUES (29, '玉泉营', 7);
INSERT INTO `location` VALUES (30, '北京南站', 7);
INSERT INTO `location` VALUES (31, '苹果园', 8);
INSERT INTO `location` VALUES (32, '古城', 8);
INSERT INTO `location` VALUES (33, '果园', 9);
INSERT INTO `location` VALUES (34, '通州北苑', 9);
INSERT INTO `location` VALUES (35, '高米店南', 10);
INSERT INTO `location` VALUES (36, '郁花园', 10);
INSERT INTO `location` VALUES (37, '亦庄', 11);
INSERT INTO `location` VALUES (38, '顺义城', 12);
INSERT INTO `location` VALUES (39, '后沙峪', 12);
INSERT INTO `location` VALUES (40, '良乡', 13);
INSERT INTO `location` VALUES (41, '长阳', 13);
INSERT INTO `location` VALUES (42, '定慧寺', 1);
INSERT INTO `location` VALUES (43, '公主坟', 1);
INSERT INTO `location` VALUES (44, '苏州桥', 1);
INSERT INTO `location` VALUES (45, '鼓楼大街', 2);
INSERT INTO `location` VALUES (46, '回龙观', 2);
INSERT INTO `location` VALUES (47, '望京', 3);
INSERT INTO `location` VALUES (48, '十里堡', 3);

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
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES (1, '发GV次新股和你', '是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是\r\n否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分\r\n类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到\r\n分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换\r\n法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个\r\n三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接\r\n第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自\r\n动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的\r\n的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好\r\n了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司\r\n风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你\r\n了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是\r\n否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风\r\n格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的\r\n大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就\r\n知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过\r\n火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将\r\n自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好\r\n了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着\r\n下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 \r\n阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链\r\n接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁\r\n发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老\r\n板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支\r\n链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更\r\nsdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风\r\n格和风格 阿拉丁发那个老师的的adfl是否更换法规回复公司风格更好发过火 方式更好是否更sdkj,fghkj来的萨芬个链接第六届发过来到分类就更好了对方过后的大连市分行给你了东方红支链淀粉东方蓝海龙泽党风廉政到分类干活了;自动发货管理者及相关留着下次不努力\r\n就知道每次老板娘拉到了换是否更换是否更换三个三个是上课了的方便顾客将自行车打了风格和风格 阿拉丁发那个老师的的adfl', '阿斯顿法国', '2019-04-28 12:43:03.170388');
INSERT INTO `news` VALUES (2, '收到货', '是的法规和的话', '是的法规和', '2019-04-28 12:52:39.786803');
INSERT INTO `news` VALUES (3, '是梵蒂冈和发vh', '对方是个好', '双方都很高', '2019-04-28 12:52:44.523817');
INSERT INTO `news` VALUES (4, '我是', '是的法规和是', '是否更换', '2019-04-28 12:54:02.879808');
INSERT INTO `news` VALUES (5, '的发过火发过火', '发过火法国恢复规划规划自行车v和注册VB和', '如图', '2019-04-28 12:54:09.584940');
INSERT INTO `news` VALUES (6, '而郭德纲', '大发鬼地方个成功阿法狗血常规', '阿斯顿法国', '2019-04-28 12:54:15.804426');
INSERT INTO `news` VALUES (7, '才能下半年从V型不能VB你VB你', '续保女不女的钛合金消费比女性难受分享吧谁发过发v', '是', '2019-04-28 12:54:24.620399');
INSERT INTO `news` VALUES (8, '十多个返回生成差多少分工fad', '发的当装修风格', '大风歌', '2019-04-28 12:54:31.543422');
INSERT INTO `news` VALUES (9, '全通过ad搜嘎c', '茶道功夫打算放过第三方只剩下三个VB想', '打算放过', '2019-04-28 12:54:38.399476');
INSERT INTO `news` VALUES (10, '十多个号东方今年从北京的泛海国际', '爱我打算成功发v爱是梵蒂冈as', '奥术灌输', '2019-04-28 12:54:44.830770');
INSERT INTO `news` VALUES (11, '从V型和v', '是否更换必须穿', '是的法规和', '2019-04-28 12:55:10.640554');
INSERT INTO `news` VALUES (12, '是梵蒂冈和告诉对方过后sdgh', '时代光华是的法规和是的法规和是的法规和s', '是是的法规和是梵蒂冈和', '2019-04-28 12:55:15.709714');
INSERT INTO `news` VALUES (13, '是否更换形成那你想从VB很难', '是否更换是否核心VB很难受发过火sfg', '谁发过是梵蒂冈和', '2019-04-28 12:55:20.873755');
INSERT INTO `news` VALUES (14, '私人会所发挂号信文化认同感是梵蒂冈和wrst', 'sg的规划师法规和三个是时该如何sg三个news_info_viewsnews_info_viewsnews_info_viesg的规划师法规和三个是时该如何sg三个sg的规划师法规和三个是时该如何sg三个news_info_viewsnews_insg的规划师法规和三个是时该如何sg三个news_info_viewsnews_info_viewsnews_insg的规划师法规和三个是时该如何sg三个news_info_viewsnews_info_viewsnews_insg的规划师法规和三个是时该如何sg三个news_info_viewsnews_info_viewsnews_info_viewsnews_inwssg的规划师法规和三个是时该如何sg三个news_info_viewsnews_info_viewsnews_in', 'sDGF', '2019-04-28 12:55:45.560873');
INSERT INTO `news` VALUES (15, 'ASDFGFDS', 'ADFG ADFG AFDG ASDFG', 'ASFG A', '2019-04-28 12:55:50.176397');
INSERT INTO `news` VALUES (16, '是修改红包自行车v直播阿三个返回撒地方和', '是大法官好在大V红包招待费v好吧在v查询并sad发vVB阿萨大V', '撒旦法规说的', '2019-04-28 12:55:56.618361');
INSERT INTO `news` VALUES (17, '是的发v或注册VB', '爱上对方过后真的VB在从vsadhb', '从是啥都好巴适得发红包', '2019-04-28 12:56:02.012674');
INSERT INTO `news` VALUES (18, '一季度不能从VB你在v不知羞耻巴尔在v朝北', '山东滨州程序包自行车本', '是大VVB', '2019-04-28 12:56:08.372415');
INSERT INTO `news` VALUES (19, '手续费高多谢支持VB上边这大V', '阿斯蒂芬都不在VB长得丑VB秩序册吧', '爱的风格在v', '2019-04-28 12:56:14.857017');
INSERT INTO `news` VALUES (20, '阿德父子雄兵不准许成本打副本是zdvc', '打副本是在大V从ad发布秩序部', '矮冬瓜', '2019-04-28 12:56:21.886837');
INSERT INTO `news` VALUES (21, '爱心安装V型vSXCvCv', 'asdfgzxc v', 'asfdgv', '2019-04-28 12:56:28.705776');
INSERT INTO `news` VALUES (22, '大幅度发VB你', '是否更换办手续差点被自行车不VB自行车v不再v', '昂地方盖上章', '2019-04-28 12:56:39.538460');
INSERT INTO `news` VALUES (23, '是的非常VB相册VB主程序吧', '萨尔复合弓长得丑VB秩序册VB盛世嫡妃VB行政村v', '撒地方和', '2019-04-28 12:56:46.206792');

-- ----------------------------
-- Table structure for release
-- ----------------------------
DROP TABLE IF EXISTS `release`;
CREATE TABLE `release`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `mod_time` datetime(6) NOT NULL,
  `houseR_id` int(11) NOT NULL,
  `userR_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `release_houseR_id_6c683f4c_fk_houseinfo_id`(`houseR_id`) USING BTREE,
  INDEX `release_userR_id_5a281d0b_fk_user_id`(`userR_id`) USING BTREE,
  CONSTRAINT `release_houseR_id_6c683f4c_fk_houseinfo_id` FOREIGN KEY (`houseR_id`) REFERENCES `houseinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `release_userR_id_5a281d0b_fk_user_id` FOREIGN KEY (`userR_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for specifythepurchase
-- ----------------------------
DROP TABLE IF EXISTS `specifythepurchase`;
CREATE TABLE `specifythepurchase`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` int(11) NOT NULL,
  `housetype` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `addressinfo` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `telephone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `mod_time` datetime(6) NOT NULL,
  `userS_id` int(11) NOT NULL,
  `villageS_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `specifythepurchase_userS_id_e7f4cf7a_fk_user_id`(`userS_id`) USING BTREE,
  INDEX `specifythepurchase_villageS_id_c74d1564_fk_village_id`(`villageS_id`) USING BTREE,
  CONSTRAINT `specifythepurchase_userS_id_e7f4cf7a_fk_user_id` FOREIGN KEY (`userS_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `specifythepurchase_villageS_id_c74d1564_fk_village_id` FOREIGN KEY (`villageS_id`) REFERENCES `village` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `birthday` date DEFAULT NULL,
  `telephone` varchar(12) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `QQ` varchar(12) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `headPortrait` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `signature` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `regTime` datetime(6) NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_username_email_telephone_QQ_16979fb0_uniq`(`username`, `email`, `telephone`, `QQ`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (10, 'leyton', 'pbkdf2_sha256$150000$ZJmgwmGZ26eX$9hX7z9WEgjxHJGh+jZQUJz+pfO4gnxtwElGPMhFrzLQ=', 'male', 'leyton01@protonmail.com', NULL, NULL, NULL, '/static/images/guanyu.jpg', NULL, '2019-05-19 15:31:20.977510', 1);

-- ----------------------------
-- Table structure for village
-- ----------------------------
DROP TABLE IF EXISTS `village`;
CREATE TABLE `village`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of village
-- ----------------------------
INSERT INTO `village` VALUES (1, '海淀');
INSERT INTO `village` VALUES (2, '昌平');
INSERT INTO `village` VALUES (3, '朝阳');
INSERT INTO `village` VALUES (4, '门头沟');
INSERT INTO `village` VALUES (5, '东城');
INSERT INTO `village` VALUES (6, '西城');
INSERT INTO `village` VALUES (7, '丰台');
INSERT INTO `village` VALUES (8, '石景山');
INSERT INTO `village` VALUES (9, '通州');
INSERT INTO `village` VALUES (10, '大兴');
INSERT INTO `village` VALUES (11, '亦庄开发区');
INSERT INTO `village` VALUES (12, '顺义');
INSERT INTO `village` VALUES (13, '房山');

-- ----------------------------
-- Table structure for xadmin_bookmark
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `url_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `query` varchar(1000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_bookmark_content_type_id_60941679_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for xadmin_log
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` varchar(32) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id`(`content_type_id`) USING BTREE,
  INDEX `xadmin_log_user_id_bb16a176_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES (1, '2019-05-20 11:12:50.823152', '127.0.0.1', '1', '<p>你好</p>', 'change', '修改 email 和 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (2, '2019-05-20 11:16:46.776515', '127.0.0.1', '1', '<span>你好</span>', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (3, '2019-05-20 16:29:35.980075', '127.0.0.1', '1', '<pre class=\"brush:python;toolbar:false\">print(&#39;hello&nbsp;world&#39;)</pre><p><img src=\"http://img.baidu.com/hi/jx2/j_0013.gif\"/></p>', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (4, '2019-05-20 16:37:25.092688', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (5, '2019-05-20 16:57:54.418403', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (6, '2019-05-20 17:28:35.989409', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (7, '2019-05-20 17:29:04.327598', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (8, '2019-05-20 17:43:12.895047', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (9, '2019-05-20 17:44:36.859185', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);
INSERT INTO `xadmin_log` VALUES (10, '2019-05-20 19:48:25.700034', '127.0.0.1', '1', '是个很反感', 'change', '修改 advices', 18, 1);

-- ----------------------------
-- Table structure for xadmin_usersettings
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `value` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES (1, 'dashboard:home:pos', '', 1);

-- ----------------------------
-- Table structure for xadmin_userwidget
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `widget_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `value` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `xadmin_userwidget_user_id_c159233a_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
