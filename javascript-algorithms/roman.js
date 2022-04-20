'use strict';

function convertToRoman(num) {
  let roman = '';
  while (num > 0) {
    if (num / 1000 >= 1) {
      roman += 'M';
      num -= 1000;
      continue;
    } else if (num / 900 >= 1) {
      roman += 'CM';
      num -= 900;
      continue;
    } else if (num / 500 >= 1) {
      roman += 'D';
      num -= 500;
      continue;
    } else if (num / 400 >= 1) {
      roman += 'CD';
      num -= 400;
      continue;
    } else if (num / 100 >= 1) {
      roman += 'C';
      num -= 100;
      continue;
    } else if (num / 90 >= 1) {
      roman += 'XC';
      num -= 90;
      continue;
    } else if (num / 50 >= 1) {
      roman += 'L';
      num -= 50;
      continue;
    } else if (num / 40 >= 1) {
      roman += 'XL';
      num -= 40;
      continue;
    } else if (num / 10 >= 1) {
      roman += 'X';
      num -= 10;
      continue;
    } else if (num / 9 >= 1) {
      roman += 'IX';
      num -= 9;
      continue;
    } else if (num / 5 >= 1) {
      roman += 'V';
      num -= 5;
      continue;
    } else if (num / 4 >= 1) {
      roman += 'IV';
      num -= 4;
      continue;
    } else if (num / 1 >= 1) {
      roman += 'I';
      num -= 1;
      continue;
    }
  }
  return roman;
}
