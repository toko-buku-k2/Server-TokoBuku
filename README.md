# Server-TokoBuku

> python + flask + postgresql

## Technology stack

- Python
- Flask
- PostgreSQL

## API List

- http://127.0.0.1:5127/user - [GET] - return all users
- http://127.0.0.1:5127/user/{id}/remove - [GET] - delete users with id
- http://127.0.0.1:5127/user/login - [POST] - returns user data when successfully logged in
- http://127.0.0.1:5127/user/register - [POST] - add user data with status 'user'
- http://127.0.0.1:5127/user/addpegawai - [POST] - add user data with status 'pegawai'
- http://127.0.0.1:5127/buku - [GET] - return all books
- http://127.0.0.1:5127/buku/kategori - [GET] - return all categories
- http://127.0.0.1:5127/buku/{id} - [GET] - return books with id
- http://127.0.0.1:5127/buku/cari/{key} - [GET] - returns all books with the title or category key
- http://127.0.0.1:5127/buku/{id}/remove - [GET] - delete books with id
- http://127.0.0.1:5127/buku/add - [POST] - add book data
- http://127.0.0.1:5127/buku/{id}/edit - [POST] - update book data with id
- http://127.0.0.1:5127/reting/all - [GET] - return all reting
- http://127.0.0.1:5127/reting/{idBuku} - [GET] - return all reting in book with idBuku
- http://127.0.0.1:5127/reting/{idBuku}/add - [POST] - add reting in book with idBuku
- http://127.0.0.1:5127/transaksi/all - [GET] - return all transactions
- http://127.0.0.1:5127/transaksi/all/{idUser} - [GET] - return all transactions in user with idUser
- http://127.0.0.1:5127/transaksi/add - [POST] - add transaction
- http://127.0.0.1:5127/transaksi/{id}/edit - [POST] - update status transaction with id

## Init

### 1. Create Database and Table

```bash
\i database/db.sql
```

### 2. Insert Table

```bash
\i database/master.sql
```

### 3. Change "SQLALCHEMY_DATABASE_URI"

change '5127' with your posgresql password.

```bash
SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:5127@localhost/bukuku'
```

### 4. Create venv

```bash
python -m venv venv
```

### 5. Activate venv

for windows :

```bash
venv\Scripts\activate
```

for linux :

```bash
venv\lib\activate
```

### 6. Install requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python app
```
