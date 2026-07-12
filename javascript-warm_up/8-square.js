#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
  process.exit(0);
}
for (let i = 0; i < Number(process.argv[2]); i++) {
  console.log('X'.repeat(Number(process.argv[2])));
}
