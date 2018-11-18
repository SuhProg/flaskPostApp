DROP TABLE if EXISTS posts;
	CREATE TABLE posts (
		id integer primary key autoincrement,
		name text NOT NULL,
		content text NOT NULL		
);
