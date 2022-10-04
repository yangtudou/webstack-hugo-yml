#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from ruamel.yaml import YAML
yaml = YAML()
from WebSiteInfo import *

with open('TaxonomyInfo.json','r',encoding='utf8')as fp:
    TaxonomyInfo = json.load(fp)


# 常用
TaxonomyInfo[0]["links"] = [
    土豆仓库,
    土豆博客,
    Github,
    DockerHub,
    Pinterest,
    Behance,
    Dribbble,
    Medium,
    Youtube
]

# 博客
TaxonomyInfo[1]["links"] = [
    GXNAS,
    P3terxZone,
    reuixiy,
    三言字体
]

# 资源下载
TaxonomyInfo[2]["links"] = [
    锯齿一号,
    果核剥壳,
    uu_win

]

# 实用工具
TaxonomyInfo[3]["links"] = [
    IP可用性检测工具
]
# 设计 --> 三维设计
TaxonomyInfo[4]["list"][0]["links"] = [
    blender,
    材质贴图
]

# 设计 --> 包装设计
TaxonomyInfo[4]["list"][1]["links"] = [
    世界创意包装
]

# 设计 --> 工业设计
TaxonomyInfo[4]["list"][2]["links"] = [
    普象网,
    二维码演示
]


# 开始写入，生成的文件在 /配置文件
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.top_level_colon_align = True
yaml.default_flow_style = False
yaml.explicit_start = True
with open('../webstack.yml', 'w', encoding='utf-8') as f:
    yaml.dump(TaxonomyInfo, f)