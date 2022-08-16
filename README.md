# 功能

本项目实现了12306火车抢票系统的自动登录，可自动过滑动验证码，自动查询车票是否开售，一旦放票可以自动选票并提交订单，可以选学生票，你只需在10分钟内支付即可。需要注意的是该程序要在放票前几分钟运行，要不然票都被抢光了再运行神仙也抢不到。

# 环境

本项目测试环境：win10，python3，selenium > 4.0，chrome = 104，pycharm，chromedriver.exe = 104

chromedriver.exe版本为104，可以根据自己电脑浏览器版本重新下载chromedriver.exe替换

chromedriver.exe下载地址：http://chromedriver.storage.googleapis.com/index.html

# 说明

**提前根据自身要求修改好代码，然后找一个已经能预订的车票测试一下该程序能否帮你抢到合适的票，再用它去抢票 **



程序默认抢的是硬卧，如果要抢其他类型的车票例如硬座请修改`value=//td[8]`为`value=//td[10]`

并且该段代码能保证即使同一车次的列车既经过郑州，又经过郑州西，选出来的车票仍是唯一的你想要的那张

```python
# 车票出发站
start_station = str(ticket.text).replace("复\n", "").replace("智\n", "").split('\n')[1]
# 车票到达站
arrival_station = str(ticket.text).replace("复\n", "").replace("智\n", "").split('\n')[2]
# 如果车票的车次等于想要的车次并且车票的出发站等于您的出发站，到达站等于您的到达站并且硬卧的状态不是候补则点击预订，这样可使得车票唯一
 # value = '//td[2]'表示商务座特等座，'//td[3]'表示一等座，'//td[4]'表示二等座，'//td[5]'表示高级软卧，'//td[6]'表示软卧 ，'//td[7]'表示动卧，'//td[8]'表示硬卧，'//td[9]'表示软座，td[10]表示硬座
if ticket.find_element(by=By.CLASS_NAME,value='number').text == conf.trainnumber and start_station == conf.fromstation and arrival_station == conf.destination and ticket.find_element(by=By.XPATH, value='//td[8]').text != "候补":

```

下面是选择乘车人，如果不是学生就把`driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()`注释掉即可

```python
# 选择乘车人，如果是学生，则需要确认购买学生票
driver.find_element(by=By.XPATH, value='//*[@id="normalPassenger_0"]').click()
# 点击确认购买学生票，如果不是学生，把这行注释了就行
driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()
# 第二个乘车人
# driver.find_element(by=By.XPATH, value='//*[@id="normalPassenger_1"]').click()
# 如果第二个乘车人也是学生，则需要点击确认第二个人也购买学生票
# driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()
```

如果抢的是硬座就需要选座，把注释解开即可

```python
# 选座  F座
# driver.find_element(by=By.ID, value='1F').click()
# 第二个人选座
# driver.find_element(by=By.ID, value='2D').click()
```

