package main

type Car struct{
	Name string
	model string
	yearOfRelease int
}

func getCarName(c Car) string {
	return c.Name
}

func getCarModel(c Car) string {
	return c.model
}