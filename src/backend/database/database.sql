-- SQLite
CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(50),
  role VARCHAR(50) NOT NULL DEFAULT 'user',
  email VARCHAR(255) NOT NULL,
  metadata JSON,
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE TABLE IF NOT EXISTS `game` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(255),
  `result_metric` json NOT NULL,
  `other` json,
  `timestamp` long DEFAULT (now())
);

CREATE TABLE IF NOT EXISTS `game_entries` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user` int,
  `game` int,
  `shortname` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL,
  `isvalid` bool NOT NULL DEFAULT false,
  `timestamp` long DEFAULT (now())
);

CREATE TABLE IF NOT EXISTS `game1_leaderboard` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user` json COMMENT '{username:str}',
  `game` json COMMENT '{name:str ,filepath:str, shortname:str}',
  `ranking` int,
  `score` int,
  `timestamp` long DEFAULT (now())
);

CREATE TABLE IF NOT EXISTS `game_history` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `game` int,
  `round_score` json COMMENT '[{P1:{move:int,score:int},P2:{move:int,score:int}}]',
  `timestamp` long DEFAULT (now())
);

ALTER TABLE `game_entries` ADD FOREIGN KEY (`user`) REFERENCES `user` (`id`);

ALTER TABLE `game_entries` ADD FOREIGN KEY (`game`) REFERENCES `game` (`id`);

ALTER TABLE `game_history` ADD FOREIGN KEY (`game`) REFERENCES `game` (`id`);
