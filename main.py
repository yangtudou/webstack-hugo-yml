#!/usr/bin/env python3
#首先需要自己准备一个文件夹，最外层的文件夹命名方式随便。
#内层的文件夹命名方式是这样的，没有子目录的就直接用把分类名写成 归类名.txt 这样的。有子目录的以子目录的名字建文件夹，在文件夹里再新建 归类名.txt
'''
-- root
      + xxx.txt
      + xxx.txt
      + xxx
          + xxx.txt
          + xxx.txt
      + xxx.txt
      + xxx.txt
'''
#xxx.txt 需要四个参数 1.名称 2.图标 3.链接 4.网站描述
#目前图片还没解决怎么做，只能自己添加。后期研究怎么网上直接爬下来放进去。
#计划是用base64代替图片格式来做，做个仓库专门调用。图片命名方式和名称一致，目前是png格式。

#需要的模块 glob、ruamel、yaml
import glob

taxonomy = [ ]
websitpages = [ ]
for base in glob.glob('./websitepages/*.txt', recursive=True):
    taxonomy.append(base.strip('./websitepages | txt').split('/'))
    path = [base]
    for f in path:
        file = open(f, encoding='utf-8')
        webs = [ ]
        for w in file:
            ws = {'title': w.split()[0], 'logo': w.split()[1], 'url': w.split()[2], 'description': w.split()[3]}
            webs.append(ws)
        websitpages.append(webs)

ggg = [ ]

for i in range(len(taxonomy)):
    x = {'taxonomy': ''.join(taxonomy[i]), 'icon': 'icon', 'link': websitpages[i]}
    ggg.append(x)
print(websitpages)
# from ruamel import yaml
# with open('./test.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(ggg, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

#print(glob.glob('./websitepages/*/*.txt', recursive=True))
