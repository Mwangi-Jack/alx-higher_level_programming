const fs = require('fs');

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const outputPath = process.argv[4];

const file1Contents = fs.readFileSync(file1Path, 'utf8');
const file2Contents = fs.readFileSync(file2Path, 'utf-8');

const outputFileContents = `${file1Contents} \n ${file2Contents}`;

fs.writeFileSync(outputPath, outputFileContents);
