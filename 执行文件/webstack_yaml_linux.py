#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from ruamel.yaml import YAML
yaml = YAML()

# 读取网站数据库
with open('./执行文件/WebSiteInfo.json','r',encoding='utf8')as fp:
    WebSiteInfo = json.load(fp)

TaxonomyInfoWithoutTerms = []
# TaxonomyInfoWithTerms = []

# 没有子分类的数据
TaxonomyInfoWithoutTerms_infos = [
    [
        "常用",
        "fa-star",
        [
            "土豆仓库",
            "Github",
            "DockerHub",
            "Pinterest",
            "Behance",
            "Dribbble",
            "Medium",
            "Youtube"
        ]
    ],
    [
        "博客",
        "fa-coffee",
        [
            "GXNAS",
            "P3terxZone",
            "reuixiy",
            "三言字体"
        ]
    ],
    [
        "资源下载",
        "fa-download",
        [
            "锯齿一号",
            "果核剥壳",
            "uu_win"
        ]
    ]
]

# 有子分类的数据
# TaxonomyInfoWithTerms_infos = []

# 添加没有子目录的函数
# 参数 TaxonomyInfoWithoutTerm_website 必须以 list 方式存在
def add_TaxonomyInfoWithoutTerm(TaxonomyInfoWithoutTerm_name,TaxonomyInfoWithoutTerm_icon,TaxonomyInfoWithoutTerm_website):
    TaxonomyInfoWithoutTerm = {
        "taxonomy": "无子分类主分类名",
        "icon": "fa-star",
        "links": []
    }
    TaxonomyInfoWithoutTerm["taxonomy"] = TaxonomyInfoWithoutTerm_name
    TaxonomyInfoWithoutTerm["icon"] = TaxonomyInfoWithoutTerm_icon
    TaxonomyInfoWithoutTerm["links"] = []
    for i in TaxonomyInfoWithoutTerm_website:
        if i in WebSiteInfo:
            TaxonomyInfoWithoutTerm["links"].append(WebSiteInfo[i])
    return TaxonomyInfoWithoutTerm

# 添加有子目录的函数
# def add_TaxonomyInfoWithTerm(TaxonomyInfoWithTerm_name,TaxonomyInfoWithTerm_icon,TaxonomyInfoWithtTerm_website):
#     TaxonomyInfoWithTerm = {
#         "taxonomy": "有子分类网站分类",
#         "icon": "分类标签",
#         "list": [
#             {
#                 "term": "子分类名字",
#                 "links": []
#             }
#         ]
#     }
#     TaxonomyInfoWithTerm["taxonomy"] = TaxonomyInfoWithTerm_name
#     TaxonomyInfoWithTerm["icon"] = TaxonomyInfoWithTerm_icon
#     return TaxonomyInfoWithTerm

# 整合没有子目录的网站
for i in TaxonomyInfoWithoutTerms_infos:
    TaxonomyInfoWithoutTerms.append(add_TaxonomyInfoWithoutTerm(i[0],i[1],i[2]))

# 整合所有的网站
# websites = TaxonomyInfoWithoutTerms + TaxonomyInfoWithTerms


# 目前只支持没有子分类的生成
# 开始写入，生成的文件在
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.top_level_colon_align = True
yaml.default_flow_style = False
yaml.explicit_start = True
with open('./yaml_update/webstack.yml', 'w', encoding='utf-8') as f:
    yaml.dump(TaxonomyInfoWithoutTerms, f)