mod lib;
use crate::lib::Parser;

use std::io::{self, Read};


fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_to_string(&mut buffer)?;
    let (s, exp) = lib::expr().parse(&buffer).expect("Nothing");
    println!("{}", lib::eval(exp));
    Ok(())    
}
