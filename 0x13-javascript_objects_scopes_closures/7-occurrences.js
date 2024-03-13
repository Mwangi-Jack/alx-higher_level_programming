#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;

  for (const i in list) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
  }

  return occurence;
};
