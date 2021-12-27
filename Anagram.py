str = ['code', 'doce', 'ecod', 'framer', 'frame']
str2 = ['code', 'aaagmnrs', 'anagrams', 'doce', 'code', 'aaagmnrs', 'code']
str3 = ['fqwltvzkqt', 'volphckcyufdqmlglimklfzktgygdttnhcvpfdfbrp', 'lkvshwywshtdgmbqbkkxcvgumo',
  'mwvytbytnuqhmfjaqtgngcwkuzyamnerphfmwevh', 'lezohyeehbrcewjxvceziftiqtntfsrptugtiznorvonzjfea',
  'gamayapwlmbzitzszhzkosvnknber', 'ltlkggdgpljfisyltmmfvhybljvk', 'pcflsaqevcijcyrgmqirzniax',
  'kholawoydvchveigttxwpukzjfh', 'brtspfttotafsngqvoijxuvq', 'ztvaalsehzxbshnrvbykjqlrzzfm',
  'vyoshiktodnsjjpqplciklzqrxloqxrudygjty', 'leizmeainxslwhhjwslqendjvx', 'yghrveuvphknqtsdtwxcktmwwwsdthzmlmbh',
  'kmouhpbqur', 'fxgqlojmwsomowsjvpvhznbsilhhdkbdxqgrgedpzch', 'gefeukmcowoeznwhpiiduxdnnlbnmyjyssbsococdzcu',
  'nkrfduvouaghhcyvmlkza', 'jpfpyljtyjjpyntsefxiswjuten', 'ycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvguxtrdsdf',
  'fssmeluodjgdgzfmrazvndtaur', 'kugs', 'dpawxitivdubbqeonycaegxfjkkl', 'fkraoheucsvpiteqrs',
  'gkaaaohxxzhqjtkqaqhkwbe', 'bpmglbjipnujywogwc', 'lkyrdejaqufowbigrsnjniegvd',
  'otugocedktcbbufnxorixibbdfrzuqsyrfqghoyqevcuanuu', 'szitaoaowsxyglafbwzddoznrvjqeyqignpi',
  'ruijvyllsibobjltusrypanvybsfrxtlfmpdidtyozoolz', 'lgdgowijatklvjzscizrkupmsoxftumyxifyunxucubvk', 'ctkqlr',
  'qgzjvjwzizppvso', 'flvioemycnphf', 'tbnwedtubynsbirepgcxfgsfomhvpmymkdoh', 'ttyyc', 'ibbeaxniwjkfvabnrll',
  'maglythkgla', 'zgkeulyrpaeurdvexqlwgakdtbihmfrjijanxkhrqdllecy', 'pcflsaqevcijcyrgmqixnzira', 'klqrct',
  'ibbeaxniwjkfvanrbll', 'vyoshiktodnsjjpqplciklzqrxloqxrudyyjtg',
  'ycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvgxddftsru', 'yyctt', 'yghrveuvphknqtsdtwxcktmwwwsdtlhbhmmz',
  'vyoshiktodnsjjpqplciklzqrxloqxrugyytjd', 'cttyy', 'brtspfttotafsngqvoiqxuvj', 'lkyrdejaqufowbigrsnjvedgin',
  'volphckcyufdqmlglimklfzktgygdttnhcvpfdrbpf', 'qgzjvjwzizpsovp'
]


def remove_duplicate(matrix):
    result = []
    for element in  sort_and_remove(matrix):
        result.append(matrix[element])
    return print(result)


def sort_and_remove(matrix):
    copy = []
    unique = []
    for element in matrix:
        copy.append("".join(sorted(element)))
    for element in set(copy):
        unique.append(copy.index(element))
    return sorted(unique)

remove_duplicate(str)
remove_duplicate(str2)
remove_duplicate(str3)