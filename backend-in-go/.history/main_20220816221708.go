package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)
db *sql.DB,


func main() {
	db, err := sql.Open("postgres", "postgres://vhovanfzobpdbh:08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6@ec2-3-224-184-9.compute-1.amazonaws.com:5432/db56ir97s1v38l")
	if err != nil {
		panic(err)
	}

  printQueryResult(db,"select * from orders")
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected!")
}
