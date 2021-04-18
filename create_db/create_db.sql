

DROP TABLE IF EXISTS ogranizations;
CREATE TABLE ogranizations(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	inn INTEGER,
	created_at INTEGER,
	udated_at INTEGER
);


DROP TABLE IF EXISTS contractors;
CREATE TABLE contractors(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	inn INTEGER,
	created_at INTEGER
);


DROP TABLE IF EXISTS builders;
CREATE TABLE builders(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	inn INTEGER,
	created_at INTEGER
);


DROP TABLE IF EXISTS projects;
CREATE TABLE projects(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	organization_id INTEGER NOT NULL,
	created_at INTEGER,
	FOREIGN KEY (organization_id) REFERENCES ogranizations(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);


DROP TABLE IF EXISTS workpacks;
CREATE TABLE workpacks(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL
);


DROP TABLE IF EXISTS contracts;
CREATE TABLE contracts(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	organization_id INTEGER NOT NULL,
	contractors_id INTEGER NOT NULL,
	from_date INTEGER NOT NULL,
	created_at INTEGER,
	FOREIGN KEY (organization_id) REFERENCES ogranizations(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (contractors_id) REFERENCES contractors(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);

DROP TABLE IF EXISTS specs;
CREATE TABLE specs(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	contract_id INTEGER NOT NULL,
	workpack_id INTEGER NOT NULL,
	amount REAL NOT NULL,
	FOREIGN KEY (contract_id) REFERENCES contracts(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (workpack_id) REFERENCES workpacks(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);


DROP TABLE IF EXISTS types;
CREATE TABLE types(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL
);


DROP TABLE IF EXISTS services;
CREATE TABLE services(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	title VARCHAR(255) NOT NULL,
	type_id INTEGER NOT NULL,
	created_at INTEGER,
	FOREIGN KEY (type_id) REFERENCES types(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);


DROP TABLE IF EXISTS applications;
CREATE TABLE applications(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	from_date INTEGER NOT NULL,
	to_date INTEGER NOT NULL,
	project_id INTEGER NOT NULL,
	contract_id INTEGER NOT NULL,
	workpack_id INTEGER NOT NULL,
	type_id INTEGER NOT NULL,
	service_id INTEGER NOT NULL,
	builder_id INTEGER NOT NULL,
	responsible VARCHAR(255), 
	FOREIGN KEY (project_id) REFERENCES projects(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (contract_id) REFERENCES contracts(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (workpack_id) REFERENCES workpacks(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (type_id) REFERENCES types(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (service_id) REFERENCES services(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (builder_id) REFERENCES builders(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);




