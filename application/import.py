import csv


from flask_sqlalchemy import SQLAlchemy
engine = create_engine("postgres://rioxhygwbwemti:e7a86e1f6e1691315eb9a00b77105952a3c9756852f310780d00302abd1e1908@ec2-174-129-22-84.compute-1.amazonaws.com:5432/d1s2v7fpgo4ntn")
db = scoped_session(sessionmaker(bind=engine))

def main():
	try:
		db.execute("SELECT * FROM Books")
	except Exception:
		db.execute("CREATE TABLE Books(Id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, artist VARCHAR NOT NULL, year INTEGER NOT NULL)")
		f = open("books.csv")
		reader = csv.reader(f)
	n=0
	for isbn, title, author, year in reader:
		db.execute("INSERT INTO books(isbn, title, author, year) VALUES(:isbn,:title,:author,:year)", {"isbn": isbn, "title": title, "author": author, "year": year})
		print(f"Added {title} to book database")
		n += 1
		if n == 300:
			break
	db.commit()
if __name__=='__main__':
	main()