//문제: 11383
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [a, b] = input[0].split(" ").map(Number);
  const original = [];
  const new_one = [];
  for (let i = 1; i <= a; i++) {
    let temp = [];
    input[i].split("").forEach((e) => {
      temp.push(e);
      temp.push(e);
    });
    original.push(temp);
  }
  for (let i = a + 1; i <= 2 * a; i++) {
    new_one.push(input[i].split(""));
  }
  //   console.log(original, new_one);
  let answer = "Eyfa";
  for (let i = 0; i < a; i++) {
    original[i].forEach((e, idx) => {
      if (e !== new_one[i][idx]) answer = "Not Eyfa";
    });
  }

  console.log(answer);
}
