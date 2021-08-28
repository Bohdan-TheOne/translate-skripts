// https://snkmanga.com/manga/attack-on-titan-vol-3-chapter-10-wheres-the-left-arm/

// vrb = document.getElementsByClassName('alignnone size-full lazyloaded');
// [].forEach.call(vrb, function (e) { console.log(e.src) })

const http = require('https');
const fs = require('fs');

let chNum = 30;
let num = 45
let path = 'https://cdn.readsnk.com/file/mangap/5/100' + chNum + '000/'


function formatNumber(num, length) {
    if (length <= ("" + num).length) { return "" + num }
    return "0".repeat(length - ("" + num).length) + num
}

chNum = formatNumber(chNum, 3)

for (let i = 1; i <= num; i++) {
    if (!fs.existsSync(chNum)) {
        fs.mkdirSync(chNum);
    }
    const file = fs.createWriteStream(chNum + '/' + formatNumber(i, 2) + '.jpg');
    const request = http.get(path + i + '.jpg', function (response) {
        response.pipe(file);
    });
}
