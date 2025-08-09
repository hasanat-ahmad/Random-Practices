package main

import "fmt"

type Person struct {
	Name string
	Age  int
	Email   string
}

func (p *Person) setAge(age int){
	p.Age = age
}

func (p Person) DisplayDetails() {
	fmt.Println("Name: ", p.Name)
	fmt.Println("Age: ", p.Age)
	fmt.Println("Email: ", p.Email)
}