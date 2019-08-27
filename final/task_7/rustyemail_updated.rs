use std::io;

use std::ops::Not;



fn main() {

	
	
	
	let mut inp = String::new();
	
	
	println!("enter the emai ID to be checked :");
	

	match io::stdin().read_line(&mut inp) {
		Ok(_) => {
			println!("the email you entered is  {}",inp);
		},
		Err(e) => println!("oopsie  {}",e)
	}

	
	let foo = inp.trim_end();  // remove trailing whitespaces
	
	let b = inp.contains("@");   

	let v = inp.contains("@.");   // invalid email provider 
	
	let a = foo.ends_with(".com");  // suffix
	
	let p = foo.ends_with(".edu");  
	
	let q = foo.starts_with("@");  // invalid username
	
	println!(" has the .com /.edu suffix -- {}, ", a | p);
	println!(" has the @ --                 {}, ", b);
	println!(" has  a valid username --     {}, ", q.not());
	println!(" has a valid email client  -- {}, ", v.not());
	

	if (b == true) && ((a == true) | (p == true)) && ( v == false) && (q == false)  {
		println!(" its a valid email ");

	} 
	else {
		println!(" not a valid email");
	}
}

