package main

import  (
    "github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
    "os"
    "flag"
    "fmt"

)


func main() {


    var handle string 
    fmt.Println(" Enter twitter handle ")
    fmt.Scanln(&handle)   // takes input on handle var 

    t_name := flag.String("twitter handle", handle, " contains the twitter handle ")

    flag.Parse()
    config := oauth1.NewConfig("mXDKLkeWnsbsCGZLTRvQMksTI", "EAP4YWKRTlhcWQUhIkGSQ2bNllJUMZBen1JdM6E2gkbHlvVlmY")
    token := oauth1.NewToken("1173614657132625920-llVlJGTyllfXCQfi5GP5dTAoJ0drXA", "rsWbfecAVwTphHZPRPs1UK0CXGFrbvuLqEGVQL9AmNaPr")
    

    httpClient := config.Client(oauth1.NoContext, token)

    client := twitter.NewClient(httpClient)
    // User Show

    f, err := os.Create("userhandler.txt")

    params := &twitter.FollowerListParams{
        ScreenName: *t_name,
    }
    

    // Followers
    followers, resp, err := client.Followers.List(params)

    var count int = 0;
    fmt.Println(resp, err)

    f.WriteString(*t_name)     // user name 

    for _, follower := range followers.Users {
        count++
        f.WriteString("\n"+ follower.ScreenName)
    }
    f.WriteString("\n")
    f.WriteString(fmt.Sprintf("\n", count))
    f.Close()


    



}