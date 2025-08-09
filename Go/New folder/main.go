package main
import ("fmt")

func main()  {
  person := Person{
    "hasanat", 20, "abc",
  }

  person.setAge(30)
  fmt.Println(person)
}