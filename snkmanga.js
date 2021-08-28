// https://snkmanga.com/manga/attack-on-titan-vol-3-chapter-10-wheres-the-left-arm/

// vrb = document.getElementsByClassName('alignnone size-full lazyloaded');
// [].forEach.call(vrb, function (e) { console.log(e.src) })

const http = require('https');
const fs = require('fs');

let i = 1;
let chNum = 15
chNum = (chNum < 10) ? '00' + chNum : (chNum < 100) ? '0' + chNum : chNum;

let arr = [
    'https://snkmanga.com/wp-content/uploads/2020/01/001-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/002-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/003-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/004-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/005-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/006-13.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/007-25.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/008-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/009-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/010-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/011-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/012-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/013-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/014-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/015-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/016-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/017-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/018-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/019-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/020-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/021-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/022-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/023-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/024-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/025-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/026-34.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/027-33.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/028-33.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/029-32.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/030-32.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/031-31.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/032-31.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/033-30.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/034-30.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/035-30.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/036-29.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/037-29.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/038-28.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/039-26.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/040-26.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/041-25.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/042-24.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/043-19.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/044-15.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/045-9.jpg',
    'https://snkmanga.com/wp-content/uploads/2020/01/046-6.jpg'
];
arr.forEach(function (e) {
    if (!fs.existsSync(chNum)) {
        fs.mkdirSync(chNum);
    }
    const num = (i < 10) ? '0' + i : i;
    const file = fs.createWriteStream(chNum + '/' + chNum + '-' + num + '.jpg');
    const request = http.get(e, function (response) {
        response.pipe(file);
    });
    i += 1;
})
