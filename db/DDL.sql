--
-- File generated with SQLiteStudio v3.1.1 on 周五 2月 2 15:23:14 2018
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Goods
CREATE TABLE Goods (Id INTEGER PRIMARY KEY, Name TEXT, ShopId TEXT NOT NULL REFERENCES Shops (ShopId), GoodId TEXT NOT NULL UNIQUE, CreationDate DATETIME, MainPic TEXT);

-- Table: Records
CREATE TABLE Records (Id INTEGER PRIMARY KEY, date DATE NOT NULL, GoodId TEXT NOT NULL REFERENCES Goods (GoodId), sales_30 integer, fav_cnt integer, view_cnt integer, review_cnt integer);

-- Table: Shops
CREATE TABLE Shops (Id INTEGER PRIMARY KEY, Name TEXT, Link TEXT, ShopId TEXT NOT NULL UNIQUE, CreationDate DATETIME DEFAULT (datetime('now', 'localtime')));

-- Index: Goods_idx
CREATE INDEX Goods_idx ON Goods (Id, ShopId, GoodId);

-- Index: Records_idx
CREATE INDEX Records_idx ON Records (Id, date, GoodId);

-- Index: Shops_idx
CREATE INDEX Shops_idx ON Shops (Id, Name, ShopId);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
