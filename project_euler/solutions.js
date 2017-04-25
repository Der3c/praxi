/* Find the sum of all the multiples of 3 or 5 below 1000. */

var total = 0
for (var i = 1; i < 1000; i++) {
  if (i % 3 == 0 || i % 5 == 0)
    total += i;
}
console.log(total);
/* Problem #1 End */

/* By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. */
/* Classic expression is Fn = Fn-1 + Fn-2. will use seed values 0 * 1 */
function sumFibbo(limit) {
  var sum = 0, a = 0, b = 1, f;

  while (b < limit) {
    f = a;
    a = b;
    b += f;

    if (b % 2 == 0)
    sum += b;
  }
  return sum;
}
console.log(sumFibbo(4000000));
/* Problem #2 End */
