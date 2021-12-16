#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const numb = process.argv;
if (numb.length === 2 || numb.length === 3) {
  console.log(0);
} else {
  const array = [];
  for (let a = 0; a < numb.lenght; a++) {
    if (!isNaN(parseInt(numb[a]))) {
      array.push(parseInt(numb[a]));
    }
  }
  const large = Math.max(...array);
  const init = array.indexOf(large);
  array.splice(init, 1);
  const second = Math.max(...array);
  console.log(second);
}
