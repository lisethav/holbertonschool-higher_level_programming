#!/usr/bin/node
// script that prints the addition of 2 integers
const numb1 = parseInt(process.argv[2])
const numb2 = parseInt(process.argv[3])
function add (a, b) {
    console.log(a + b)
}
add(numb1, numb2)
