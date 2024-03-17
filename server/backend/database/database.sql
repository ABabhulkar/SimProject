CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(50),
  role VARCHAR(50) NOT NULL DEFAULT 'user',
  email VARCHAR(255) NOT NULL,
  metadata JSON,
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE TABLE IF NOT EXISTS game (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255),
  result_metric JSON NOT NULL,
  other JSON,
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE TABLE IF NOT EXISTS game_entries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user INTEGER NOT NULL REFERENCES user(id),
  game INTEGER NOT NULL REFERENCES game(id),
  shortname VARCHAR(255) NOT NULL,
  filepath VARCHAR(255) NOT NULL,
  isvalid bool NOT NULL DEFAULT false,
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE TABLE IF NOT EXISTS game1_leaderboard (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user JSON COMMENT '{username:str}',
  game JSON COMMENT '{name:str ,filepath:str, shortname:str}',
  ranking INTEGER,
  score INTEGER,
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE TABLE IF NOT EXISTS game_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  game INTEGER NOT NULL REFERENCES game(id),
  round_score JSON COMMENT '[{P1:{move:int,score:int},P2:{move:int,score:int}}]',
  timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);