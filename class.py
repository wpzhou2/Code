#爬汕大课程

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql

conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='course',port=3306,charset='utf8')
url='http://credit.stu.edu.cn/portal/stulogin.aspx'#url中指明定位到学分制系统登录页面
driver=webdriver.Chrome(r"D:\Program Files\software\chromedriver.exe")
driver.get(url)

name_input=driver.find_element_by_id('txtUserID')#找到用户名的框框
pass_input=driver.find_element_by_id('txtUserPwd')#找到输入密码的框框
login_button=driver.find_element_by_id('btnLogon')#找到登录按钮

name_input.clear()
name_input.send_keys("16wpzhou2")#填写用户名
time.sleep(0.1)
pass_input.clear()
pass_input.send_keys("Zwp123123")#填写密码
time.sleep(0.1)
login_button.click()#点击登录


def login(classID):
    cursor=conn.cursor()
    url1='http://credit.stu.edu.cn/Elective/DispkkbInfo.aspx?ClassID='+str(classID)
    driver.get(url1)
    html=driver.page_source.encode('utf-8').decode()

    soup=BeautifulSoup(html,'html.parser')
    if(soup.find(attrs={'id':'lbl_ClassRoom'}).string=="*"):
        return
    if(soup.find(attrs={'id':'lbl_Semester'}).string!="2018-2019学年春季学期"):
        return

    list1=soup.find_all(attrs={'class':'DGItemStyle'})
    list2=soup.find_all(attrs={'class':'DGAlternatingItemStyle'})

    classID=soup.find(attrs={'id':'lbl_ClassID'}).string.strip()
    semester=soup.find(attrs={'id':'lbl_Semester'}).string.strip()
    courseName=soup.find(attrs={'id':'lbl_CourseName'}).string.strip()
    courseTime=soup.find(attrs={'id':'lbl_Time'}).string.strip()
    number=soup.find(attrs={'id':'lbl_Number'}).string.strip()
    classRoom=soup.find(attrs={'id':'lbl_ClassRoom'}).string.strip()
    teacher=soup.find(attrs={'id':'lbl_Teacher'}).string.strip()

    print(classID)
    print(courseName)
    print(semester)

    for item in list1:
        s=str(item)
        soup1=BeautifulSoup(s,'html.parser')
        td_list=soup1.find_all(name='td')
        courseItem=[]
        flag1=0
        if(len(td_list)==7):
            flag1=1;

        for ti in td_list:
            courseItem.append(ti.string)

        if(flag1==1):
            cursor.execute("insert into courses1(classID,className,classTime,classNumber,semester,classRoom,"
                           "teacher,studentID,studentName,studentSex,major) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (str(classID),str(courseName),str(courseTime),str(number),str(semester),
                            str(classRoom),str(teacher),str(courseItem[1]),str(courseItem[2]),str(courseItem[3]),str(courseItem[4])))


    for item in list2:
        s=str(item)
        soup1=BeautifulSoup(s,'html.parser')
        td_list=soup1.find_all(name='td')
        courseItem=[]
        flag2=0
        if(len(td_list)==7):
            flag2=1
        for ti in td_list:
            courseItem.append(ti.string)
        if(flag2==1):
            cursor.execute("insert into courses1(classID,className,classTime,classNumber,semester,classRoom,"
                           "teacher,studentID,studentName,studentSex,major) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (str(classID), str(courseName), str(courseTime), str(number), str(semester),
                            str(classRoom), str(teacher), str(courseItem[1]), str(courseItem[2]), str(courseItem[3]),
                            str(courseItem[4])))


if __name__ =="__main__":
    for classID in range(107000,110000):
        login(classID)
        conn.commit()#数据库进行的操作都要提交
    conn.close()
