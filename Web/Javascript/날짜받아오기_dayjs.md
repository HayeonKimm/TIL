const dayjs = require('dayjs');

const now = dayjs();
let time = now.format();
time = time.slice(0, 10).split('T').join(' ');

console.log(time);
