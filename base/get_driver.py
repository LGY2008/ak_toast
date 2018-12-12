from appium import webdriver
def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.44.101:5555'
    # 获取使用toast
    desired_caps['automationName'] = 'Uiautomator2'
    # 输入中文
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    # app信息
    desired_caps['appPackage'] = "com.vcooline.aike"
    desired_caps['appActivity'] = ".umanager.LoginActivity"
    return webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps )

