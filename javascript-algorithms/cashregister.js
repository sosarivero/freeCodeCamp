'use strict';

function checkCashRegister(price, cash, cid) {
  // Use reduce to get the total amount of money in the cash register.
  let funds = cid.reduce((sum, current) => sum + current[1], 0);
  // The change that is owed to the client.
  let change = cash - price;

  let result = {};

  // The actual change that will be given, taken from the cash register.
  let changeToGive = cashArray(change, cid);

  if (funds < change || !changeToGive) {
    result.status = 'INSUFFICIENT_FUNDS';
    result.change = [];
    // Use JSON.stringify to compare multi-dimensional arrays.
  } else if (JSON.stringify(cid) === JSON.stringify(changeToGive)) {
    result.status = 'CLOSED';
    result.change = changeToGive;
  } else {
    result.status = 'OPEN';
    result.change = changeToGive
      .filter((currency) => currency[1] > 0)
      .reverse(); // Need to use .reverse() because of grader... not sure why.
  }

  return result;
}

function cashArray(money, cashregister) {
  let array = [
    ['PENNY', 0],
    ['NICKEL', 0],
    ['DIME', 0],
    ['QUARTER', 0],
    ['ONE', 0],
    ['FIVE', 0],
    ['TEN', 0],
    ['TWENTY', 0],
    ['ONE HUNDRED', 0],
  ];

  // Use JSON.parse(JSON.stringify()) to deeply copy the multidimensional array.
  let cid = JSON.parse(JSON.stringify(cashregister));

  // This is basically copied from my Roman numerals project in FCC.
  while (money > 0) {
    if (money / 100 >= 1 && cid[8][1] > 0) {
      array[8][1] += 100;
      cid[8][1] -= 100;
      money -= 100;
      continue;
    } else if (money / 20 >= 1 && cid[7][1] > 0) {
      array[7][1] += 20;
      cid[7][1] -= 20;
      money -= 20;
      continue;
    } else if (money / 10 >= 1 && cid[6][1] > 0) {
      array[6][1] += 10;
      cid[6][1] -= 10;
      money -= 10;
      continue;
    } else if (money / 5 >= 1 && cid[5][1] > 0) {
      array[5][1] += 5;
      cid[6][1] -= 5;
      money -= 5;
      continue;
    } else if (money / 1 >= 1 && cid[4][1] > 0) {
      array[4][1] += 1;
      cid[4][1] -= 1;
      money -= 1;
      continue;
    } else if (money / 0.25 >= 1 && cid[3][1] > 0) {
      array[3][1] += 0.25;
      cid[3][1] -= 0.25;
      money -= 0.25;
      continue;
    } else if (money / 0.1 >= 1 && cid[2][1] > 0) {
      array[2][1] += 0.1;
      cid[2][1] -= 0.1;
      money -= 0.1;
      continue;
    } else if (money / 0.05 >= 1 && cid[1][1] > 0) {
      array[1][1] += 0.05;
      cid[1][1] -= 0.05;
      money -= 0.05;
      continue;
    } else if (cid[0][1] >= money) {
      array[0][1] += Math.ceil(money * 100) / 100;
      cid[0][1] = 0;
      money = 0;
      continue;
    } else {
      // Return false in case that there is not enough cash in the register.
      return false;
    }
  }
  return array;
}
