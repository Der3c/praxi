/* creat a lopp that prints out a triangle */
var counter = 1;
for (var pyr = "#"; counter <= 7; counter++) {
  console.log(pyr);
  pyr += "#";
}
/* end exercise */

/* my first shot at answering the fizzbuzz test. Return to this later if you come up with a more elegant solution. It works! */
for (var i = 0; i <=100; i++) {
  if (i % 3 == 0 && i % 5 == 0)
    console.log("FizzBuzz");
  else if (i % 3 == 0)
    console.log("Fizz");
  else if (i % 5 == 0)
    console.log("Buzz");
  else
    console.log(i);
  };
/* There has to be a way to do this more effeciently, maybe ternary? */

/* Printing a chess board */
var size = 8
var square = " "
for (var y = 0; y <= size; y++) {
  for (var x = 0; x <=size; x++) {
    if ((x + y) % 2 == 0)
      square += " ";
    else
      square += "#";
  }
  square += "\n";
}
console.log(square);
/* End exercise */

/* Project Euler - Find the sum of all multiples of 3 and 5 below 1000 */
var total = 0
for (var i = 1; i <= 1000; i++) {
  if (i % 3 == 0 || i % 5 == 0)
    total += i;
}

console.log(total);
/* Could ommit the equal to symbol in the for statement */
