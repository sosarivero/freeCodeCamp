'use strict';

function palindrome(str) {
  // In regex you need to specify '_', because somehow it's not included in \W
  const modifiedString = str.replace(/[\W_]/g, '').toLowerCase();

  let reversed = modifiedString.split('').reverse().join('');

  return reversed == modifiedString;
}

palindrome('_eye');
