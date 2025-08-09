// Password that has atleast 8 characters (atleast 1 capital and 1 small letter), and has alteast 1 special character

package main


import (
	"fmt"
	"unicode"
)

func LengthCheck(pwd string) bool {
	if len(pwd) >= 8 {
		return true
	} else {
		return false
	}
}

func ContainsUpperCase(pwd string) bool {
	runes := []rune(pwd)

	for i := 0; i < len(pwd); i++ {
		if unicode.IsUpper(runes[i]) {
			return true
		}
	}
	fmt.Println("Does not cantain an upper case")
	return false
}

func ConatainsLowerCase(pwd string) bool {
	runes := []rune(pwd)
	for i := 0; i < len(pwd); i++ {
		if unicode.IsLower(runes[i]) {
			return true
		}
	}
	fmt.Println("Does not contain lower case")
	return false
}

func ContainSpecialChar(pwd string) bool {
	runes := []rune(pwd)

	for i := 0; i < len(pwd); i++ {
		if unicode.IsPunct(runes[i]) {
			return true
		}
	}
	fmt.Println("Does not contain a special character")
	return false
}
