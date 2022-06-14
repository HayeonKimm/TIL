npm i prettier -D


module.exports = {
  trailingComma: 'es5',
  tabWidth: 2,
  semi: true,
  singleQuote: true,
  arrowParens: 'always',
};


- script 

"prettify": "prettier --write *.js **/*.js"+



npm run prettify
