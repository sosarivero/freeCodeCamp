function checkCashRegister(price, cash, cid) {
  let funds = cid.reduce((sum, current) => sum + current[1], 0);
  let change = cash - price;

  let result = {};

  return change;
}

function cashArray(money) {
  array = [
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

  while (money > 0) {
    if (money / 100 >= 1) {
      array[8][1] += 100;
      money -= 100;
      continue;
    } else if (money / 20 >= 1) {
      array[7][1] += 20;
      money -= 20;
      continue;
    } else if (money / 10 >= 1) {
      array[6][1] += 10;
      money -= 10;
      continue;
    } else if (money / 5 >= 1) {
      array[5][1] += 5;
      money -= 5;
      continue;
    } else if (money / 1 >= 1) {
      array[4][1] += 1;
      money -= 1;
      continue;
    } else if (money / 0.25 >= 1) {
      array[3][1] += 0.25;
      money -= 0.25;
      continue;
    } else if (money / 0.1 >= 1) {
      array[2][1] += 0.1;
      money -= 0.1;
      continue;
    } else if (money / 0.05 >= 1) {
      array[1][1] += 0.05;
      money -= 0.05;
      continue;
    } else {
      array[0][1] += Math.round(money * 100) / 100;
      money = 0;
    }
  }

  return array;
}

checkCashRegister(19.5, 20, [
  ['PENNY', 1.01],
  ['NICKEL', 2.05],
  ['DIME', 3.1],
  ['QUARTER', 4.25],
  ['ONE', 90],
  ['FIVE', 55],
  ['TEN', 20],
  ['TWENTY', 60],
  ['ONE HUNDRED', 100],
]);

console.log(cashArray(20));
