

german_stopwords = [
    'ab', 'aber', 'abermals', 'abgerufen', 'acht', 'achte', 'achten', 'achter', 'achtes', 'ag',
    'alle', 'allein', 'allem', 'allen', 'aller', 'allerdings', 'alles', 'allgemeinen', 'als', 'also',
    'am', 'an', 'ander', 'andere', 'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern',
    'anderr', 'anders', 'au', 'auch', 'auf', 'aus', 'ausser', 'außer', 'ausserdem', 'außerdem',
    'bald', 'bei', 'beide', 'beiden', 'beim', 'beispiel', 'bekannt', 'bereits', 'besonders', 'besser',
    'besten', 'bin', 'bis', 'bisher', 'bist', 'dabei', 'dadurch', 'dafür', 'dagegen', 'daher', 'dahin',
    'dahinter', 'damals', 'damit', 'danach', 'daneben', 'dank', 'dann', 'daran', 'darauf', 'daraus',
    'darf', 'darfst', 'darin', 'darüber', 'darum', 'darunter', 'das', 'dass', 'dasselbe', 'davon',
    'davor', 'dazu', 'dazwischen', 'dein', 'deine', 'deinem', 'deiner', 'dem', 'dementsprechend',
    'demgegenüber', 'demgemäss', 'demgemäß', 'demselben', 'demzufolge', 'den', 'denen', 'denn',
    'denselben', 'der', 'deren', 'derjenige', 'derjenigen', 'dermassen', 'dermaßen', 'derselbe',
    'derselben', 'des', 'deshalb', 'desselben', 'dessen', 'deswegen', 'dich', 'die', 'diejenige',
    'diejenigen', 'dies', 'diese', 'dieselbe', 'dieselben', 'diesem', 'diesen', 'dieser', 'dieses',
    'dir', 'doch', 'dort', 'drei', 'drin', 'dritte', 'dritten', 'dritter', 'drittes', 'durch',
    'durchaus', 'dürfen', 'dürft', 'durfte', 'durften', 'eben', 'ebenso', 'ehrlich', 'eigen',
    'eigene', 'eigenen', 'eigener', 'eigenes', 'ein', 'einander', 'eine', 'einem', 'einen', 'einer',
    'eines', 'einige', 'einigen', 'einiger', 'einiges', 'einmal', 'eins', 'elf', 'ende', 'endlich',
    'entweder', 'er', 'Ernst', 'erst', 'erste', 'ersten', 'erster', 'erstes', 'es', 'etwa', 'etwas',
    'euch', 'früher', 'fünf', 'fünfte', 'fünften', 'fünfter', 'fünftes', 'für', 'gab', 'ganz', 'ganze',
    'ganzen', 'ganzer', 'ganzes', 'gar', 'gedurft', 'gegen', 'gegenüber', 'gehabt', 'gehen', 'geht',
    'gekannt', 'gekonnt', 'gemacht', 'gemocht', 'gemusst', 'genug', 'gerade', 'gern', 'gesagt',
    'geschweige', 'gewesen', 'gewollt', 'geworden', 'gibt', 'ging', 'gleich', 'gott', 'gross',
    'groß', 'grosse', 'große', 'grossen', 'großen', 'grosser', 'großer', 'grosses', 'großes', 'gut',
    'gute', 'guter', 'gutes', 'habe', 'haben', 'habt', 'hast', 'hat', 'hatte', 'hätte', 'hatten',
    'hätten', 'heisst', 'her', 'heute', 'hier', 'hin', 'hinter', 'hoch', 'ich', 'ihm', 'ihn',
    'ihnen', 'ihr', 'ihre', 'ihrem', 'ihren', 'ihrer', 'ihres', 'immer', 'in', 'indem', 'infolgedessen',
    'ins', 'irgend', 'ja', 'jahr', 'jahre', 'jahren', 'je', 'jede', 'jedem', 'jeden', 'jeder',
    'jedermann', 'jedermanns', 'jedoch', 'jemand', 'jemandem', 'jemanden', 'jene', 'jenem', 'jenen',
    'jener', 'jenes', 'jetzt', 'kam', 'kann', 'kannst', 'kaum', 'kein', 'keine', 'keinem', 'keinen',
    'keiner', 'kleine', 'kleinen', 'kleiner', 'kleines', 'kommen', 'kommt', 'können', 'könnt',
    'konnte', 'könnte', 'konnten', 'kurz', 'lang', 'lange', 'leicht', 'leide', 'lieber', 'los',
    'machen', 'macht', 'machte', 'mag', 'magst', 'mahn', 'man', 'manche', 'manchem', 'manchen',
    'mancher', 'manches', 'mann', 'mehr', 'mein', 'meine', 'meinem', 'meinen', 'meiner', 'meines',
    'mensch', 'menschen', 'mir', 'mittel', 'mochte', 'möchte', 'mochten', 'mögen', 'möglich',
    'mögt', 'morgen', 'muss', 'müssen', 'musst', 'müsst', 'musste', 'mussten', 'na', 'nach', 'nachdem',
    'nahm', 'natürlich', 'neben', 'nein', 'neue', 'neuen', 'neun', 'neunte', 'neunten', 'neunter',
    'neuntes', 'nicht', 'nichts', 'nie', 'niemand', 'niemandem', 'niemanden', 'noch', 'nun',
    'nur', 'ob', 'oben', 'oder', 'offen', 'oft', 'ohne', 'ordnung', 'recht', 'rechte', 'rechten',
    'rechter', 'rechtes', 'richtig', 'rund', 'sagt', 'sagte', 'sah', 'satt', 'schlecht', 'schluss',
    'schon', 'sechs', 'sechste', 'sechsten', 'sechster', 'sechstes', 'sehr', 'sei', 'seid', 'seien',
    'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'seit', 'seitdem', 'selbst', 'sich',
    'sie', 'sieben', 'siebente', 'siebenten', 'siebenter', 'siebentes', 'sind', 'so', 'solang',
    'solche', 'solchem', 'solchen', 'solcher', 'solches', 'soll', 'sollen', 'sollst', 'sollt',
    'sollte', 'sollten', 'sondern', 'sonst', 'sowie', 'später', 'startseite', 'statt', 'steht',
    'suche', 'tag', 'tage', 'tagen', 'tat', 'teil', 'tel', 'tritt', 'trotzdem', 'tun', 'über',
    'überhaupt', 'übrigens', 'uhr', 'um', 'und', 'uns', 'unse', 'unsem', 'unsen', 'unser', 'unsere',
    'unserem', 'unseren', 'unserer', 'unseres', 'unter', 'usw', 'viel', 'viele', 'vielem', 'vielen',
    'vieler', 'vieles', 'von', 'vor', 'wahr?', 'während', 'währenddem', 'währenddessen', 'wann',
    'war', 'wäre', 'waren', 'wart', 'warum', 'was', 'wegen', 'weil', 'weit', 'weiter', 'weitere',
    'weiteren', 'weiteres', 'welche', 'welchem', 'welchen', 'welcher', 'welches', 'wem', 'wen',
    'wenig', 'wenige', 'weniger', 'weniges', 'wenigstens', 'wenn', 'wer', 'werde', 'werden', 'werdet',
    'weshalb', 'wessen', 'wie', 'wieder', 'will', 'willst', 'wir', 'wird', 'wirklich', 'wirst',
    'wo', 'wohl', 'wollen', 'wollt', 'wollte', 'wollten', 'worden', 'wurde', 'würde', 'wurden',
    'würden', 'z.b', 'zahlreich', 'zeit', 'zu', 'zuerst', 'zugleich', 'zum', 'zunächst', 'zur',
    'zurück', 'zusammen', 'zwanzig', 'zwar', 'zwei', 'zweite', 'zweiten', 'zweiter', 'zweites',
    'zwischen', 'zwölf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
german_stopwords = list(set(german_stopwords))