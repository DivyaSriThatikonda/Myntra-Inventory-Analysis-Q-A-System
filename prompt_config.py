# Configuration for Inventory Analysis Chatbot
# All BRAND_NAMES, CATEGORIES, and INDIVIDUAL_CATEGORIES are lowercase to match database normalization.

BRAND_NAMES = [
    "sojanya", "hubberholme", "louis philippe", "da intimo", "rain & rainbow", "manq", "janasya", "mirchi fashion",
    "triumph", "free authority", "sugathari", "indian women", "rajnandini", "mbeautiful", "pause sport", "jump usa",
    "perfkt-u", "le bourgeois", "purple state", "chhabra 555", "globus", "tabard", "kifahari", "basiics by la intimo",
    "kalyani", "coucou", "monte carlo", "forca", "deyann plus", "m&h easy", "llajja", "rangriti", "jewels gehna",
    "pothys", "span", "gosriki", "sera", "fifa u-17 wc", "mkh", "actoholic", "ad by arvind", "makclan", "head",
    "planetinner", "routeen", "minions by kook n keech", "house of kkarma", "fab dadu", "shangrila", "hritika",
    "vastramay plus", "showoff", "cotton on", "sirikit", "amirah s", "justanned", "broowl", "armaan ethnic", "catchy",
    "christeena", "the roadster lifestyle co", "3pin", "nick&jess", "sanganeri kurti", "zima leto", "zri",
    "donald duck", "hrx by hrithik roshan", "roadster", "shavya", "supersox", "dollar missy", "arise", "the vanca",
    "armisto", "pavechas", "zeyo", "aurelia", "shae by sassafras", "kryptic", "clora creation", "enamor", "red tape",
    "damensch", "chemistry", "inner sense", "panchhi", "ruggers", "rigo", "m7 by metronaut", "indus route by pantaloons",
    "sports52 wear", "ethnic junction", "instafab plus", "ayaany", "ethnovogue", "not yet by us", "even", "khadio",
    "kook n keech toons", "manq casual", "sg leman", "mackly", "tinted", "dixcy scott maximus", "wolfpack", "wishful",
    "9teenagain", "wyfees", "ms.lingies", "masculino latino", "actimaxx", "sakhi jaipur", "silai bunai", "prettybold",
    "evolove", "lindbergh", "solemio", "denimize by fame forever", "rodzen", "soul space", "giordano",
    "enchanted drapes", "maishi", "sudarshan silks", "truebrowns", "zaveri pearls", "toothless",
    "kalenji by decathlon", "aujjessa", "cierge", "sanskruptihomes", "marc loire", "perfly by decathlon",
    "simond by decathlon", "blissclub", "style shoes", "modeve", "tiara", "koton", "ben sherman", "thangamagan",
    "big fox", "louis stitch", "platinum studio", "shinoy", "adwitiya collection", "sparrowhawk", "next look",
    "runwayin", "swiss club", "lacylook", "perfect wear", "vishudh", "mitera", "smarty pants", "indo era", "ira soleil",
    "ksut", "purvaja", "lady love", "one8", "calvin klein underwear", "spykar", "klamotten", "soie", "being human",
    "ives", "clorals", "treemoda", "joven", "laado - pamper yourself", "asics", "sanwara", "blissta", "centra",
    "ed hardy", "van heusen denim labs", "dennis lingo", "fuaark", "imt", "allen solly tribe", "urbanic", "cation",
    "melon", "gracit", "hangup trend", "chennis", "mf", "defacto", "reveira", "reebok classic", "mango man",
    "richlook", "basics", "chill winston", "fabglobal", "venisa", "kami kubi", "aesthetic bodies", "waahiba", "obow",
    "woods", "varkha fashion", "anekaant", "copperline", "evoq", "kurti's by menka", "siah", "ratan creation",
    "pyjama party", "cotclo", "h&m", "piroh", "zotw", "lux cozi for her", "sztori marvel", "aarke ritu kumar",
    "v&m", "kica", "campus", "peora", "fabnest curve", "sztori garfield", "johnny bravo by kook n keech",
    "beverly hills polo club", "deewa", "nayo", "hangup", "the indian garage co", "ziyaa", "momtobe", "sringam",
    "solognac by decathlon", "the bear house", "khushal k", "leading lady", "i like me", "zebu", "espresso", "imara",
    "peter england", "wrangler", "ajile by pantaloons", "nite flite", "rudra bazaar", "indian virasat",
    "yogue activewear", "hypernation", "cobb", "hrx", "fasense", "mango", "pashmoda", "nehamta", "cantabil", "spirit",
    "hangup plus", "triban by decathlon", "ruhaans", "fame forever by lifestyle", "gallus", "kraft india", "voi jeans",
    "monochrome", "desinoor.com", "klotthe", "idalia", "anmi", "momin libas", "akkriti by pantaloons",
    "pride apparel", "cl sport", "black panther", "kisah plus", "griffel", "ivoc plus", "glam roots", "saaki",
    "senyora", "azira", "pannkh", "marc louis", "somras", "foreign culture by fort collins", "friends by dressberry",
    "513", "strop", "smileyworld", "jean cafe", "dais", "berrylush", "pepe", "kipsta by decathlon", "kalakari india",
    "vedana", "meemee", "wtfunk", "shrestha by vastramay", "mode by red tape", "luxure by louis philippe",
    "royal enfield", "iris", "van heusen flex", "karatcart", "everdion", "fusion threads", "jdc",
    "fouganza by decathlon", "vero amore", "only", "levis", "highlander", "jaipur kurti", "huetrap", "ishin",
    "anaisa", "maaesa", "shaftesbury london", "marks & spencer", "rosaline by zivame", "artengo by decathlon",
    "dreamz by pantaloons", "plutus", "austin wood", "florence", "fabnest", "raymond", "urban ranger by pantaloons",
    "revolution", "panit", "cinocci", "voxati", "invictus indoor", "fabseasons", "john pride", "v dot", "the nks plus",
    "be indi", "the kaftan company", "parfait", "swiss military", "tag 7 plus", "alena", "pinwheel",
    "peter england university", "code by lifestyle", "ethnicity", "hps sports", "bucik", "imyoung", "saadhvi", "suta",
    "satyam weaves", "i know", "bishop cotton", "anug by sojanya", "creature", "ashnaina", "tossido", "white fire",
    "winered", "aesthetic nation", "camey", "bruun & stengade", "aadvika", "kalamandir", "dream of glory inc",
    "besiva", "silvermerc designs", "watko by decathlon", "columbia", "1 stop fashion", "aayusika",
    "dexter by kook n keech", "bellofox", "svanik", "youthnic", "jisora", "btwin by decathlon", "magnetic designs",
    "luxurazi", "aasi", "lill", "millennial men", "manq plus", "anwaind", "villain", "ritu kumar", "rare", "only & sons",
    "uri and mackenzie", "mumbai indians", "masch sports", "floret", "w", "bewakoof", "street 9", "ahalyaa",
    "see designs", "os", "urbano fashion", "dollar bigboss", "n-gal", "slazenger", "mimosa", "rajesh silk mills",
    "lux cozi", "n2s next2skin", "park avenue", "kotty", "underjeans by spykar", "yak yak", "aeropostale",
    "zelocity by zivame", "adorenite", "blinkin", "rare rabbit", "swagg india", "grancy", "french connection",
    "forever 21", "neudis", "kook n keech looney tunes", "gant", "souchii", "french flexious", "invincible", "sugr",
    "maxence", "armure", "abof", "solly jeans co.", "madsto", "rustorange", "allen solly woman", "vega",
    "vandnam fabrics", "obaan", "sayesha", "hk colours of fashion", "women touch", "red chief", "castle", "sanisa",
    "athleto", "v sales", "forca by lifestyle", "eavan", "status quo", "jinfo", "raisin", "skechers", "femea",
    "franco leone", "oxemberg", "blitzsox", "apratim", "mode de base", "code 61", "mokshi", "black coffee", "bullmer",
    "varanga", "invictus", "kanvin", "bushirt", "prettycat", "friskers", "fashionrack", "dollar", "nyamba by decathlon",
    "portblair", "c9 airwear", "dynamocks", "chkokko", "blackberrys", "fido dido", "quechua by decathlon", "laabha",
    "vbuyz", "akimia", "shopgarb", "divena", "c9", "wear your mind", "mystere paris", "byford by pantaloons", "bitz",
    "tommy hilfiger", "studio rasa", "prettyplus by desinoor.com", "sweet dreams", "mpl sports", "curvy love",
    "souminie", "arrow new york", "adobe", "anoma", "bodycare insider", "av2", "trundz", "gespo", "louis philippe athplay",
    "beebelle", "mint & oak", "sangam prints", "netram", "pneha", "charukriti", "vaaba", "harbornbay", "crocodile",
    "rodamo", "van heusen woman", "kaajh", "vairagee", "not just pyjamas", "faballey curve", "curvezi by ziyaa",
    "lotto", "lamaaya", "genx", "greenfibre", "street armor by pantaloons", "nexus", "texco", "unisets", "modi kurta",
    "havida sarees", "dyca", "sztori dc", "lovely lady", "prenea", "araaliya", "yaadleen", "saraf rs jewellery",
    "west vogue by zivame", "aryavart", "aawari", "with", "anouk", "etc", "domyos by decathlon", "ahika", "sassafras",
    "yufta", "elevanto", "difference of opinion", "breakbounce", "de moza", "flying machine", "arrow", "neu look fashion",
    "louis philippe jeans", "aamna", "mamma presto", "coucou by zivame", "indietoga", "arrow sport", "navysport",
    "cukoo", "innocence", "dixcy scott", "cape canary", "7threads", "secrets by zerokaata", "sapper", "club york",
    "enviously young", "neva", "freecultr", "jockey", "veirdo", "mufti", "colorplus", "richard parker by pantaloons",
    "heelium", "mezmoda", "decorealm", "komli", "sojanya plus", "purple feather", "fabindia", "sasimo",
    "kook n keech emoji", "the mom store", "dixcy scott slimz", "groverson paris beauty", "ethnix by raymond",
    "paroksh", "tulsattva", "bratma", "nakkashi", "awesome", "kultprit", "saree swarg", "aarrah", "charak", "raas",
    "vividartsy", "sparx", "luxrio", "minions by dressberry", "every de by amante", "tom & jerry by sztori",
    "anti culture", "selvamagan", "online fayda", "ramas", "shangrila creation", "ants", "octave", "poonam designer",
    "mine4nine", "chipbeys", "tng", "threadcurry", "tribord by decathlon", "amosio", "bene kleed", "pepe jeans",
    "yuris", "pluss", "justice league", "slumber jill", "house of pataudi", "biba", "one8 x puma", "mameraa", "fashor",
    "single", "appulse", "shaily", "benstoke", "kalt", "vrsales", "erotissch", "freehand", "mag", "shubhkala",
    "krossstitch", "duke", "redround", "beat london by pepe jeans", "maanja", "bharatsthali", "ethnic basket",
    "om shantam sarees", "madame m secret", "juniper plus", "parx", "wildcraft", "tattva", "rangoli", "vebnor",
    "beau design", "xoxo design", "and", "i jewels", "get glamr", "woowzerz", "rajubhai hargovindas", "dollar socks",
    "lino perros", "new balance", "jade blue", "bambos", "desi weavess", "pinkloom", "pashtush", "flaher", "abhishti",
    "myaza", "safaa", "yovish", "firstkrush", "zizo by namrata bajaj", "fever", "ladusaa", "deebaco", "austivo",
    "kenneth cole", "alan jones", "malhaar", "indi inside", "here&now", "maniac", "kook n keech marvel", "clovia",
    "vimal jonney", "saree mall", "door74", "myshka", "westclo", "bossini", "global desi", "palakh", "colt",
    "ode by house of pataudi", "meeranshi", "adidas originals", "miss chase", "softskin", "calvin klein jeans",
    "rangmanch by pantaloons", "crimsoune club", "seven rocks", "cosmo lady", "ucla", "hummel", "peter england elite",
    "thomas scott", "melange by lifestyle", "jaipur attire", "yavi", "athena", "koi sleepwear", "maashie", "vento",
    "genius18", "louis philippe ath.work", "proteens", "laa calcutta", "style quotient", "kook n keech batman",
    "pierre carlo", "rock.it", "neerus", "iki chic", "balista", "sethukrishna", "stylestone", "rubans", "just wow",
    "zigo", "v2 value & variety", "swishchick", "harsam", "merlot", "vinenzia", "burnt umber", "kimayra", "susie",
    "20dresses", "mylo essentials", "rosaline", "vaividhyam", "suitltd", "pivot", "nimayaa", "mesmore",
    "house of jammies", "pirko", "pache", "rasm", "u.s. polo assn. women", "terquois", "109f", "dealseven fashion",
    "poshak hub", "zivame", "wrogn active", "masha", "cottinfab", "sztori", "nation polo club", "kisah", "ivoc",
    "force nxt", "juniper", "nautica", "mbe", "kappa", "napra", "candyskin", "louis philippe sport", "balenzia",
    "pretty awesome", "mr bowerbird", "vemante", "goldstroms", "quarantine", "peter england casuals", "leather retail",
    "rangmayee", "galypso", "m&h our water", "u&f", "aarika", "griiham", "serona fabrics", "9shines label", "manu",
    "dc comics", "mutaqinoti", "spaces", "woodland", "melangebox", "rang gali", "thara sarees", "siril",
    "modern indian by chemistry", "yoloclan", "ennoble", "shiloh", "silver stock", "unnati silks", "v tradition",
    "gvs shoppe", "skidlers", "juneberry", "triveni", "kook n keech superman", "kook n keech harry potter", "foga",
    "sg", "skyria", "get wrapped", "karmic vision", "inesis by decathlon", "tantkatha", "98 degree north", "trendyol",
    "united liberty", "nejo", "sangria", "campus sutra", "dollar ultra", "varkala silk sarees", "alcis", "hancock",
    "yash gallery", "kook n keech", "drape in vogue", "shewill", "max", "quttos", "ketch", "romeo rossi", "mod & shy",
    "popnetic", "high star", "van heusen", "molly & michel", "weavers villa", "fugazee", "sand dune", "soundarya",
    "mabish by sonal jain", "brachy", "metronaut", "van heusen sport", "bitterlime", "ginni arora label",
    "fcuk underwear", "celio", "dillinger", "vero moda", "zola", "jatriqq", "fabric fitoor", "lenissa", "clt.s",
    "ginger by lifestyle", "shyaway", "cayman", "creeva", "american crew plus", "zoeyams", "sf jeans by pantaloons",
    "the dry state", "star wars by wear your mind", "stylee lifestyle", "saadgi", "fusion beats", "blacksmith",
    "bewakoof plus", "arhi", "loom legacy", "uptownie lite", "u.s. polo assn. tailored", "sutram", "american-elm",
    "simon carter london", "impackt", "anvi be yourself", "imperative", "furryflair", "ayaki", "blush 9 maternity",
    "fitup life", "marvel avengers", "minora", "silvertraq", "bummer", "disney by dressberry", "anahi", "sharaa ethnica",
    "braveo", "tusok", "berry blues", "pockman", "soxytoes", "american eye", "slickfix", "bruchi club", "kvsfab",
    "moda rapido", "u.s. polo assn. denim co.", "bhama couture", "stylum", "inddus", "nike", "urban scottish",
    "fashion depth", "urbano plus", "kalini", "cultsport", "kipek", "urban dog", "jack & jones",
    "united colors of benetton", "qurvii", "tokyo talkies", "secret wish", "reebok", "lee", "oxolloxo", "fabriko",
    "divastri", "wintage", "indya", "prakhya", "olaian by decathlon", "fcuk", "gritstones", "favoroski", "divyank",
    "xin", "steenbok", "gulmohar jaipur", "attiitude", "nakshi", "badoliya & sons", "saffron threads", "nba", "bukkum",
    "cavallo by linen club", "tissu", "rooted", "unsully", "vartah", "matinique", "shirt theory", "kiana", "sqew",
    "fashiol", "curare", "seerat", "rex straut jeans", "wedze by decathlon", "ix impression", "berrys intimatess",
    "rute", "fitz", "suti", "globon impex", "sztori superman", "glorious", "vasudha", "scoldme", "tasarika", "what's down",
    "picot", "navyasa", "madame", "wear equal", "j hampstead", "power", "avi living", "bani women", "altiven",
    "sitaram designer", "fitleasure", "surhi", "english navy", "harvard", "libas", "puma motorsport", "trident",
    "cross court", "amante", "tom burg", "jompers", "extra love by libas", "lady lyka", "adidas", "karigari", "flambeur",
    "tag 7", "classic polo", "paris hamilton", "american crew", "rajgranth", "off limits", "ducati", "laceandme",
    "beevee", "the souled store", "nabaiji by decathlon", "okane", "kopnhagn", "akshatani", "om sai latest creation",
    "selected", "looknbook art", "wacoal", "t-base", "raa jeans", "v-mart", "marc", "urgear", "the million club",
    "mascln sassafras", "southbay", "rangmanch plus by pantaloons", "soch", "luni", "lagashi", "saanjh", "geroo jaipur",
    "lakshita", "sg rajasahab", "rg designers", "9rasa", "agroha", "yoonoy", "bonjour", "kosha", "athlisis",
    "disney by wear your mind", "faserz", "roadster fast and furious", "saubhagya", "heemara", "qomn", "agil athletica",
    "agil armero", "do dhaage", "parcel yard", "manohari", "kastner", "bavaria", "aventura outfitters", "beatitude",
    "american archer", "flx by decathlon", "house of kari", "dennis morton", "mayra", "roly poly", "freakins", "swasti",
    "texlon", "devoiler", "subea by decathlon", "finnoy", "jaipuri bunaai", "flavido", "blanc9", "jerfsports",
    "scorpius", "charu", "rue collection", "colour me by melange", "mast & harbour", "locomotive", "xyxx",
    "one8 by virat kohli", "puma", "bigbanana", "vastramay", "anubhutee", "abelino", "yuuki", "ether", "jainish",
    "prakrti", "dennison", "namaskar", "bannos swagger", "proline active", "readiprint fashions", "conditions apply",
    "kalista", "all about you", "tankhi", "people", "studio shringaar", "taavi", "amrutam fab", "ojjasvi", "fbella",
    "lebami", "ardeur", "american eagle outfitters", "kook n keech disney", "highlight fashion export",
    "miaz lifestyle", "tweens", "fitkin", "cherokee", "excalibur", "almo wear", "chitwan mohan",
    "marvel by wear your mind", "tulip 21", "the weave traveller", "pistaa", "eccentric", "silk land", "antony morato",
    "showoff plus", "xl love by janasya", "satrani", "awadhi", "ziva fashion", "883 police", "tuna london", "feranoid",
    "jansons", "dodo & moa", "rivi", "antaran", "amydus", "muscle torque", "missguided", "ardozaa", "selvia", "austiex",
    "kajaru", "diva walk exclusive", "man matters", "poker active", "rajnie", "lounge dreams", "atsevam",
    "ikk kudi by seerat", "raano", "priyaasi", "brinns", "hush puppies", "zelocity", "madhuram", "imfashini", "pisara",
    "nirkhi", "linen club", "fawoment", "ethnic street", "inocencia", "la bele", "singni", "vimal", "dressberry",
    "anayna", "claura", "tikhi imli", "aayna", "softrose", "wild west", "phwoar", "vastranand", "kiprun by decathlon",
    "gerua", "forclaz by decathlon", "deyann", "fort collins", "allen solly", "aprique fab", "silk bazar",
    "the pink moon", "boston club", "indian terrain", "indibelle", "allen solly sport", "nanda silk mills", "inweave",
    "vastraa fusion", "faballey", "tarmak by decathlon", "kuons avenue", "fresh feet", "rare roots", "aasiya",
    "canary london", "mash unlimited", "kolor fusion", "bareblow", "puma hoops", "plagg", "be awara", "american bull",
    "shubhvastra", "bralux", "alvaro castagnino", "la intimo", "smugglerz", "accessher", "indyes", "molcha", "naari",
    "fashion fricks", "east ink", "bene kleed plus", "venitian", "teakwood leathers", "paramount chikan",
    "indethnic", "indiankala4u", "kook n keech star wars", "aasi - house of nayo", "colors", "katso",
    "calvin klein innerwear", "the mini needle", "don vino", "etiquette", "wodreams", "adbucks", "resha",
    "khoday williams", "fila", "bronz", "ortange", "sztori batman", "indian wootz", "mark leute", "broadstar",
    "dc by kook n keech", "sangria", "campus sutra", "zivame"
]

CATEGORIES = [
    "indian wear", "topwear", "bottom wear", "sports wear", "lingerie & sleep wear", "inner wear & sleep wear",
    "western", "plus size"
]

INDIVIDUAL_CATEGORIES = [
    "lounge-pants", "lounge-shorts", "tunics", "nehru-jackets", "patiala-and-dupatta", "scarves", "kurtis",
    "lehenga-choli", "clothing-set", "harem-pants", "salwar-and-dupatta", "stoles", "tops", "dress-material",
    "co-ords", "churidar", "shrug", "sleepsuit", "trousers", "tracksuits", "night-suits", "capris",
    "necklace-and-chains", "tshirts", "kurta-sets", "dresses", "sarees", "stockings", "sherwani", "dhotis",
    "jeggings", "dungarees", "outdoor-masks", "waistcoat", "trunk", "robe", "jumpsuit", "swimwear", "jeans",
    "bra", "dupatta", "sweaters", "palazzos", "baby-dolls", "bath-robe", "thermal-tops", "blazers", "kurtas",
    "boxers", "pyjamas", "sports-sandals", "salwar", "thermal-set", "lounge-tshirts", "casual-shoes", "heels",
    "shorts", "innerwear-vests", "lingerie-set", "flats", "saree-blouse", "thermal-bottoms", "patiala",
    "swim-bottoms", "shawl", "burqas", "socks", "jackets", "skirts", "leggings", "saree-accessories",
    "earrings", "suits", "boots", "tights", "shapewear", "nightdress", "lingerie-accessories", "camisoles",
    "track-pants", "shirts", "briefs", "sweatshirts", "coats", "rain-jacket"
]

SAMPLE_QUESTIONS = {
    "what is the stock of jeans from sangria": "SELECT SUM(Current_Stock) FROM sales_and_stock_info WHERE BrandName = 'sangria' AND Individual_category = 'jeans'",
    "how many kurtas were sold by roadster": "SELECT SUM(Quantity_Sold) FROM sales_and_stock_info WHERE BrandName = 'roadster' AND Individual_category = 'kurtas' AND Quantity_Sold > 0",
    "show me tshirts from campus sutra with low stock": "SELECT TOP 10 BrandName, Individual_category, size, Current_Stock, Reorder_Level, DiscountPriceInRs FROM sales_and_stock_info WHERE BrandName = 'campus sutra' AND Individual_category = 'tshirts' AND Current_Stock <= Reorder_Level",
    "what is the total revenue for indian wear": "SELECT SUM(RevenueInRs) FROM sales_and_stock_info WHERE Category = 'indian wear'",
    "list the top-rated dresses": "SELECT TOP 1 WITH TIES BrandName, Individual_category, Ratings, Reviews FROM MyntraFashionClothing WHERE Individual_category = 'dresses' ORDER BY CAST(Ratings AS FLOAT) DESC",
    "how many shirts were sold in xl size": "SELECT SUM(Quantity_Sold) FROM sales_and_stock_info WHERE Individual_category = 'shirts' AND size = 'xl' AND Quantity_Sold > 0",
    "what is the stock of kurtas for women": "SELECT SUM(Current_Stock) FROM sales_and_stock_info WHERE Individual_category = 'kurtas' AND category_by_Gender = 'women'",
    "show me jackets under 2000 rupees": "SELECT BrandName, Individual_category, Description, DiscountPriceInRs, Current_Stock FROM sales_and_stock_info WHERE Individual_category = 'jackets' AND DiscountPriceInRs < 2000",
    "what is the average rating for tops": "SELECT AVG(CAST(Ratings AS FLOAT)) AS Avg_Rating FROM MyntraFashionClothing WHERE Individual_category = 'tops'",
    "how many jeans were sold in size m in the next 30 days": "SELECT SUM(Quantity_Sold) FROM sales_and_stock_info WHERE Individual_category = 'jeans' AND size = 'm' AND Quantity_Sold > 0 AND Predicted_Stockout_Date <= DATEADD(day, 30, GETDATE())",
    "what is the predicted restock date for low stock shirts": "SELECT BrandName, Individual_category, size, Predicted_Restock_Date, Predicted_Restock_Quantity FROM sales_and_stock_info WHERE Individual_category = 'shirts' AND Current_Stock <= Reorder_Level",
    "cheapest tshirts for men": "SELECT TOP 5 BrandName, Description, DiscountPriceInRs, Current_Stock FROM sales_and_stock_info WHERE Individual_category = 'tshirts' AND category_by_Gender = 'men' ORDER BY DiscountPriceInRs ASC",
    "highest rated jeans with more than 100 reviews": "SELECT TOP 5 BrandName, Individual_category, Ratings, Reviews FROM MyntraFashionClothing WHERE Individual_category = 'jeans' AND Reviews > 100 ORDER BY CAST(Ratings AS FLOAT) DESC",
    "restock priority for high turnover items": "SELECT BrandName, Individual_category, size, Current_Stock, Reorder_Level, Predicted_Restock_Quantity, Predicted_Restock_Date FROM sales_and_stock_info WHERE Turnover_Flag = 'High' AND Current_Stock <= Reorder_Level ORDER BY Current_Stock/Reorder_Level ASC"
}

PROMPT_TEMPLATE = """
You are an expert SQL query generator for a retail inventory database with two tables: 'sales_and_stock_info' and 'MyntraFashionClothing'. Given a natural language query, generate a precise SQL query for Microsoft SQL Server.

**Table: sales_and_stock_info**
Columns: Product_id (int), BrandName (varchar), Category (varchar), Individual_category (varchar), category_by_Gender (varchar), Description (varchar), DiscountPriceInRs (decimal), Current_Stock (int), Reorder_Level (int), Quantity_Sold (int), RevenueInRs (decimal), Turnover_Flag (varchar), Predicted_Restock_Quantity (int), Predicted_Stockout_Date (datetime), Predicted_Restock_Date (datetime), size (varchar)
Sample brands: {brand_samples}
Sample categories: {category_samples}
Sample individual categories: {individual_category_samples}

**Table: MyntraFashionClothing**
Columns: URL (varchar), Product_id (int), BrandName (varchar), Category (varchar), Individual_category (varchar), category_by_Gender (varchar), Description (varchar), DiscountPriceInRs (decimal), OriginalPriceInRs (decimal), DiscountOffer (varchar), Ratings (varchar), Reviews (int), standardSize (varchar), DiscountPercent (decimal)
Sample brands: {brand_samples}
Sample categories: {category_samples}
Sample individual categories: {individual_category_samples}

**Instructions:**
- For stock, sales, revenue, or restock predictions, use 'sales_and_stock_info'.
- For ratings, reviews, or discounts, use 'MyntraFashionClothing'.
- Join tables on Product_id if both are needed.
- Use exact terms from the query for BrandName, Individual_category, category_by_Gender, and size (e.g., 'track-pants', 'jaipur kurti').
- There are {brand_count} unique BrandNames, {category_count} unique Categories, and {individual_category_count} unique Individual_categories.
- For 'how many' or 'sold' queries, use SUM(Quantity_Sold) with Quantity_Sold > 0.
- For revenue, use SUM(RevenueInRs).
- For price queries, use DiscountPriceInRs.
- For ratings, use MyntraFashionClothing.Ratings (varchar, e.g., '4.2'); cast to FLOAT for sorting (e.g., CAST(Ratings AS FLOAT)).
- For time-based queries, use Predicted_Stockout_Date or Predicted_Restock_Date (e.g., WHERE Predicted_Stockout_Date <= DATEADD(day, 30, GETDATE())).
- For restock predictions, use Predicted_Restock_Quantity and Turnover_Flag (e.g., 'High', 'Normal', 'Low').
- For gender, use category_by_Gender (e.g., 'men', 'women').
- For size, use size (e.g., 'xl', 'm').
- For description-based queries (e.g., 'blue jeans'), use Description LIKE '%blue%'.
- Sample questions and SQL:
  {sample_questions}

Generate the SQL query for: {query}
Return only the SQL query, without 'sql' prefix or Markdown formatting.
"""