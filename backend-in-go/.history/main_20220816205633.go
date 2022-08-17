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

func main()
