package main

import "fmt"


func FindingMaxInArray(arr []int) int {
	
	var max int = arr[0]
	for i := 0; i < len(arr); i++{
		if arr[i] > max{
			max = arr[i]
		}
	}
	fmt.Println("Max in array is", max)
	return max
}

func FindingMinInArray(arr []int) int {
	
	var min int = arr[0]
	for i := 0; i < len(arr); i++{
		if arr[i] < min{
			min = arr[i]
		}
	}
	fmt.Println("Min in array is", min)
	return min
}
