extern crate regex;

use regex::Regex;

fn main()
	 {
    use std::io::{stdin,stdout,Write};


    let mut mail=String::new();


    print!("Enter email id  : ");


    let _=stdout().flush();


    stdin().read_line(&mut mail).expect("error: unable to read user input");


	if Regex::new(r"^[a-zA-Z0-9]+@[a-z][.]?[a-z]*").unwrap().is_match(&mut mail) == true
	{

	    println!("valid ");

	}
	else
	{

	    println!("not valid ");

	}
}
