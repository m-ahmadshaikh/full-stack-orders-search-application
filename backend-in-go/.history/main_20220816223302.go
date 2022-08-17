package main

import (
	"database/sql"
  "encoding/json"
    "fmt"
    "log"
    "net/http"

    "github.com/gorilla/mux"
    _ "github.com/lib/pq"
)

// Function for handling errors
func checkErr(err error) {
  if err != nil {
      panic(err)
  }
}

func setupDB() *sql.DB {
  db, err := sql.Open("postgres", "postgres://vhovanfzobpdbh:08761f73371f52f8ffe9b6ce9878fe96f9135c81ee8e7e42dc6acf7b1dd3f9c6@ec2-3-224-184-9.compute-1.amazonaws.com:5432/db56ir97s1v38l")
  checkErr(err)
  return db
}

func getJSON(db *sql.DB, sqlString string) (string, error) {
	rows, err := db.Query(sqlString)
	if err != nil {
		return "", err
	}
	defer rows.Close()
	columns, err := rows.Columns()
	if err != nil {
		return "", err
	}
	count := len(columns)
	tableData := make([]map[string]interface{}, 0)
	values := make([]interface{}, count)
	valuePtrs := make([]interface{}, count)
	for rows.Next() {
		for i := 0; i < count; i++ {
			valuePtrs[i] = &values[i]
		}
		rows.Scan(valuePtrs...)
		entry := make(map[string]interface{})
		for i, col := range columns {
			var v interface{}
			val := values[i]
			b, ok := val.([]byte)
			if ok {
				v = string(b)
			} else {
				v = val
			}
			entry[col] = v
		}
		tableData = append(tableData, entry)
	}
	jsonData, err := json.Marshal(tableData)
	if err != nil {
		return "", err
	}
	fmt.Println(string(jsonData))
	return string(jsonData), nil
}

func main() {
	router := mux.NewRouter()

  fmt.Println("Server at 8080")
    log.Fatal(http.ListenAndServe(":8000", router))
}
