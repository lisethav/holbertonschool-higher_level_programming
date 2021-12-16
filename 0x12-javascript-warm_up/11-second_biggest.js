#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const numb = process.argv.slice(2);
if (numb.length < 2) {
  console.log(0);
} else {
  numb.sort((a, b) => a - b);
  numb.pop();
  console.log(numb.pop());
}
