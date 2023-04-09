//문제: 1356
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let answer = "NO";
  const arr = input[0].split("").map(Number);
  for (let i = 0; i < arr.length; i++) {
    let a = 1;
    let b = 1;
    for (let p = 0; p <= i; p++) {
      a *= arr[p];
    }
    for (let q = arr.length - 1; q > i; q--) {
      b *= arr[q];
    }
    if (a === b) answer = "YES";
  }
  console.log(answer);
}
