package main

import "fmt"

func InsertElement(arr []int, number int) {
	for i := 0; i < len(arr); i++ {
		if arr[i] == 0 {
			arr[i] = number
			fmt.Println(number, "added to index", i)
			break
		}
	}
}

func DeleteElement(arr []int, number int) {
	for i := 0; i < len(arr); i++ {
		if arr[i] == number {
			arr[i] = 0
			fmt.Println(number, "deleted from index", i)

			break
		}
	}
}

func SearchElement(arr []int, number int) {
	found := false
	for i := 0; i < len(arr); i++ {
		if arr[i] == number {
			fmt.Println(number, "found at index", i)
			found = true
		}
	}
	if !found {
		fmt.Println(number, "not found")
	}
}

func UpdateElement(arr []int, number int, index int) {
	updated := false

	for i := 0; i < len(arr); i++ {
		if i == index {
			arr[i] = number
			updated = true
			fmt.Println(number, "updated at index", i)
		}
	}
	if !updated {
		fmt.Println("Number not updated")
	}
}
