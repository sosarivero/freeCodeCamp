'use strict';

// Formats for valid USA telephone numbers:
// 555-555-5555
// (555)555-5555
// (555) 555-5555
// 555 555 5555
// 5555555555
// 1 555 555 5555

function telephoneCheck(str) {
  const usaPhone = /^(1\s?)?(\(\d{3}\)|(\d{3}))\s?-?\d{3}-?\s?\d{4}$/;

  return usaPhone.test(str);
}
