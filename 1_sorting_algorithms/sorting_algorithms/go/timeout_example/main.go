package main

import (
    "fmt"
    "time"
)

func main() {

    c1 := make(chan string, 1)
    go func() {
        time.Sleep(2 * time.Millisecond)
        c1 <- "result 1"
    }()
	fmt.Println("Called 1")

    select {
    case res := <-c1:
        fmt.Println(res)
    case <-time.After(1 * time.Second):
        fmt.Println("timeout 1")
    }

    c2 := make(chan string, 1)
    go func() {
        time.Sleep(2 * time.Second)
        c2 <- "result 2"
    }()
	fmt.Println("Called 2")
    select {
    case res := <-c2:
        fmt.Println(res)
    case <-time.After(100 * time.Millisecond):
        fmt.Println("timeout 2")
    }
}