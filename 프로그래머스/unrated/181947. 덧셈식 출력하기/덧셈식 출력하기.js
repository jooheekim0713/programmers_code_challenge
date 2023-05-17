const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let sum = 0;

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    sum = Number(input[0])+ Number(input[1]);
    console.log(String(input[0] +" + "+ input[1] + " = "+ sum))
    process.exit();
});