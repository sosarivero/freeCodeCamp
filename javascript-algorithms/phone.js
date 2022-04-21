'use strict';

// 555-555-5555
// (555)555-5555
// (555) 555-5555
// 555 555 5555
// 5555555555
// 1 555 555 5555

function telephoneCheck(str) {
  const test1 = /^(1\s?)?(\(\d{3}\)|(\d{3}))\s?-?\d{3}-?\s?\d{4}$/;

  return test1.test(str);
}

console.log(telephoneCheck('1 555 555 5555'));
