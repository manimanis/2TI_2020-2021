hljs.registerLanguage('algorithm', (hljs) => {
  return {
    name: 'algorithm',
    case_insensitive: true, 
    aliases: ['alg'],
    lexemes : '[àéèêâäöüÄÖÜßa-zA-Z]+',
    keywords: {
      keyword: 'début afficher lire si alors sinon fin tantque faire répéter jusqua mod div',
      literal: 'faux vrai nul'
    },
    contains: [
      {
        className: 'string',
        begin: '"', end: '"'
      },
      hljs.C_LINE_COMMENT_MODE,
      hljs.C_NUMBER_MODE
    ]
  };
});

