package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

const (
	host     = "ec2-3-224-184-9.compute-1.amazonaws.com"
	port     = 5432
	user     = "vhovanfzobpdbh"
	password = "08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6"
	dbname   = "db56ir97s1v38l"
)

func main() {
	// psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
	// 	"password=%s dbname=%s sslmode=disable",
	// 	host, port, user, password, dbname)
	db, err := sql.Open("postgres", "postgres://vhovanfzobpdbh:08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6@ec2-3-224-184-9.compute-1.amazonaws.com:5432/db56ir97s1v38l")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected!")
}
