# 引入模块
import glob
import os
from ruamel.yaml import YAML
####################################
# 没有子目录
# 根目录名
taxonomy = [ ]
# 网站
websitpages = [ ]
# 先提取网站路径，再根据路径来提取每个文件内容
for base in sorted(glob.glob('./websitepages/*.txt', recursive=True), key=os.path.getmtime):
    taxonomy.append(base.strip('./websitepages | txt').split('/'))
    path = [base]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            webs.append(
                {
                    'title': w.split()[0],
                    'logo': w.split()[1],
                    'url': w.split()[2],
                    'description': w.split()[3]
                }
            )
        websitpages.append(webs)
# 分离根目录名
taxonomys = [ ]
for i in range(len(taxonomy)):
    x = {
        'taxonomy': ''.join(taxonomy[i]),
        'icon': 'icon',
        'links': websitpages[i]
    }
    taxonomys.append(x)
######################################
# 有子目录
# 根目录名
taxonomy_with_term = [ ]
# 网站
websitpages_with_term = [ ]
# 子目录名
term = [ ]
for i in sorted(glob.glob('./websitepages/*/', recursive=True), key=os.path.getmtime):
    taxonomy_with_term.append(i.strip('./websitepages | txt').split('/'))
for base in sorted(glob.glob('./websitepages/*/*.txt', recursive=True), key=os.path.getmtime):
    term.append((base.strip('./websitepages | txt').split('/'))[1])
    path = [base]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            webs.append(
                {
                    'title': w.split()[0],
                    'logo': w.split()[1],
                    'url': w.split()[2],
                    'description': w.split()[3]
                }
            )
        websitpages_with_term.append(webs)


terms = [ ]
taxonomy_with_terms = [ ]
for i in range(len(term)):
    terms.append(
        {
            'term': term[i],
            'links': websitpages_with_term[i]
        }
    )
for i in range(len(taxonomy_with_term)):
    taxonomy_with_terms.append(
        {'taxonomy': ''.join(taxonomy_with_term[i]),
         'icon': 'icon',
         'list': terms
         }
    )
######################################################
# 开始写入 yaml 文件
ggg = taxonomys + taxonomy_with_terms
yaml = YAML()
# 换行对齐什么的，目前有点问题，但不影响使用
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.top_level_colon_align = True
yaml.default_flow_style = False
yaml.explicit_start = True
with open('../webstack.yml', 'w', encoding='utf-8') as f:
    yaml.dump(ggg, f)
