DROP TABLE InCart;
DROP TABLE Notification;
DROP TABLE Wishlist;
DROP TABLE Referral;
DROP TABLE Review;
DROP TABLE Transaction;
DROP TABLE Product;
DROP TABLE Category;
DROP TABLE Brand;
DROP TABLE AddMoney;
DROP TABLE Orders;
DROP TABLE PaymentGateway;
DROP TABLE users;

CREATE TABLE users (
	uid INT,
	Name TEXT,
	phone CHAR(10),
	address TEXT,
	email TEXT,
	password TEXT, -- in some hashed format 
	wallet_amount INT,
	referral_token TEXT,
	--shipping_address TEXT,
	role TEXT CHECK(role='buyer' or role='seller' or role='admin'),
	Primary Key(uid)
);

CREATE TABLE Referral (
	giver_id INT,
	taker_id INT,
	Primary Key (taker_id),
	Foreign Key (giver_id) references users on delete cascade,
	Foreign Key (taker_id) references users on delete cascade
);

CREATE TABLE Category (
	category_id INT,
	name TEXT,
	category_desc TEXT,
	-- thumbnail TEXT,
	Primary Key(category_id)
);

CREATE TABLE Brand (
	brand_id INT,
	name TEXT,
	brand_desc TEXT,
	-- thumbnail TEXT,
	Primary Key (brand_id)
);


CREATE TABLE Product (
	product_id INT,
	category_id INT,
	brand_id INT,
	seller_id INT,
	advertised TEXT,
	name TEXT,
	price FLOAT,
	product_desc TEXT,
	quantity_available INT,
	discount FLOAT, -- in percentage
	images TEXT, -- url(s)
	Primary Key (product_id),
	Foreign Key (category_id) references Category on delete set null,
	Foreign Key (brand_id) references Brand on delete set null,
	Foreign Key (seller_id) references users on delete set null

);

CREATE TABLE Review (
	product_id INT,
	buyer_id INT,
	rating INT,
	review_text TEXT,
	Primary Key (buyer_id, product_id),
	Foreign Key (product_id) references Product on delete cascade,
	Foreign Key (buyer_id) references users on delete set null
);


CREATE TABLE Notification (
	notif_id INT,
	user_id INT,
	-- seen TEXT CHECK(seen='true' or seen='false'),
	seen INT, -- 0, 1
	notif_text TEXT,
	notif_timestamp TIMESTAMP,
	Primary Key(notif_id),
	Foreign Key (user_id) references users on delete cascade
);

CREATE TABLE PaymentGateway (
	payment_id INT,
	method_name TEXT,
	Primary Key(payment_id)
);

CREATE TABLE AddMoney (
	id INT,
	user_id INT,
	payment_id INT,
	amount INT,
	Primary Key (id),
	Foreign Key (user_id) references users on delete cascade,
	Foreign Key (payment_id) references PaymentGateway on delete set null
);

CREATE TABLE Orders (
	order_id TEXT,
	-- user_id INT,
	payment_id INT,
	amount INT,
	trasaction_time TIMESTAMP,
	Primary Key (order_id),
	Foreign Key (payment_id) references PaymentGateway on delete set null
	-- Foreign Key (user_id) references users on delete cascade
);

CREATE TABLE Transaction (
	seller_id INT, -- any constraint that the role is selleR??
	buyer_id INT,
	product_id INT,
	order_id TEXT,
	quantity INT CHECK (quantity>0),
	Primary Key (seller_id, buyer_id, product_id, order_id),
	Foreign Key (seller_id) references users on delete set null,
	Foreign Key (buyer_id) references users on delete cascade,
	Foreign Key (product_id) references Product on delete set null,
	Foreign Key (order_id) references Orders on delete cascade
);



CREATE TABLE InCart (
	id INT,
	buyer_id INT,
	product_id INT,
	quantity INT CHECK (quantity>0),
	Primary Key (id),
	Foreign Key (buyer_id) references users on delete cascade,
	Foreign Key (product_id) references Product on delete cascade
);

CREATE TABLE Wishlist (
	buyer_id INT,
	product_id INT,
	Primary Key (buyer_id, product_id),
	Foreign Key (buyer_id) references users on delete cascade,
	Foreign Key (product_id) references Product on delete cascade
);

drop sequence auto_increment_users;
drop sequence auto_increment_category;
drop sequence auto_increment_notif;
drop sequence auto_increment_brand;
create sequence auto_increment_users START WITH 2000 INCREMENT BY 1;
alter table users alter uid set default nextval('auto_increment_users');
-- create sequence auto_increment_products START WITH ... INCREMENT BY 1;
create sequence auto_increment_category START WITH 50 INCREMENT BY 1;
alter table users alter uid set default nextval('auto_increment_category');
create sequence auto_increment_notif START WITH 20000 INCREMENT BY 1;
alter table Notification alter notif_id set default nextval('auto_increment_notif');
create sequence auto_increment_brand START WITH 5000 INCREMENT BY 1;
alter table Brand alter brand_id set default nextval('auto_increment_brand');
-- create sequence auto_increment_order START WITH ... INCREMENT BY 1;


CREATE INDEX user_table_uid
ON users (uid);

CREATE INDEX product_pid
ON Product (product_id);

CREATE INDEX order_uid
ON Orders (order_id);

CREATE INDEX trasaction_oid
ON Transaction (order_id);

CREATE INDEX review_pid
ON Review (product_id);

CREATE INDEX addMoney_uid
ON AddMoney (user_id);