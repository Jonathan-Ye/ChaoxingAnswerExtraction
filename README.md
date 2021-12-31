# ChaoxingAnswerExtraction

## 基于Python的超星学习通考试页面的答案提取与合并项目
2021年12月31日


### 1	引言
代人有一代人的使命，一代人有一代人的担当。新时代，给了青年人更多新平台、新机会，新时代，广大青年生逢其时。青年兴则国家兴，青年强则国家强。青年一代有理想、有本领、有担当，国家就有前途，民族就有希望。因此本项目为了让更多青年学习了解时事政治，使用Python语言提取了[人民日报官网](http://paper.people.com.cn/)的信息，包括纸质报纸的PDF批量下载，以及相关数据的提取等功能。

### 2	项目背景

#### 2.1	项目目的
抛弃传统纸质报纸，通过Python高效获取数据，提高信息获取效率以及质量。软件核心功能包括：
    下载PDF文件，随时随地可以获得和纸质版一样的阅读体验；
    爬取每日头版内容，分析国家发展导向，洞察关键信息。

#### 2.2	适用人群
想快速了解，查看或检索人民日报信息的人群。

### 3	概要设计
### 3.1	软件核心功能
下载人民日报PDF文件，因网站只开放前两年的数据（截至2021年6月14日可追溯至2020年1月1日）。由于人民日报官网于2020年7月1日改版，本软件完美支持新版及旧版本。保存的PDF文件按照日期分类保存至对应文件夹中。
### 3.2	技术
本软件基于Python的requests-bs4技术路线开发。
### 3.3	开发环境
操作系统版本：
Windows 10 20H2

Python版本：
Python 3.8 64-bit

库版本：
requests 2.22.0
beautifulsoup4 4.9.3
jieba 0.42.1
wordcloud 1.8.1

### 4	结语
本软件旨在增强公民意识，帮助提高自身政治素质，提高政治参与度，希望大家可以通过本软件学到更多的知识。
