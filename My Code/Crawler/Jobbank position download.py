'''
Python Application - Crawler

Jobbank.com is one job platform in Canada. 
Crawler analysis and practice aim to optimizine job hunting efficency.
Finished code, run test pass.

Note:
* error warning: internet speed may cause error
* troubleshooting: slow program speed
'''
#Source Code

import requests, gevent, openpyxl, re, time             # 页面请求，excel控制，正则表达式解析positioncode，控制时间 
from bs4 import BeautifulSoup                           # 解析网页源码
from lxml import etree                                  # xpath方法定位检索页面click按钮
from selenium import webdriver                          # 浏览器模拟运行
from selenium.webdriver.chrome.options import Options   # 浏览器静默运行
from gevent import monkey                               # 异步处理页面请求
from gevent.queue import Queue
monkey.patch_all()

# Excel文档操作
wb=openpyxl.Workbook()                              # create excel document 创建新的空的Excel文件,并重命名
sheet = wb.active                                   # 获取活动工作薄
sheet.title = 'postion Canada'                      # 职位工作薄命名
sheet1 = wb.create_sheet(title = 'postion Code')    # 创建新的工作薄并命名，用于保存职位网址代码   

# 写入标题栏
rows1= ['Postion','Website','Place','JD','Salary','Vacancy','Email','Expired Date']              # input title row
sheet.append(rows1)                                                                              # write first row

# 输入搜索条件
position = input('please input your position:' )
place = input('please input your city name:' )
#url='https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=' + str(postion) + '&locationstring=' + str(place) +'&sort=M'   

list1 = []                                                  # 创建存放网址数据的列表
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}       

# Step 1 检索页面操作
def searPage(pK,pP):
    
    # 使用headers

    # 首页检索后的页面
    url0='https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=' + str(pK) + '&locationstring=' + str(pP) +'&sort=M'   


    #  模拟浏览器工作，静默模式
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')  # 设置option,后台运行
    #driver = webdriver.Chrome(options = chrome_options)


    driver = webdriver.Chrome()
    driver.get(url0)
    #print(res.status_code)                                      # confirm status

    #time.sleep(10)      #   等待内容加载

    # 根据检索首页的职位总数，以每一次点击加载20条信息计算，得出总点击数
    clicktime = 0
    while clicktime<2: # 试用X次
        print('start click')
        #button = driver.find_element_by_class_name('.far.fa-chevron-circle-down')
        button = driver.find_element_by_xpath("//*[@class='far fa-chevron-circle-down']") 
        print('find target - Done')
        button.click()
        print('Click - Done')
        #time.sleep(int(clicktime+2))
        clicktime+=1
        print('Click '+str(clicktime)+' times')

    # 职位检索页面解析
    pageSource = driver.page_source                             # 获取Elements中渲染完成的网页源代码
    bs_first = BeautifulSoup(pageSource,'html.parser')          # 使用bs解析网页 
    print('Source Code Analysis - Done')

    # 获取职位代码
    list_kind = bs_first.find('div',class_='results-jobs').find_all('article')  # 提取数据，到 article层

    for i in list_kind:                                         # 遍历提取出的article值
        number1 = i['id']                                       # 取出 id 的值，该值需要继续提取
        url_number = re.compile(r'\d{8}')                       # 使用正则表达式提取id中的数字部分，创建数字规则
        mo  = url_number.search(str(number1))                   # 提取出id中的数据
        mo1 = mo.group()                                        # 返回被查找字符串中实际匹配的文本
        #print(mo1)                                             # 确认返回值正确
        list1.append(mo1)                                       # 把数字存入列表

    print('Source Code Extract - Done')

    # 存入数据
    sheet1.append(list1) 
    wb.save('/Users/chang/Desktop/food postion.xlsx')
    
    # 关闭浏览器
    driver.close()
    print('Step 1 DONE')
    return list1

# Step 2 职位页面信息提取
def position_crawler():
    while not work.empty():
        url = work.get_nowait()     # 用get_nowait()函数可以把队列里的网址都取出
        
        # 获得职位页面地址
        #url2 = 'https://www.jobbank.gc.ca/jobsearch/jobposting/' + str(i) + '?source=searchresults'   # 单个职位页面

        # 浏览器静默方式运行
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')  
        #driver = webdriver.Chrome(options = chrome_options)
        driver = webdriver.Chrome()
        driver.get(url)
        #time.sleep(3) #等待加载，可跳过
        
        # 解锁mail隐藏按钮
        button = driver.find_element_by_class_name('btn-success')
        button.click()
        print('button click - Done')
        #time.sleep(3) #等待加载，可跳过

        # 获得页面源码并解析
        pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
        bs_second = BeautifulSoup(pageSource,'html.parser') # 使用bs解析网页
        print('bs - Done')

        # 点击mail的按钮，等待反馈，时间约为5s
        #time.sleep(5)
        y=0
        for y in range(5):
            y+=1
            time.sleep(2)
            print(str(y))

        # 提取mail，出现异常频率较高，可能是由于触发反爬虫机制，因此采用两种方式提取，1.bs 2.reGex
        try:
            mail = bs_second.find('div', class_='howtoapply').find('p').find('a')  
            print(mail)
            #mail1 = mail['href']    # 取href值，取出的是 mailto:sushigobutehr@gmail.com
            mail2 = mail.text        # 取出的是元素a的值：sushigobutehr@gmail.com
            print('mail extract - Done')
        except:        
            print('BS解析失败')
            try:
                emailRegex = re.compile(r'''(
                    [a-zA-Z0-9._%+-]+ # username
                    @ # @ symbol
                    [a-zA-Z0-9.-]+ # domain name
                    (\.[a-zA-Z]{2,4}) # dot-something
                    )''', re.VERBOSE)
                mail1  = emailRegex.search(str(bs_second))  
                mail2  = mail1.group()
            except:
                mail2 = 0
                print('re解析失败')
                pass
            pass

        # 职位名称
        postion = bs_second.find('span', property='title')
        m1 = postion.text.strip()          
        print('position - Done')

        # 职位网址
        website = url 
        print('url - Done')

        # 获取工作地点
        place0 = bs_second.find('span',class_='city')           
        place1 = place0.text.strip()                           
        print('place - Done')

        #获取工作内容描述
        JD = bs_second.find('div',property='skills')            
        JD1 =JD.text.strip()                                    # 整理数据
        print('JD - Done')

        # 获取薪水数据
        salary = bs_second.find('span', property='minValue')    
        m2 = salary['content']                                  
        print('salary - Done')

        # 获取空缺名额
        vac0 = bs_second.find('ul', class_='job-posting-brief') # 定位
        vacNumber = re.compile(r'(\d)( vacancy)')               # 定位
        vac1 = vacNumber.search(str(vac0))
        # 此环节易报错，原因未知
        try:
            vac2 =vac1.group(1)
        except:
            pass                           
        print('vacancy - Done')        
        
        # 获取职位有效期
        expiredDate = bs_second.find('p', property='validThrough').text  
        print('expired date - Done')

        # 存入列表
        row = [m1, website, Place1, JD1, m2, vac2, mail2, expiredDate]  
        
        # 写入数据
        sheet.append(row)   

        # 关闭浏览器
        driver.close()   

        # 减慢程序速度
        # time.sleep(1)                       

        # 保存文件
        wb.save('/Users/chang/Desktop/food postion.xlsx')   
        print('save - Done')
        # 确认完成
        #print('Position ' + str(i+1) + ' Done')
            
        print(url,work.qsize())  

searPage(position,place)

# 协程处理爬取数据
start = time.time()

url_list = []

for i in list1:
    t_url = 'https://www.jobbank.gc.ca/jobsearch/jobposting/' + str(i) + '?source=searchresults'   # 单个职位页面
    url_list.append(str(t_url))

work = Queue()

for url in url_list:
    work.put_nowait(url)                                    # 用put_nowait()函数可以把网址都放进队列里

tasks_list = []                                             # 创建空的任务列表

for x in range(2):                                          # 相当于创建了2个爬虫
    task = gevent.spawn(position_crawler)                   # 用gevent.spawn()函数创建执行crawler()函数的任务
    tasks_list.append(task)                                 # 往任务列表添加任务

gevent.joinall(tasks_list)                                  # 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。

end = time.time()

print(end-start)
