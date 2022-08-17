package main

import (
  "database/sql"
  "fmt"

  _ "github.com/lib/pq"
)

const(
host = 'localhost'
port=5432
user = 'postgres'
password = ''
dbname = "first_db"
)

unc main() {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	  "password=%s dbname=%s sslmode=disable",
	  host, port, user, password, dbname)
  }
