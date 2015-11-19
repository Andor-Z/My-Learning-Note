drop table if exists entries;
creattable entries(
	id     integer primary key autoincrement,
	title  string NOT NULL,
	text string NOT NULL
	);