use std::io;




fn main() {

	
	
	
	let mut inp = String::new();
	
	
	println!("enter the emai ID to be checked :");
	

	match io::stdin().read_line(&mut inp) {
		Ok(_) => {
			println!("the email you entered is  {}",inp);
		},
		Err(e) => println!("oopsie  {}",e)
	}

	
	let foo = inp.trim_end();
	
	let b = inp.contains("@");   // this is working fine
	
	println!(" has the @ -- {}, ", b);
	
	
	
	
	let a = foo.ends_with(".com");  //for some reason this isn't wrorking, it's always returning false 
	
	println!("has the .com suffix  -- {}, ", a);
	
	

	if (b == true) && (a == true)  {
		println!(" its a valid email ");

	} 
	else {
		println!("not a valid email");
	}
}

