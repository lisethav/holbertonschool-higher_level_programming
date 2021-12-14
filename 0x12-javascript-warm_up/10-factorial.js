#!/usr/bin/node
// script that computes and prints a factorial
const numb1 = parseInt(process.argv[2]);
function factorial (numb) {
  if (numb === 0) {
    return (-1);
  }
  if (numb === 1) {
    return (1);
  }
  return (numb * factorial(numb - 1));
}
console.log(factorial(numb1));
