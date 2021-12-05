import glob
import os
from tkinter import filedialog
from ruamel import yaml
path = filedialog.askdirectory(initialdir=os.getcwd())
path1 = path + '/*.txt'
path2 = path + '/*/*.txt'
path3 = path + '/webstack.yml'
#没有子目录
taxonomy = [ ]
websitpages = [ ]
for i in glob.glob(path1, recursive=False):
    taxonomy.append(i.strip('.txt').split('\\'))
    path = [i]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            webs.append({'title': w.split()[0], 'logo': w.split()[1], 'url': w.split()[2], 'description': w.split()[3]})
        websitpages.append(webs)

taxonomys = [ ]
for i in range(len(taxonomy)):
    x = {'taxonomy': taxonomy[i][1], 'icon': 'icon', 'links': websitpages[i]}
    taxonomys.append(x)

#有子目录
taxonomy_with_term = [ ]
websitpages_with_term = [ ]
term = [ ]
for i in glob.glob(path2, recursive=True):
    taxonomy_with_term.append(i.strip('.txt').split('\\')[1])
for base in glob.glob(path2, recursive=True):
    term.append((base.strip('.txt').split('\\'))[2])
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
for i in range(1,len(taxonomy_with_term)):
    taxonomy_with_terms.append({'taxonomy': ''.join(taxonomy_with_term[i]), 'icon': 'icon', 'list': terms})



ggg = taxonomys + taxonomy_with_terms



with open(path3, 'w', encoding='utf-8') as f:
    yaml.dump(ggg, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

