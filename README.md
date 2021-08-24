# SICNU_Report_Epidemic
四川师范大学疫情健康报告打卡
---
#### 安装Selenium
`pip install selenium`
#### 下载对应的Chrome和ChromeDriver
Linux，Mac，Windows都可以  
Chrome：https://www.google.com/chrome/  
ChromeDriver：https://chromedriver.chromium.org/downloads  
#### 填写用户名和密码
打开sicnu_report.py，修改下面的信息，支持多账号，依次为用户名，密码，本科生或研究生；
```
userInfo = [
    ["2020******", "*******", undergraduate],
    ['2020******', '*******', postGraduate]
]
```
#### Linux下可配合crontab定时运行
先看linux上有没有crontab，没有百度安装一下；  
安装好的，输入：`crontab -e`  
按`i`：  
`0 7 * * * cd /path/to/pyfile && nohup /root/anaconda3/bin/python -u sicnu_report.py>log.txt 2>&1 &`  
输入`:wq`保存   
查看刚设置的定时任务：   
`crontab -l`
#### 注意
有图形界面的，可以注释掉这三行，没有图形界面的，一定要有，不然可能会报错。
```
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
```
