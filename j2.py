import json
from collections import defaultdict, Counter
from datetime import datetime

# Load JSON with UTF-8 encoding
with open("flowers_processed.json", "r", encoding="utf-8") as f:
    floraldata = json.load(f)

# 1️⃣ Count occurrences of each species
unique_species = set(f["species"] for f in floraldata if "species" in f)
print("Unique species:", len(unique_species))
for sp in unique_species:
    print(sp)

print("-"*20)   

# # 2️⃣ Group data by month
# data_by_month = defaultdict(list)
# for f in floraldata:
#     if "date" in f:
#         month = datetime.strptime(f["date"], "%Y-%m-%d").strftime("%Y-%m")
#         data_by_month[month].append(f)

# # Save separate JSON files for each month
# for month, entries in data_by_month.items():
#     filename = f"flowers_{month}.json"
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(entries, f, indent=2)
#     print(f"Saved {len(entries)} entries to {filename}")



# bract milkweed: 1
# mule fat: 1
# Spike Beard-heath: 1
# Leafless Ghostplant: 1
# Dillwynia elegans: 1
# Caladenia graniticola: 1
# Añañuca de fuego: 1
# pink sun-orchid: 2
# seaside pea: 1
# Diuris maculata: 1
# big bluestem: 2
# Tillandsia turneri: 1
# Star Xanthosia: 1
# Black Medick: 1
# Alsike clover: 1
# mist flower: 2
# western harebell: 1
# Cyanothamnus anemonifolius anemonifolius: 1
# woolly tidestromia: 1
# dotted gayfeather: 1
# Prostanthera decussata: 1
# hairy buttercup: 1
# Narrowleaf False Boneset: 1
# Hibbertia empetrifolia: 1
# Bunch-flowered Daffodil: 1
# small matweed: 1
# silky evolvulus: 1
# Pakihi Rush: 1
# Abert's sanvitalia: 1
# Cherry-plum: 1
# bedstraw St. John's Wort: 1
# Common Hop Bush: 1
# Wright's silktassel: 1
# Beardlip Penstemon: 1
# Pimelea axiflora: 1
# Goodia lotifolia: 1
# wright's hymenothrix: 1
# chagualillos: 2
# 霧社木薑子: 1
# Hairy Mountain Mahogany: 1
# rough menodora: 1
# macoun's everlasting: 1
# royal sandmat: 1
# Mostacilla: 1
# pinewoods geranium: 2
# Monticalia vaccinioides: 1
# Rocky Mountain zinnia: 1
# Small-leaved kowhai: 1
# Lilly Pilly: 1
# Slender Thistle: 1
# Cardinal Flower: 1
# Dracophyllum secundum: 1
# Vriesea ruschii: 1
# Clinopodium nepeta spruneri: 1
# Spanish clover: 1
# pine-barren sandwort: 1
# Selkirkia limense: 1
# Lys de mer: 1
# Texas Bull Nettle: 1
# achupalla: 2
# Fendler's ceanothus: 1
# slimleaf plains-mustard: 2
# owlsclaws: 1
# דם-המכבים האדום: 1
# פשתה שעירה: 1
# naked bishop's cap: 1
# White Mullein: 1
# Jacobaea adonidifolia: 1
# צהרון מצוי: 1
# Taxandria spathulata: 1
# Southern Mountains Paintbrush: 1
# Armeria pubinervis: 1
# Aromatic Aster: 1
# עירית גדולה: 1
# panicled willowherb: 3
# Hypericum richeri burseri: 1
# Phyteuma orbiculare: 1
# Bowman's root: 1
# Picris hieracioides: 2
# Ruellia ciliatiflora: 1
# Campanula glomerata: 1
# Potentilla nivalis: 1
# suur lõvilõug: 1
# Mignonette vine: 1
# Erigeron uniflorus: 1
# Echinocereus coccineus roemeri: 1
# American snoutbean: 1
# Bearded Beggarticks: 1
# Gardenia ovularis: 1
# Ortiguilla: 1
# Physalis solanacea: 1
# Smooth Beggarticks: 1
# Hardy Fuchsia: 1
# Bush Vetch: 2
# Great burnet: 1
# Marsh Lousewort: 1
# Montbretia: 1
# Cherry laurel: 2
# ice plant: 1
# tulip tree: 1
# Marcavala-preta: 1
# Chagas: 1
# uvas de gato: 1
# Pasakana: 1
# Wingpetal: 1
# Allium ericetorum: 3
# Quisco: 1
# Silene saxifraga: 1
# tojo-arnal-do-litoral: 1
# Linajola comune: 1
# Cirsium subuliforme: 1
# longleaf cologania: 1
# Sweet Shaggytuft: 1
# Wright's Deervetch: 2
# Clavelinas deshilachadas: 1
# Salz-Hornklee: 1
# Roter Zahntrost: 1
# Silene latifolia: 1
# Verbascum sinuatum: 1
# Wilde Sumpfkresse: 1
# Thalictrum macrocarpum: 1
# Texas mountain laurel: 1
# Bunte Kronwicke: 1
# Sweet acacia: 1
# Slender Woolly Buckwheat: 1
# Yellow-wort: 1
# Small Toadflax: 1
# Coastal groundcherry: 1
# marsh cudweed: 1
# water smartweed: 2
# common silverweed: 1
# Tillandsia eizii: 1
# Hauya elegans: 1
# Digitale jaune: 1
# gatassa: 1
# Βάτος ο ιερός: 1
# Λάδανο: 1
# Vicia pannonica: 1
# Ophrys scolopax: 1
# American beautyberry: 1
# Eriosyce castanea: 1
# Kudzu Bean: 2
# Mauve en arbre: 1
# Chardon laiteux: 1
# Lavande à toupet: 1
# Ciste de Montpellier: 1
# Liseron fausse-guimauve: 1
# Camélée à trois coques: 1
# romarin commun: 1
# Fumeterre grimpante: 1
# euphorbe des garrigues: 1
# Linaire couchée: 1
# Coronille des jardins: 1
# alliaire officinale: 2
# Maceron: 1
# western heermann's buckwheat: 2
# western lessingia: 1
# Tillandsia recurvata: 1
# Watermelon: 1
# Adonis flammea: 1
# Roemeria argemone: 1
# Spiny Starwort: 1
# blue hound's-tongue: 1
# Southern Crupina: 1
# Douglas' threadleaf ragwort: 1
# Horn-Sauerklee: 1
# Pale Toadflax: 3
# Oval Ladies' Tresses: 3
# black garlic: 1
# laiteron rude et laiteron glauque: 1
# Géranium des Pyrénées: 2
# Cirse des champs: 2
# Italian Bugloss: 1
# Pale agoseris: 1
# Miersia tenuiseta: 1
# Gänseblümchen: 1
# Nettle-leaved Bellflower: 3
# Kriechendes Fingerkraut: 1
# Early Dog-violet: 1
# Campanule gantelée: 3
# Aristoloche clématite: 1
# Pszeniec zwyczajny: 2
# Woolly Sorrel: 3
# Gentiana puberulenta: 1
# Große Kuhschelle: 2
# showy tick-trefoil: 1
# wild cucumber: 1
# pointed-leaved tick-trefoil: 1
# Mastranzo: 1
# Croton suberosus: 2
# Miersia chilensis: 1
# Ufer-Wolfstrapp: 1
# Wasserminze: 1
# gnome plant: 1
# Striga elegans: 1
# whorled loosestrife: 1
# Least Snoutbean: 1
# Gewöhnliche Telekie: 2
# Matapoll: 2
# Sauge glutineuse: 1
# snakeroots: 1
# Aloe: 1
# Ophrys insectifera: 1
# campanilla palmeada: 2
# Zizotes Milkweed: 1
# Solanum pinnatum: 1
# Hoary Ragwort: 1
# tuestenbræk: 1
# Anaphalis margaritacea: 1
# flame tree: 1
# Tue-limurt: 1
# prakttidlösa: 1
# Redcenter Morning-glory: 2
# Schmalblättriges Weidenröschen: 2
# peònia de muntanya: 1
# erva-pulgueira-das-berlengas: 1
# bruguera: 2
# Calendula suffruticosa algarbiensis: 1
# viboreira-da-berlenga: 1
# Scrophularia sublyrata: 2
# Dittrichia viscosa revoluta: 1
# Kleine Malve: 3
# Tropaeolum austropurpureum: 1
# Great Valley gumweed: 1
# 荞麦叶大百合: 1
# Lespedeza pilosa: 1
# Virginia mountain mint: 1
# manyflower tobacco: 1
# Trifolium repens: 1
# ślaz zaniedbany: 2
# Trapoeraba: 1
# common gardenia: 1
# Rubus idaeus: 1
# Impatiens capensis: 1
# Baccharis patens: 1
# Baccharis jocheniana: 1
# Senecio heterotrichius: 1
# Asparagus asparagoides: 1
# Impatiens glandulifera: 1
# side-flowering skullcap: 2
# Bistorta officinalis: 1
# Chicory: 1
# Safrà blanc: 1
# Prímula integrifòlia: 1
# Olivarda: 1
# Zottiges Weidenröschen: 1
# Netted Globecherry: 1
# Kuckucksblume: 1
# Small Palafox: 1
# Marsh Jaumea: 1
# Gewöhnliches Bitterkraut: 1
# Longhead Sceptre: 1
# bigpod sesbania: 2
# fenouil: 1
# Tanaisie commune: 1
# 臺灣莓: 1
# Viola adenothrix: 1
# Trança-de-Outono: 1
# Aralia bipinnata: 1
# 間型沿階草: 1
# lliri de mar: 1
# Österreichischer Kranzenzian: 1
# Bellardie visqueuse: 1
# Liseron des haies: 1
# purpurbräcka: 1
# malva enana: 1
# Hypericum triquetrifolium: 1
# Campaneta blava: 1
# Τριβόλι: 2
# Szczawik żółty: 1
# Közönséges vasfű: 1
# Aechmea gamosepala: 1
# Orenga: 1
# Common Swordlily: 1
# Gaillet jaune: 1
# Vara d'or: 1
# Hyssopus officinalis: 2
# shaggy portulaca: 1
# Vielstängeliges Fingerkraut: 1
# Cyanella lutea lutea: 1
# Renoster Watsonia: 2
# Cichorium intybus: 1
# Blushing Bride: 1
# Voyria aurantiaca: 1
# Clutia pulchella: 1
# Sérapias à labelle allongé: 1
# matrimony vine: 1
# orange coneflower: 3
# Porter's sunflower: 1
# New Zealand Willowherb: 1
# Pancratium foetidum saldense: 1
# Kluwenklokje: 1
# Véronique de Perse: 1
# Galinsoge cilié: 1
# Quelite: 1
# křížatka obecná: 1
# Brushland Lantana: 1
# marsh cinquefoil: 1
# Sea Pumpkin: 2
# Kæmpe-balsamin: 1
# Scarlet Calamint: 1
# Orange Satyre: 1
# Algarrobo negro: 1
# purple false foxglove: 3
# compass plant: 2
# Copper Brightfig: 1
# Silène acaule: 1
# Achillée des Pyrénées: 1
# Trèfle alpin: 1
# Épiaire officinale: 1
# rohtopurasruoho: 1
# Mirabilis glabrifolia: 1
# Дрёма широколистная: 1
# Подмаренник мягкий: 1
# Чистец однолетний: 1
# Капуста полевая: 1
# common hedge parsley: 1
# swamp milkweed: 1
# beach suncup: 1
# genziana sfrangiata: 1
# Zigzag Spiderwort: 1
# Thesium hispidulum: 1
# Huevos de víbora: 2
# English bedstraw: 1
# Bergwiesen-Frauenmantel: 1
# Яснотка пурпурная: 2
# Asterolasia pallida: 1
# Sheathing Spiderlily: 1
# European lily of the valley: 1
# Gentianopsis ciliata: 2
# Meadow Saffron: 1
# Asclepias fascicularis: 1
# Alpelimurt: 1
# høstlyng: 1
# Bidens odorata: 1
# Ash Gumbush: 1
# Sand Stock: 1
# Strapwort: 1
# Campana-da-praia: 1
# Sea Aster: 1
# cornichão-das-areias: 1
# Fluweelblad: 1
# Genciana ciliada: 1
# Isranunkel: 1
# Racinaea tetrantha: 1
# Конюшина польова: 1
# Phacelia sanzinii: 1
# Adesmia grandiflora: 1
# scallop hakea: 1
# Rio Grande clammyweed: 1
# Dyer's Greenweed: 1
# Saxifrage faux Orpin: 1
# Drosera lasiantha: 1
# smooth lessingia: 2
# Rooikrans Wattle: 1
# Черноголовка обыкновенная: 1
# Diplotaxis tenuifolia: 1
# common reed: 1
# hoary alyssum: 2
# Γλιστρίδα: 1
# Mexican Oregano: 1
# 白苦柱: 1
# field gentian: 1
# Moss Campion: 1
# mossy saxifrage: 1
# Geranium-like Saxifrage: 1
# felwort: 1
# Alpine Smartweed: 1
# Water Saxifrage: 1
# alpine bistort: 1
# Вьюнок полевой: 1
# Ломонос виноградолистный: 1
# Sandplain lupine: 2
# Gentiane asclépiade: 1
# Мак сомнительный: 1
# Coastal white spider orchid: 1
# Willowleaf Lettuce: 1
# Delicious Sourfig: 1
# Violeta común: 1
# Canadese Fijnstraal: 1
# Zomerfijnstraal: 1
# Pyrenean Gentian: 1
# bog asphodel: 2
# Rusty-leaved Alpenrose: 1
# Burser's gentian: 1
# Isotropis cuneifolia cuneifolia: 2
# Feijão da praia: 1
# Valériane rouge: 1
# pennyroyal bluecurls: 1
# Firewood Banksia: 1
# 雙心皮草: 2
# small balsam: 1
# Drosera macrophylla: 1
# Gulsporre: 1
# Minnie Daisy: 1
# Senecione sudafricano: 1
# kielo: 1
# Caladenia × cala: 1
# Abacaxi-de-tingir: 1
# Oxalis incarnata: 1
# scrambling lily: 1
# Bàlsam emparrador: 1
# Prickly Swamp Wattle: 1
# Nipah: 1
# Yellow Flags: 1
# Taxandria parviceps: 1
# Phytolacca icosandra: 1
# Common Clematis: 1
# sléz přehlížený: 1
# White ginger: 1
# Pyrenäen-Storchschnabel: 1
# Capestar: 1
# Wolfskers: 1
# Bulbine Lily: 1
# Variable sallow wattle: 1
# Acacia verticillata verticillata: 4
# Cherry Ballart: 1
# River Rose: 1
# Mountain Pepper: 3
# Spreading Wattle: 2
# Pale Currant Bush: 1
# Leptecophylla divaricata: 2
# Avalanche lily: 1
# Dollrose Storksbill: 1
# Звездчатка злаковая: 1
# Tillandsia straminea: 1
# straw-colored flatsedge: 1
# Canada lily: 1
# Chlorophytum cooperi: 1
# Scarlet Rosemallow: 1
# Bush Maerua: 1
# Verticordia grandiflora: 1
# flannel cudweed: 1
# Salad Twinleaf: 1
# Гулявник лекарственный: 1
# Герань сибирская: 1
# Calectasia valida: 1
# Dwarf Chenille Plant: 1
# Pennsylvania sedge: 1
# 島田氏雞兒腸: 1
# 臺灣牛皮消: 1
# large gnat-orchid: 1
# Pincushion Mistletoe: 1
# Trifolium alpinum: 1
# drunken berry: 2
# 饭包草: 1
# eastern mantis orchid: 2
# Black-beaked Triggerplant: 1
# Drosera barbigera: 1
# Spiny Rice-Flower: 2
# Перестріч лучний: 1
# Carousel spider orchid: 1
# ハマナス: 2
# Salvia × floriferior: 1
# 馬先蒿: 1
# Kangaroo Grass: 1
# 鐵掃帚: 1
# kurtturuusu: 1
# Common Black Jack: 1
# Heidenelke: 1
# Glistnik jaskółcze ziele: 1
# Winged Stackhousia: 1
# tiny bedstraw: 1
# Coffee: 1
# Mediterranean Stork's-bill: 1
# 栾属: 2
# Asian spiderflower: 1
# Common Lionface: 1
# Pigea vernonii vernonii: 1
# Fleshy Tree Orchid: 3
# Prickly mingimingi: 1
# bacon and eggs: 2
# Pavot du Pays de Galles: 7
# Conospermum huegelii: 1
# common bird-of-paradise flower: 1
# Indian Zehneria: 1
# Big-leaved Acacia: 1
# California loosestrife: 1
# Russian knapweed: 1
# Nevada smokebush: 1
# Бородавник обыкновенный: 1
# purple lettuce: 1
# Oregano: 1
# European goldenrod: 1
# Ipil: 1
# Tripa-de-Ovelha: 1
# snakebush: 1
# Platylobium parviflorum: 2
# Solanum silvestre: 1
# Senecio madagascariensis: 1
# Myriophyllum votschii: 1
# Chiloglottis chlorantha: 1
# White Maire: 1
# Papaver heterophyllum: 1
# Trifolium dichotomum: 1
# Large Dewflower: 1
# Weichsel: 1
# Karvi: 1
# common bogbuttons: 1
# Corydale jaune: 1
# Штернбергия зимовникоцветная: 1
# Rikkalutukka: 1
# Grevillea celata: 1
# Mile-a-minute Vine: 1
# Caladenia denticulata: 1
# Blood Heath: 1
# Maiden Pink: 1
# Joseph's spider orchid: 1
# Camphor Storksbill: 1
# Bushveld Koobooberry: 1
# lír přímořský: 1
# Platysace compressa: 1
# 巴氏鐵線蓮: 1
# 二裂唇莪白蘭: 2
# 緣毛松蘭: 2
# 紅斑松蘭: 2
# 筆頭蛇菰: 2
# Zieria laevigata: 1
# Tádega: 1
# Pale pink-sorrel: 2
# Ahomansikka: 1
# black crowberry: 1
# Wrzos zwyczajny: 1
# Epacris microphylla: 1
# Hibbertia saligna: 1
# Echium sabulicola sabulicola: 1
# Pacar Air: 1
# Arrowroot Orchid: 1
# Астрагал солодколистий: 1
# Colchique d'automne: 1
# milkwort boronia: 1
# Speronella fior-cappuccio: 1
# veined spider orchid: 7
# red beard orchid: 3
# Narrow-lipped spider-orchid: 4
# Rhododendron tomentosum: 1
# Acacia myrtifolia: 1
# Caladenia leptochila leptochila: 1
# pygmy finger orchid: 1
# renouée à feuilles de patience: 1
# Corrigiole des rives: 1
# Chondrille à tige de jonc: 1
# Creeping Baby's-breath: 1
# Peka-a-waka: 2
# Leafless Clematis: 1
# 鸭跖草: 1
# Anglestem Buckwheat: 1
# Spindly Spiderhead: 1
# Oxalis punctata: 1
# Water Buttons: 1
# Small Triggerplant: 1
# Scilly Pigmyweed: 2
# cutleaf evening primrose: 1
# Drosera indumenta: 1
# Pygmy Purslane: 2
# Pink Bladderwort: 1
# 雞屎藤: 1
# Callicoma: 1
# sweet vernal grass: 1
# Artánita: 1
# Chinese wisteria: 1
# Spoon Leaved Cudweed: 1
# Plantago maritima serpentina: 1
# Narrow-leaf Wax Flower: 2
# Knotted Crane's-bill: 1
# Styphelia recurvisepala: 1
# one-leaved donkey orchid: 12
# Isopogon mnoraifolius: 1
# Small Waxlip Orchid: 1
# Wallum sun orchid: 2
# Boronia spathulata: 1
# Cyclamen graecum graecum: 2
# Anarthria scabra: 2
# Bossiaea webbii: 1
# Arrowsmith spider orchid: 3
# 寬葉雀稗: 1
# Chloanthes parviflora: 2
# Indian fig opuntia: 2
# Pale Tulp: 1
# Ipomoea coccinea: 1
# blue grass lily: 1
# Onion weed: 2
# 香附子: 1
# 两型豆: 1
# elegant hair grass: 1
# 藿香蓟: 1
# Japanese mazus: 1
# 刺蓼: 1
# Spiky Guinea Flower: 1
# Senecio carnosulus: 1
# Australian Blackthorn: 1
# small-fruited may: 1
# Isopogon petiolaris: 1
# Poranthera obovata: 2
# pale groundsel: 1
# None: 2
# Lavender Grevillea: 1
# delta mudwort: 1
# Giant Herb-Robert: 1
# tall greenhood: 1
# forest boronia: 2
# Gompholobium knightianum: 1
# Golden Pomaderris: 1
# Orange Bell-climber: 2
# Adenanthos cuneatus: 1
# コウリンタンポポ: 1
# Feldahorn: 1
# Sydney golden wattle: 1
# Leschenaultia formosa: 1
# dune fan-flower: 1
# trailing guinea flower: 1
# hairy mitrewort: 1
# Correa reflexa speciosa: 1
# White Wall-rocket: 1
# Gnat orchid: 1
# Kleines Springkraut: 1
# cotton fireweed: 1
# アメリカオニアザミ: 2
# Margarita costera: 1
# ビロードモウズイカ: 1
# アカツメクサ: 1
# silver daisy-bush: 1
# Black's goodenia: 1
# Morelotia octandra: 1
# Hörmanns Läusekraut: 1
# Greenbract Froetang: 1
# Strap-leaf sagittaria: 2
# Chapman's spider orchid: 1
# Sharpleaf groundcherry: 1
# fuchsia heath: 1
# sticky everlasting: 1
# Digger's Speedwell: 1
# Persicaria arifolia: 1
# Chelone glabra: 1
# Gentiana andrewsii: 1
# Ipheion uniflorum: 1
# Eryngium pinnatifidum: 2
# Grevillea oleoides: 1
# Kirk's tree daisy: 1
# Pepino cimarrón: 1
# Lesser swine-cress: 1
# Pixie cap: 2
# choke cherry: 1
# Lewis flax: 1
# Saline Plantain: 1
# Royal Triggerplant: 1
# Taiwan Cherry: 1
# Cirsium muticum: 2
# Verbena hastata: 1
# Echinocystis lobata: 1
# White Point-vetch: 1
# pink knotweed: 1
# Mazorquilla: 1
# Posy Triggerplant: 1
# Stylidium acuminatum meridionale: 1
# Kalm's Lobelia: 2
# 杭子梢: 1
# Pinyon Brickellbush: 1
# black chokeberry: 1
# 牻牛儿苗: 1
# Manyflowered Ipomopsis: 3
# aster lancéolé: 1
# Discolored Obovate Rhynchotechum: 1
# longroot smartweed: 1
# 少蕊败酱: 2
# silvery lupine: 3
# corkystem passionvine: 1
# Fetid marigold: 1
# Pacific trillium: 1
# Charuteira: 1
# Pittosporum tenuifolium: 1
# Aromo Australiano: 1
# Sea Spurge: 2
# Sawtooth Candyleaf: 1
# European water-horehound: 1
# Lady's Thumb: 1
# MacDougal verbena: 1
# Pink Honeysuckle: 1
# Barba de bode: 1
# Tanaecium dichotomum: 1
# Brown Knapweed: 1
# Conospermum taxifolium: 1
# 高雄飄拂草: 2
# Carrot Tops: 1
# Narrowleaf Milkweed · Algodoncillo de Hojas Delgadas: 1
# Twiggy Daisybush: 1
# Bigbract Verbena: 1
# Narrow-lipped Hammer Orchid: 1
# Flying Duck Orchid: 2
# King-in-his-carriage: 1
# Demarz's Tinsel Lily: 1
# southern coastal bushmallow: 1
# Rosy Sundew: 1
# threadleaf groundsel: 1
# purple star-thistle: 1
# swamp agrimony: 1
# Blueberry Lily: 1
# Drummond's false pennyroyal: 1
# wild pansies: 2
# Pittosporum viscidum: 1
# bog cranberry: 2
# Tillandsia vernicosa: 1
# Pitayo sina: 1
# Austrocylindropuntia floccosa: 1
# Austrocylindropuntia lauliacoana: 1
# annual buckwheat: 1
# ヘクソカズラ: 1
# Western Columbine: 1
# Scarlet Grevillea: 1
# spreading fleabane: 1
# Southern Flax: 1
# Philotheca trachyphylla: 1
# ragged nettlespurge: 1
# Oxalis dichondrifolia: 1
# pink bunny orchid: 1
# napier grass: 1
# Catnip: 1
# Hierba de fuego: 1
# Round-stem False Foxglove: 1
# Yorkshire fog: 1
# Pink jasmine: 1
# Peruvian zinnia: 1
# Skunkweed: 1
# Montia calycina: 1
# Mirto: 1
# Mexican tea: 1
# painted trillium: 1
# American groundnut: 1
# Small-leaved pohuehue: 1
# Pterodon pubescens: 1
# Tropical sage: 1
# Japanese Clover: 1
# Miconia affinis: 1
# common lantana: 1
# great basin rabbitbrush: 1
# Bruyère vagabonde: 1
# common hovea: 1
# Calystegia sepium sepium: 1
# Verveine officinale: 1
# Barbados Lily: 1
# Seaside Buckwheat: 1
# Common Spikeweed: 1
# Purslane Speedwell: 1
# Dillwynia laxiflora: 1
# Arizona thistle: 1
# Autumn Squill: 1
# large pansy orchid: 1
# tall bush-clover: 1
# Redroot Buckwheat: 1
# Candelabra Bush: 1
# ワルナスビ: 1
# deerbrush ceanothus: 1
# Southern Russian Thistle: 1
# golden hedge-hyssop: 1
# Long-Bracted Gavilea: 1
# feather dalea: 1
# Fremont barberry: 1
# Small-leaf Globemallow: 1
# slender goldentop: 2
# Rose Coreopsis: 2
# Grindelia nuda aphanactis: 1
# Perpétua-roxa: 1
# Ageratina altissima: 1
# Bico-de-nambu: 1
# groundcover milkvetch: 1
# showy fanpetals: 1
# blunt-leaf heath: 1
# Cistus inflatus: 1
# Honey Caladenia: 1
# seneci pirinenc: 1
# Saxifraga geranioides: 1
# snow-on-the-mountain: 1
# Water Star-Grass: 1
# Cynanchum chinense: 1
# Lanceleaf Blanketflower: 2
# Tropic Croton: 1
# Nodding nixie: 1
# Héliotrope d'Europe: 1
# Réséda jaune: 1
# mayapple: 1
# alpine azalea: 1
# Dainty Blue China Orchid: 1
# fetgera blanca: 1
# panical blau: 1
# Grande ortie: 1
# Géranium à feuilles rondes: 1
# Cardón colorado: 1
# American eelgrass: 1
# Common Twayblade: 1
# Rosy Hyacinth Orchid: 1
# Cymbalaire des murs: 1
# Parish's nightshade: 1
# Balsamine à petites fleurs: 1
# Pūriri: 1
# Phebalium graniticola: 1
# The Pincushion: 1
# Bletia neglecta: 1
# Galega officinalis: 1
# Combleaf Gazania: 1
# Reynoutria japonica: 1
# Abrojo: 1
# Foreland Viooltjie: 1
# Tabebuia nodosa: 1
# Gewöhnliches Alpen-Edelweiß: 1
# silky beach pea: 1
# Woolly Burdock: 1
# Prairie Goldenrod: 1
# Stranglewort: 1
# russet bushwillow: 1
# Asthma plant: 1
# wild bergamot: 1
# Barba de chivo: 1
# Echeandia mexicana: 1
# Australian parsnip: 1
# Bastard Sandalwood: 1
# saguaro: 1
# Caledon Bluebell: 1
# Downy Goldenrod: 1
# Helianthemum nummularium pyrenaicum: 1
# Alchemilla fissa: 1
# Saxifraga moschata: 1
# Phyteuma hemisphaericum: 1
# Sticky Groundsel: 1
# dwarf snapdragon: 1
# Rosmarin: 1
# Corethrogyne filaginifolia: 1
# Poataniwha: 1
# Сколимус испанский: 1
# Maracujá-de-cobra: 1
# Hall's Honeysuckle: 1
# Pacific ninebark: 1
# Red Helleborine: 1
# Illinois bundleflower: 1
# Scaldweed: 1
# Common Yellowwort: 1
# Rote Schuppenmiere: 1
# Amole: 1
# Mountain True-Eye: 1
# Alternating Sorrel: 1
# blue waxweed: 1
# Prospero autumnale: 1
# Ajo Blanco: 1
# Aufrechter Sauerklee: 1
# Priva lappulacea: 1
# clasping water horehound: 1
# Lambstail: 1
# Hybrid Lindheimer's Paintbrush: 1
# Cirse de Montpellier: 1
# Canelilla: 1
# petite astrance: 1
# bristly sarsaparilla: 1
# Purple Bladderwort: 1
# bristle thistle: 1
# sea purslane: 1
# Elliott's goldenrod: 1
# Northern St. John's-wort: 1
# Канадска злолетница: 1
# Winged Loosestrife: 1
# Roundleaf Dottypea: 1
# longhorn steer's-head: 2
# yellow fritillary: 3
# Nuttall's Lobelia: 1
# Gefleckte Taubnessel: 1
# Afrikanischer Tulpenbaum: 1
# Siam weed: 1
# Christmas Orchid: 1
# Southwest Texas Strawberry Cactus: 1
