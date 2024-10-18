package main
import "fmt"

func main() {
  number := 8
  fmt.Printf("The number of possible proper fractions is %v\n", ETF(number))
}

func ETF(val int) int{
  if val == 1 {
    return 0
  }

  answer := val
  p := 2
  for p*p <= val {
    if val % p==0 {
      for val % p==0 {
        val /= p
      }
      answer -= answer/p
    }
    p += 1
  }

  if val > 1 {
    answer -= answer/val
  }

  return answer
}
