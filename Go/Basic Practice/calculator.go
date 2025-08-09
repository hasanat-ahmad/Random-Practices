package main

import "fmt"


func Cal() {
	fmt.Println("1. Add")
	fmt.Println("2. Subtract")
	fmt.Println("3. Multiply")
	fmt.Println("4. Divide")

	var choice int
	for {
		fmt.Print("\nEnter your choice :")
		fmt.Scanln(&choice)

		if choice >= 1 && choice <= 4 {
			var num1 int
			var num2 int
			fmt.Println("Enter first number: ")

			fmt.Scanln(&num1)

			fmt.Println("Enter second number: ")
			fmt.Scanln(&num2)

			if choice == 1 {
				fmt.Print(num1, " + ", num2, " = ", num1+num2)
			} else if choice == 2 {
				fmt.Print(num1, " - ", num2, " = ", num1-num2)
			} else if choice == 3 {
				fmt.Print(num1, " * ", num2, " = ", num1*num2)
			} else if choice == 4 {
				if num2 == 0 {
					fmt.Println("Divisor cannot be 0")
				} else {
					fmt.Print(num1, " / ", num2, " = ", num1/num2)
				}
			}
		} else {
			fmt.Print("Invalid input")
			break
		}
	}

}
