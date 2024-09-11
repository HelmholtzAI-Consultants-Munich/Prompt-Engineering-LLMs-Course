fn f1(i: &str, s: i32) -> String {
    let mut e = String::new();
    let mut c = i.chars().peekable();

    while let Some(x) = c.next() {
        let mut n = 1;

        while c.peek() == Some(&x) {
            n += 1;
            c.next();
        }

        let y = f2(x, s);
        e.push_str(&format!("{}{}", n, y));
    }

    e
}

fn f2(a: char, b: i32) -> char {
    if a.is_ascii_lowercase() {
        let z = 'a' as u8;
        let o = a as u8 - z;
        let v = (o as i32 + b) % 26;
        let w = if v < 0 { v + 26 } else { v };
        return (z as i32 + w) as u8 as char;
    }
    a
}

fn main() {
    let i = "aaabbcddd";
    let s = 3;
    let e = f1(i, s);
    println!("Original: {}", i);
    println!("Encoded: {}", e);
}
