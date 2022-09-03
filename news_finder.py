from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cmath import nan
from re import search
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import pandas as pd
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap


class Ui_news_finder(object):
    df = pd.DataFrame(columns=['Title', 'Date', 'ArticleBody', 'Image'], index=['Prothomalo', 'bangladeshPost', 'DailyStar', 'BDNews'])
    df = df.astype({'ArticleBody': str})
    def setupUi(self, news_finder):
        news_finder.setObjectName("news_finder")
        news_finder.resize(1114, 829)
        news_finder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit1 = QtWidgets.QTextEdit(news_finder)
        self.textEdit1.setGeometry(QtCore.QRect(70, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit1.setFont(font)
        self.textEdit1.setObjectName("textEdit1")
        self.pushButton = QtWidgets.QPushButton(news_finder)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget1 = QtWidgets.QTableWidget(news_finder)
        self.tableWidget1.setGeometry(QtCore.QRect(70, 140, 531, 681))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.tableWidget1.setFont(font)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setRowCount(0)
        self.tableWidget1.setColumnWidth(0,200)
        self.tableWidget1.setColumnWidth(1,80)
        self.tableWidget1.setColumnWidth(2,150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        self.textEdit3 = QtWidgets.QTextEdit(news_finder)
        self.textEdit3.setGeometry(QtCore.QRect(610, 410, 471, 401))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.textEdit3.setFont(font)
        self.textEdit3.setObjectName("textEdit3")
        self.textEdit2 = QtWidgets.QTextEdit(news_finder)
        self.textEdit2.setGeometry(QtCore.QRect(610, 290, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")
        self.label = QtWidgets.QLabel(news_finder)
        self.label.setGeometry(QtCore.QRect(790, 130, 271, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Project/default-news.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(news_finder)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(news_finder)
        QtCore.QMetaObject.connectSlotsByName(news_finder)

        self.pushButton.clicked.connect(lambda: self.search())
        self.tableWidget1.cellClicked.connect(lambda: self.details())

    def retranslateUi(self, news_finder):
        _translate = QtCore.QCoreApplication.translate
        news_finder.setWindowTitle(_translate("news_finder", "Form"))
        self.textEdit1.setHtml(_translate("news_finder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("news_finder", "Search"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("news_finder", "Title"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("news_finder", "Date"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("news_finder", "Published at"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("news_finder", "Picture"))
        self.label_2.setText(_translate("news_finder", "NEWS FINDER"))

        #edited my myself
        self.textEdit1.setPlaceholderText("Type here to search")
        self.textEdit2.setPlaceholderText("Title")
        self.textEdit2.setReadOnly(True)
        self.textEdit3.setPlaceholderText("Full news") 
        self.textEdit3.setReadOnly(True)

   

    #functions

    def details(self):
        row = self.tableWidget1.currentRow()
        if row == 0:       
            self.textEdit2.clear()
            self.textEdit2.setText(self.df['Title']['Prothomalo'])
            self.textEdit3.clear()
            self.textEdit3.setText(self.df['ArticleBody']['Prothomalo'])
            image = self.set_pic(self.df['Image']['Prothomalo'])
            self.label.setPixmap(QPixmap(image))

        elif row == 1:
            self.textEdit2.clear()
            self.textEdit2.setText(self.df['Title']['bangladeshPost'])
            self.textEdit3.clear()
            self.textEdit3.setText(self.df['ArticleBody']['bangladeshPost'])
            image = self.set_pic(self.df['Image']['bangladeshPost'])
            self.label.setPixmap(QPixmap(image))

        elif row == 2:
            self.textEdit2.clear()
            self.textEdit2.setText(self.df['Title']['DailyStar'])
            self.textEdit3.clear()
            self.textEdit3.setText(self.df['ArticleBody']['DailyStar'])
            image = self.set_pic(self.df['Image']['DailyStar'])
            self.label.setPixmap(QPixmap(image))   

        elif row == 3:
            self.textEdit2.clear()
            self.textEdit2.setText(self.df['Title']['BDNews'])
            self.textEdit3.clear()
            self.textEdit3.setText(self.df['ArticleBody']['BDNews'])
            image = self.set_pic(self.df['Image']['BDNews'])
            self.label.setPixmap(QPixmap(image))     

    def add_item_tableWidget(self):
        self.tableWidget1.setRowCount(0)
        row=0
        self.tableWidget1.setRowCount(4)
        string = self.textEdit1.toPlainText()

        if(self.prothomalo(string)==False or self.bangladeshpost(string)==False or self.dailyStar(string)==False or self.bdnews24(string)==False):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning )
            msg.setText("Please reinput. No articles found")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.tableWidget1.setItem(row, 0, QtWidgets.QTableWidgetItem(self.df['Title']['Prothomalo']))
            self.tableWidget1.setItem(row, 1, QtWidgets.QTableWidgetItem(self.df['Date']['Prothomalo']))
            self.tableWidget1.setItem(row, 2, QtWidgets.QTableWidgetItem('Prothomalo'))
            imageLabel = QtWidgets.QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            image = self.set_pic(self.df['Image']['Prothomalo'])
            imageLabel.setPixmap(QPixmap(image))
            self.tableWidget1.setCellWidget(row,3,imageLabel)
            row = row + 1

            self.tableWidget1.setItem(row, 0, QtWidgets.QTableWidgetItem(self.df['Title']['bangladeshPost']))
            self.tableWidget1.setItem(row, 1, QtWidgets.QTableWidgetItem(self.df['Date']['bangladeshPost']))
            self.tableWidget1.setItem(row, 2, QtWidgets.QTableWidgetItem('Bangladesh Post'))
            imageLabel = QtWidgets.QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            image = self.set_pic(self.df['Image']['bangladeshPost'])
            imageLabel.setPixmap(QPixmap(image))
            self.tableWidget1.setCellWidget(row,3,imageLabel)
            row = row + 1

            self.tableWidget1.setItem(row, 0, QtWidgets.QTableWidgetItem(self.df['Title']['DailyStar']))
            self.tableWidget1.setItem(row, 1, QtWidgets.QTableWidgetItem(self.df['Date']['DailyStar']))
            self.tableWidget1.setItem(row, 2, QtWidgets.QTableWidgetItem('Daily Star'))
            imageLabel = QtWidgets.QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            image = self.set_pic(self.df['Image']['DailyStar'])
            imageLabel.setPixmap(QPixmap(image))
            self.tableWidget1.setCellWidget(row,3,imageLabel)
            row = row + 1

            self.tableWidget1.setItem(row, 0, QtWidgets.QTableWidgetItem(self.df['Title']['BDNews']))
            self.tableWidget1.setItem(row, 1, QtWidgets.QTableWidgetItem(self.df['Date']['BDNews']))
            self.tableWidget1.setItem(row, 2, QtWidgets.QTableWidgetItem('BDNews24'))
            imageLabel = QtWidgets.QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            image = self.set_pic(self.df['Image']['BDNews'])
            imageLabel.setPixmap(QPixmap(image))
            self.tableWidget1.setCellWidget(row,3,imageLabel)
            row = row + 1




    def set_pic(self, url_image):

        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        return image
        


    def search(self):
        if self.textEdit1.toPlainText()=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning )
            msg.setText("Please type something")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.add_item_tableWidget()
    
    def prothomalo(self, string):
        searchLink='https://en.prothomalo.com/search?q='+string
        driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
        driver.maximize_window()
        driver.get(searchLink)
        time.sleep(1)
        html_text = driver.page_source.encode('utf-8').strip()

        soup = BeautifulSoup(html_text, 'lxml')
        
        if(soup.find('span').text=='This page isn’t working'):
            return False
        else:
            more_info = soup.find('a', class_='newsHeadline-m__title-link__1puEG')
            self.df['Image']['Prothomalo']= soup.find('figure', class_='qt-figure').picture.img['src']
            driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
            driver.maximize_window()
            driver.get(more_info['href'])
            time.sleep(5)
            html_text = driver.page_source.encode('utf-8').strip()
            driver.quit()

            soup = BeautifulSoup(html_text, 'lxml')

            self.df['Title']['Prothomalo'] = soup.find('h1', class_='storytitleInfo-m__story-headline__30dXX').text
            upload_date_block = soup.find('div', class_ = 'storyPageMetaData-m__publish-time__19bdV storyPageMetaData-m__no-update__3AA06')
            self.df['Date']['Prothomalo'] =  upload_date_block.time.span.text
            discription_block = soup.find('div', class_='story-element story-element-text')
            discription_text = discription_block.find_all('p')

            for paragraphs in discription_text:
                if(self.df['ArticleBody']['Prothomalo'] == 'nan'):
                    self.df['ArticleBody']['Prothomalo'] = paragraphs.text
                else:
                    self.df['ArticleBody']['Prothomalo'] = self.df['ArticleBody']['Prothomalo']+'\n'+paragraphs.text
                

            
            return True
    

    def bangladeshpost(self, string):

        searchLink='https://bangladeshpost.net/search?query='+string
        driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
        driver.maximize_window()
        driver.get(searchLink)
        time.sleep(1)
        html_text = driver.page_source.encode('utf-8').strip()

        soup = BeautifulSoup(html_text, 'lxml')

        if(soup.find('div', class_ = 'pagination pagination-large').p.text=='''
                Page 1 of 1, showing 0 results out of 0 total            '''):
            print("Please reinput. No articles found")
            return False
        else:
            more_info = 'https://bangladeshpost.net/'+soup.find('a', class_='search-page-link')['href']
            driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
            driver.maximize_window()
            driver.get(more_info)
            time.sleep(5)
            html_text = driver.page_source.encode('utf-8').strip()
            driver.quit()

            soup = BeautifulSoup(html_text, 'lxml')

            self.df['Title']['bangladeshPost'] = soup.find('h1', class_='detail-post-title').text
            upload_date_block = soup.find_all('div', style = 'display: block;width:100%;')
            for need_date in upload_date_block:
                self.df['Date']['bangladeshPost'] =  need_date.text.replace(' ','')
                self.df['Date']['bangladeshPost'] = self.df['Date']['bangladeshPost'].lstrip()
            discription_block = soup.find('div', class_='post-details-content')
            discription_text = discription_block.find_all('p')

            for paragraphs in discription_text:
                if(self.df['ArticleBody']['bangladeshPost'] == 'nan'):
                    self.df['ArticleBody']['bangladeshPost'] = paragraphs.text
                else:
                    self.df['ArticleBody']['bangladeshPost'] = self.df['ArticleBody']['bangladeshPost']+'\n'+paragraphs.text
                
            self.df['Image']['bangladeshPost']= soup.find('img', class_='lazyloading img-responsive')['src']
            return True


    def dailyStar(self, string):
        ##Finding the link of the first article from the search
        driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
        searchLink = 'https://www.thedailystar.net/search?t='+string+'#gsc.tab=0&gsc.q='+string+'&gsc.sort=date'

        ##Code to load to the website including javascript on chrome webdriver
        driver.maximize_window()
        driver.get(searchLink)
        time.sleep(1)
        content = driver.page_source.encode('utf-8').strip() ##extracting html data from chrome webdriver

        soup = BeautifulSoup(content,"lxml")
        firstArticle = soup.find('div', class_='gsc-webResult gsc-result')

        ##Checking to see if article has been found or user needs to reinput
        if(firstArticle.find('div', class_ = "gs-snippet").text == "No Results"):
            return False
            
        else:
            link = (firstArticle.find('a', href=True))
            
            ##loading article page through chrome webdriver
            driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
            webLink = link['href']
            driver.maximize_window()
            driver.get(webLink)
            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            driver.quit()
            
            soup = BeautifulSoup(content,"lxml")
            article = soup.find('article', class_ = 'article-section pb-30 clearfix node node-news odd view-mode-full')
            
            
            self.df['Title']['DailyStar'] = article.find('div', class_ = 'mb-30 smb-20').text
            self.df['Title']['DailyStar'] = self.df['Title']['DailyStar'].lstrip()
            self.df['Date']['DailyStar'] = article.find('div', class_ = 'date text-10').text
            articleBody = article.find('div', class_ = 'section-content margin-lr pt-20 pb-20 clearfix')
            
            articleText = articleBody.find_all('p')
            
            for paragraphs in articleText:
                if(self.df['ArticleBody']['DailyStar'] == 'nan'):
                    self.df['ArticleBody']['DailyStar'] = paragraphs.text
                else:
                    self.df['ArticleBody']['DailyStar'] = self.df['ArticleBody']['DailyStar']+'\n'+paragraphs.text
                    
            imagebody = article.find("div", class_ = "section-media sm-float-none position-relative small-full-extended mb-30 margin-lr")
            imagelink = imagebody.find("img", class_ = "lazyloaded")
            self.df['Image']['DailyStar'] = imagelink["data-srcset"]

            return True
    
    def bdnews24(self, string):
        ##Finding the link of the first article from the search
        driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
        searchLink = 'https://bdnews24.com/search/simple.do;jsessionid=E5DB425DB956353E07B68911004815A3.C5-Pres1-Eng?destinationSectionId=13&publicationName=wf-escenic-times&sortString=publishdate&sortOrder=desc&sectionId=1&articleTypes=news&pageNumber=1&pageLength=20&searchString='+string

        ##Code to load to the website including javascript on chrome webdriver
        driver.maximize_window()
        driver.get(searchLink)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip() ##extracting html data from chrome webdriver

        soup = BeautifulSoup(content,"lxml")
        
        firstArticle = soup.find('div', class_="article first")
        articleparagraph = firstArticle.find('p', class_ = 'summary')
        aritclespan = articleparagraph.find('span', class_ = 'resultTitle')
        link = aritclespan.find('a', href = True)
        
        ##loading article page through chrome webdriver
        driver = webdriver.Chrome('G:/Spring 21-22/PROGRAMMING IN PYTHON/Python Code/Project/chromedriver.exe')
        webLink = link['href']
        driver.maximize_window()
        driver.get(webLink)
        time.sleep(5)
        content = driver.page_source.encode('utf-8').strip()
        driver.quit()
        
        soup = BeautifulSoup(content,"lxml")
        article = soup.find('div', id = 'main')
        
        self.df['Title']['BDNews'] = article.find('h1', class_ = 'print-only').text
        
        dates = article.find_all('span')
        self.df['Date']['BDNews'] = dates[2].text
        
        self.df['ArticleBody']['BDNews'] = article.find('h5', class_ = 'print-only').text.lstrip()
        articleBody = article.find('div', class_ = 'custombody print-only')
        articleText = articleBody.find_all('p')
        for paragraphs in articleText:
            self.df['ArticleBody']['BDNews'] = self.df['ArticleBody']['BDNews']+'\n'+paragraphs.text
            
        imagebody = article.find("div", class_ = "gallery-image-box print-only")
        imagelink = imagebody.find("img", src=True)
        self.df['Image']['BDNews'] = imagelink["src"]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    news_finder = QtWidgets.QWidget()
    ui = Ui_news_finder()
    ui.setupUi(news_finder)
    news_finder.show()
    sys.exit(app.exec_())
