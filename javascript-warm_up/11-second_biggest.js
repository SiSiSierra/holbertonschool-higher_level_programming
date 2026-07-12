#!/usr/bin/node
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(0);
  process.exit(0);
}
const nums = process.argv.slice(2, process.argv.length);
nums.sort(function (a, b) { return a - b });
nums.reverse();
console.log(nums[1]);
