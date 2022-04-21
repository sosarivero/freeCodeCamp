'use strict';

function rot13(str) {
  let decodified = '';

  Array.from(str).forEach((char) => {
    if (char.match(/[A-Z]/)) {
      // Get the "index" of the letter in the alphabet, from 1 to 26.
      // A in UNICODE = 65.
      let n = char.charCodeAt() - 64 - 13;
      // To handle the "negative overflow" off the alphabet...
      if (n <= 0) n += 26;
      // Get the correct UNICODE by adding back the 64.
      decodified += String.fromCharCode(n + 64);
      // If it's not an uppercase letter, just add it to the string.
    } else {
      decodified += char;
    }
  });
  return decodified;
}
