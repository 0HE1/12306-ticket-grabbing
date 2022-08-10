# 12306抢票爬虫

本项目基于selenium实现了12306的自动登录，可自动过滑动验证码，自动查询车票是否开售，一旦放票可以自动选票并提交订单，可以选学生票，你只需在10分钟内支付即可。需要注意的是该程序要在放票前几分钟运行，要不然票都被抢光了再运行神仙也抢不到



## 环境

本项目测试环境：win10，python3，selenium > 4.0，chrome = 104，pycharm，chromedriver.exe = 104

chromedriver.exe版本为104，可以根据自己浏览器版本重新下载chromedriver.exe替换

chromedriver.exe下载地址：[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)



## 项目结构

```python
————12306
	————12306.py
	————config.py
	————chromedriver.exe
```



## 车票以及账号信息

在`config.py`中填入账号以及车票信息

```python
class Config:
    def __init__(self):
        # 账号
        self.username = '##########'
        # 密码
        self.password = '##########'
        # 出发地
        self.fromstation = '#####'
        # 目的地
        self.destination = '#####'
        # 出发日期
        self.date = '2022-08-09'
        # 车次   例如Z146,G127
        self.trainnumber = '####'
```



## 说明

`12306.py`中第135~138是选择乘客的，如果乘客不是学生，需要把138行`driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()`注释掉