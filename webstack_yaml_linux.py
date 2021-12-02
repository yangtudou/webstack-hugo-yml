import glob
from ruamel import yaml
#没有子目录
taxonomy = [ ]
websitpages = [ ]
for base in glob.glob('./websitepages/*.txt', recursive=True):
    taxonomy.append(base.strip('./websitepages | txt').split('/'))
    path = [base]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            webs.append({'title': w.split()[0], 'logo': w.split()[1], 'url': w.split()[2], 'description': w.split()[3]})
        websitpages.append(webs)

taxonomys = [ ]
for i in range(len(taxonomy)):
    x = {'taxonomy': ''.join(taxonomy[i]), 'icon': 'icon', 'links': websitpages[i]}
    taxonomys.append(x)
#有子目录
taxonomy_with_term = [ ]
websitpages_with_term = [ ]
term = [ ]
for i in glob.glob('./websitepages/*/', recursive=True):
    taxonomy_with_term.append(i.strip('.\websitepages | txt').split('/'))
for base in glob.glob('./websitepages/*/*.txt', recursive=True):
    term.append((base.strip('./websitepages | txt').split('/'))[1])
    path = [base]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            webs.append({'title': w.split()[0], 'logo': w.split()[1], 'url': w.split()[2], 'description': w.split()[3]})
        websitpages_with_term.append(webs)


terms = [ ]
taxonomy_with_terms = [ ]
for i in range(len(term)):
    terms.append({'term': term[i], 'links': websitpages_with_term[i]})
for i in range(len(taxonomy_with_term)):
    taxonomy_with_terms.append({'taxonomy': ''.join(taxonomy_with_term[i]), 'icon': 'icon', 'list': terms})


ggg = taxonomys + taxonomy_with_terms



with open('./test.yml', 'w', encoding='utf-8') as f:
    yaml.dump(ggg, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

