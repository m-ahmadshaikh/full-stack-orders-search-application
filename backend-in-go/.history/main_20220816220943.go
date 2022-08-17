package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

func printQueryResult(db *sql.DB, query string) error {
  rows, err := db.Query(query)
  if err != nil {
      return fmt.Errorf("canot run query %s: %w", query, err)
  }
  defer rows.Close()

  cols, _ := rows.Columns()
  row := make([]interface{}, len(cols))
  rowPtr := make([]interface{}, len(cols))
  for i := range row {
      rowPtr[i] = &row[i]
  }
  fmt.Println(cols)
  for rows.Next() {
      err = rows.Scan(rowPtr...)
      if err != nil {
          fmt.Println("cannot scan row:", err)
      }
      fmt.Println(row...)
  }
  return rows.Err()
}

func main() {
	db, err := sql.Open("postgres", "postgres://vhovanfzobpdbh:08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6@ec2-3-224-184-9.compute-1.amazonaws.com:5432/db56ir97s1v38l")
	if err != nil {
		panic(err)
	}

  printQueryResult(db,)
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected!")
}
