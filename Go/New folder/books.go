package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Book struct {
	Title  string
	Author string
	Price  int
}

func CheckPrice(b Book) {
	if b.Price > 500 {
		fmt.Println("Price is above 500")
	} else {
		fmt.Println("Below 500")
	}
}

func askDetails() {
    reader := bufio.NewReader(os.Stdin)

    fmt.Print("Enter book title: ")
    title, _ := reader.ReadString('\n')
    title = strings.TrimSpace(title)

    fmt.Print("Enter author: ")
    author, _ := reader.ReadString('\n')
    author = strings.TrimSpace(author)

    fmt.Print("Enter price: ")
    priceStr, _ := reader.ReadString('\n')
    priceStr = strings.TrimSpace(priceStr)
    price, err := strconv.Atoi(priceStr)
    if err != nil {
        fmt.Println("Invalid price. Please enter a number.")
        return
    }

    fmt.Printf("Book Title: %s\nAuthor: %s\nPrice: %d\n", title, author, price)
}