package main

import "fmt"

func Array() {
	var marks [5]int = [5]int{1, 2, 4, 5}
	// var marks = [5]int{1, 2, 4, 5}                   the 6th and 7th line are the same. 7th line is preferable
	// marks := [5]int{1, 2, 4, 5} 					 	the 6th and 8th line are the same. 8th line is preferable
	fmt.Println(marks)
	fmt.Println("Length of array is", len(marks))
	fmt.Println("Capacity of array is", cap(marks))
}

func slices() {
	var marks = []int{1, 2, 4, 5, 0}
	fmt.Println("Length of array is", len(marks))
	fmt.Println("Capacity of array is", cap(marks))
	fmt.Println(marks)
}

func rangeOne() {
	marks := [5]int{1, 2, 4, 5, 0}
	rangeOne := marks[1:3] // range is basically a part of array or slice that you want to access
	fmt.Println(rangeOne)
}
