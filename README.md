scrapy爬取BOSS直聘网、洛杉矶时报、网易云音乐等
====
`声明：所有爬虫均为个人学习所用，对所爬网站服务器带来的压力感到抱歉，本人所有项目暂停时间均超过5s，绝无使用爬虫对网站进行攻击的想法，如有使用该项目进行商业活动或其他造成侵权行为的活动，所造成的法律后果由使用者自行承担。`
## 项目一：[bossZhipin](https://github.com/spytensor/Spiders/tree/master/bossZhipin)
**所要爬取的职位分类如下：**<br> 
* 机器学习  深度学习  图像处理  图像算法   
* 图像识别  语音识别  算法研究员 自然语言处理<br> 

**所需要的职位信息如下：**<br> 
* 薪资待遇   工作经验   学历   标签   发布时间  <br> 
* 工作地点    企业名称   企业类型    企业规模   企业融资情况  
* HR姓名   HR职业   HR在线情况   工作职位描述   工作标题   详情页面<br> 

    `注：后续将对所爬数据进行清洗和分析`<br>
## 项目二：[leifengWang](https://github.com/spytensor/Spiders/tree/master/leifeng)
**所抓取的分类(截止2018年5月4日):**<br>
* 业界  人工智能  智能驾驶  AI+ Aintech&区块链  
* 未来医疗  网络安全  AR/VR 机器人  开发者  智能硬件<br>

**所需要的信息如下：**<br>
* 新闻链接  新闻标题  新闻作者  标签<br>

**对所有标题使用jieba分词后进行词云制作，效果如下:**<br>
![](https://github.com/spytensor/Spiders/blob/master/leifeng/leifeng/analysis/leifeng_word3.png)
