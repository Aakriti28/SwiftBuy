import psycopg2
import argparse
import csv
import psycopg2.extras
import numpy as np

# parser = argparse.ArgumentParser(description='Parameters for ')
# parser.add_argument('--name', type=str, help='db name')
# parser.add_argument('--user', type=str, help='username')
# parser.add_argument('--pswd', type=str, help='password')
# parser.add_argument('--host', type=str, help='host address')
# parser.add_argument('--port', type=int, help='port')
# parser.add_argument('--ddl', type=str, help='path to ddl file')
# parser.add_argument('--data', type=str, help='path to folder containing csv files')
# args = parser.parse_args()

# Connect to existing database
# conn = psycopg2.connect(dbname=args.name,user=args.user,password=args.pswd,host=args.host,port=args.port)
conn = psycopg2.connect(dbname="project",user="postgres",password="aakriti28",host="localhost",port=5432)


# Open cursor to perform db operations
cur = conn.cursor()

# install DDL
ddl = "DDL.sql"
# cur.execute(open(ddl, "r").read())





# files.append("prod_cat_brand")
# files.append("payment_gateway")
# files.append("InCart")

# files.append("AddMoney")
user_emails = set()
user_ids = set()
with open('users.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	hdr = next(reader)
	query = "INSERT INTO users (uid, Name, phone, address, email, password, wallet_amount, referral_token, role) VALUES %s ON CONFLICT DO NOTHING"	
	values_list = []
	for row in reader:
		if row[4] not in user_emails :
			user_emails.add(row[4])
			user_ids.add(row[1])
		values_list.append((row[1], row[2], row[10], row[7], row[4], row[9], row[5], row[8], row[6]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

# with open('payment_gateway.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO PaymentGateway (payment_id, method_name) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:			
# 		values_list.append((row[1],row[2]))
# 	psycopg2.extras.execute_values(cur, query, values_list)



# with open('Orders.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Orders (order_id, user_id, amount, trasaction_time, payment_id) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:
# 		values_list.append((row[4], np.random.choice(list(user_ids)), int(float(row[2])), row[3], row[1]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

# with open('AddMoney.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO AddMoney (id, user_id, payment_id, amount) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:
# 		if row[1] in user_ids :		
# 			values_list.append((row[0],row[1],row[3],row[2]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

# with open('brand.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Brand (brand_id, name, brand_desc) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:			
# 		values_list.append((row[1],row[2],row[3]))
# 	psycopg2.extras.execute_values(cur, query, values_list)


# with open('category.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Category (category_id, name, category_desc) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:			
# 		values_list.append((row[1],row[2],row[3]))
# 	psycopg2.extras.execute_values(cur, query, values_list)


# with open('products.csv','r',encoding="utf8") as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Product (category_id, brand_id, seller_id, advertised, product_id, name, price, product_desc, quantity_available, discount, images) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:			
# 		values_list.append((row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

with open('txns.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	hdr = next(reader)
	query = "INSERT INTO Transaction (seller_id, buyer_id, product_id, order_id, quantity, id) VALUES %s ON CONFLICT DO NOTHING"
	values_list = []
	for i, row in enumerate(reader):
		if row[2] in user_ids :		
			values_list.append((row[1],row[2],row[3],row[4],row[5],i))
	psycopg2.extras.execute_values(cur, query, values_list)






# with open('reviews.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Review (rating, review_text, product_id, buyer_id) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:
# 		if row[7] in user_ids :		
# 			values_list.append((row[1],row[4],row[6],row[7]))
# 	psycopg2.extras.execute_values(cur, query, values_list)


# with open('Referral.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Referral (giver_id, taker_id) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:
# 		if row[1] in user_ids and row[2] in user_ids :	
# 			values_list.append((row[1],row[2]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

# with open('Wishlist.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Wishlist (buyer_id, product_id) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:
# 		if row[1] in user_ids :				
# 			values_list.append((row[1],row[2]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

# with open('InCart.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO InCart (buyer_id, product_id, quantity) VALUES %s ON CONFLICT DO NOTHING"
# 	values_list = []
# 	for row in reader:	
# 		if row[1] in user_ids :			
# 			values_list.append((row[1],row[2],row[3]))
# 	psycopg2.extras.execute_values(cur, query, values_list)


# with open('notifs.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hdr = next(reader)
# 	query = "INSERT INTO Notification (notif_id, seen, notif_text, notif_timestamp, user_id) VALUES %s"
# 	values_list = []
# 	for row in reader:
# 		if row[1] in user_ids :		
# 			values_list.append((row[0], row[2], "You have received a notification!", row[4], row[1]))
# 	psycopg2.extras.execute_values(cur, query, values_list)

conn.commit()
cur.close()
conn.close()