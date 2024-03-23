package main

import (
	"log"
	"os"
	"time"
)

func main() {
	original := "example1.log"
        rotated := "example2.log"
	for {
		os.Remove(rotated)

		time.Sleep(1 * time.Second)

		os.Rename(original, rotated)

		time.Sleep(1 * time.Second)

		os.Create(original)

		log.Printf("%s -> %s\n", original, rotated)
	}

}

// https://imagawa.hatenadiary.jp/entry/2016/12/15/190000
