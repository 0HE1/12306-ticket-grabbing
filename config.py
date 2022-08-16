class Config:
    def __init__(self):
        # 账号
        self.username = '#########'
        # 密码  每3天12306就会强制要求修改一次密码才能使用账号密码登录
        self.password = '#########'
        # 出发地 一定要写清楚 比如：北京西站就要写北京西站，不要只写北京
        self.fromstation = '#########'
        # 目的地 一定要写清楚 比如：郑州西站就要写郑州西站，不要只写郑州
        self.destination = '#########'
        # 出发日期，格式一定要是这样：2022-08-17
        self.date = '#########'
        # 车次   例如Z146,G127
        self.trainnumber = '#########'
