#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import MySQLdb
import cgi
import json

data = cgi.FieldStorage()

url = data.getvalue('url')

print "Welcome to Selenium Scrape"

class LinkedinScrape(object):
    

    class connect(object):
            
        def __init__(self,hostName,userName,password,dbName):
            db = MySQLdb.connect(hostName,userName,password,dbName)
            self.db = db
        
        def close(self):
            db = self.db
            db.close()
            
        def create_table(self, tableName, l = ['name','headline','location','industry', 'previous', 'education', 'recommendations', 'websites']):
            columnSet=[]
            for column in l:
                columnSet.append(column + ' varchar(50)')
            columnSet = ','.join(columnSet)
            sql = "create table %s (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, %s)" % (tableName,columnSet)
            db = self.db
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            print "Table '%s' was succesfully created" % (tableName)
            return l

        def insertScrapedValues(self, tableName):
            values = ','.join(stringData)
            print values
            sql = "Insert into %s values (Null, %s)" % (tableName, values)
            db = self.db
            cursor=db.cursor()
            cursor.execute(sql)
            db.commit()
                

    def linkedinCrawler(self,linkedinEmail, linkedinPassword, url):
            global stringData
            driver = webdriver.Firefox()
            driver.get('https://www.linkedin.com/uas/login')
            inputElement1 = driver.find_element_by_id("session_key-login")
            inputElement1.send_keys(linkedinEmail)
            inputElement2 = driver.find_element_by_id("session_password-login")
            inputElement2.send_keys(linkedinPassword)
            inputElement2.send_keys(Keys.ENTER)
            time.sleep(5)
            driver.get(url)
            data = []
            soup = BeautifulSoup(driver.page_source, 'lxml')
            name = soup.find("span",{'class': 'full-name'})
            data.append(name.text)
            headline = soup.find("p",{'class': 'title'})
            data.append(headline.text)
            location = soup.find("a",{'name': 'location'})
            data.append(location.text)
            industry = soup.find("a",{'name':'industry'})
            data.append(industry.text)
            previous = soup.find("tr",{'id': 'overview-summary-past'}).find("span",{'class': 'new-miniprofile-container'}).findAll("a")
            jobs=''
            for position in previous:
                jobs += position.text + ', '
            data.append(jobs)
            education = soup.find("tr",{'id': 'overview-summary-education'}).findAll("a",{'title': 'More deatils for this school'})
            schools = ''
            for ed in education:
                schools += ed.text + ', '
            data.append(schools)
            if soup.find("td").find_next("strong") == None:
                data.append('')
            else:
                recommendations = soup.find("td").find_next("strong")
                data.append(recommendations.text)
            if soup.find("tr", {'class' : 'websites'}) == None:
                data.append('')
            else:
                websites = soup.find("tr", {'class' : 'websites'}).findAll("a")
                sites=''
                for website in websites:
                    sites += website.text + ', '
                data.append(sites)
            stringData=[]
            for datum in data:
                stringData.append("'"+datum+"'")
            driver.close()
            print "Linkedin data Beautifully scraped\n\n"
            print "<html>"
            print "<body>"
            print "<text>{}</text>".format(json.dumps(stringData))
            print "</body></html>"

LinkedinScrape = LinkedinScrape()

LinkedinScrape.linkedinCrawler('***********','********',url)
