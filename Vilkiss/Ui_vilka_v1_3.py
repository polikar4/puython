import sys
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
from selenium.webdriver.firefox.service import Service 
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
import socket

Ip_server = '82.146.57.182'
NormalSizeWindow = False
NormalSizeText  = False
KeyAuthorization = "MaskXyiSosi"
Heatless = True        
url_hawk_start = "https://hawk.live/"
url_dotapicker = "https://dotapicker.com/herocounter?language=ru-ru#!/"
urt_defolt_hero = "https://hawk.live/images/unknown_hero.png"

'''  
                elem = self.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/main/div/div[2]/div[3]/div[1]/canvas')
                self.canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", elem)
                self.canvas_png = base64.b64decode(self.canvas_base64)
                ff = QtGui.QPixmap()
                 QtGui.QPixmap.loadFromData(ff,QtCore.QByteArray.fromBase64(base64.b64encode(driver_selenium.canvas_png)))
                self.BG.setPixmap(ff)
'''

class Server():

	def __init__(self):
		self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_sock.connect((Ip_server, 53220))

	
	def check_kode(self,key):

		self.client_sock.sendall(str.encode(key ,  encoding='utf-8'))
		while True:
			data = self.client_sock.recv(1024)
			if(len(data) != 0):
				return self.check_otvet(data)

	def check_otvet(self, key):
                key = key.decode("utf-8")
                print(key)
                if(key == "11111"):
                        return True
                return False
				


class Selenium_meme():
        
        def __init__(self):
                target= self.Creat_driver()
                target= self.Open_hawk()

        def Analis_pika(self):
                pick = self.Have_pick()
                urlMatch = self.driver.current_url
                self.driver.get(url_dotapicker + pick + '/S_0_matchups/S_1_advcharts/S_2_matchups')
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/select/option[1]"))).click()
                ui.RadSolo.setText(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[2]/td[3]').text)
                ui.RadTeam.setText(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[3]/td[3]').text)
                ui.DireSolo.setText(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[2]/td[2]').text)
                ui.DireTeam.setText(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[3]/td[2]').text)

                solo = int(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[2]/td[4]').text)
                if solo >= 0:
                        ui.SoloRes.setStyleSheet("color: rgb(0, 128, 0);")
                        ui.SoloRes.setText(str(solo))
                else:
                        ui.SoloRes.setStyleSheet("color: rgb(255, 0, 0);")
                        ui.SoloRes.setText(str(-solo))
                
                team = int(self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/table/tbody/tr[3]/td[4]').text)
                if team >= 0:
                        ui.TeamRes.setStyleSheet("color: rgb(0, 128, 0);")
                        ui.TeamRes.setText(str(team))
                else:
                        ui.TeamRes.setStyleSheet("color: rgb(255, 0, 0);")
                        ui.TeamRes.setText(str(-team))

                self.Png_pickgraf()
                
                self.driver.get(urlMatch)
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[5]/img")))

                return
             
        def Get_chet(driver):
                element = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[1]/div[2]/div[2]')
                return element.text


        def Have_money(self):
                money = 0
                if 0 != len(self.driver.find_elements(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[2]/div[1]/b')):
                        element = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[2]/div[1]/b')
                        money = int(element.text) 
                else:
                        element = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[2]/div[4]/b')
                        money = 0 - int(element.text) 
 

                if money > 0:
                        ui.MoneyCount.setStyleSheet("color: rgb(0, 128, 0);")
                        ui.MoneyCount.setText(str(money))
                else:
                        ui.MoneyCount.setStyleSheet("color: rgb(255, 0, 0);")
                        ui.MoneyCount.setText(str(-money))
    
 
        def Have_pick(self):
                b = ''
                for j in range(2):
                        for i in range(5):
                                element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[{}]/div[{}]/img'.format(str(j+1),str(i+1)))
                                b += ('T_' if j == 0 else 'E_')  + (element.get_attribute('title')) + '/'
                b = b.replace(' ','_').replace("'",'')
                return b  

        def GetTeamlogo(self):
                logo1 = requests.get(self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[1]/div[1]/div/img').get_attribute('src'))
                logo2 = requests.get(self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[1]/div[3]/div/img').get_attribute('src'))
                t1 = QtGui.QPixmap()
                t2 = QtGui.QPixmap()
                QtGui.QPixmap.loadFromData(t1,QtCore.QByteArray.fromBase64(base64.b64encode(logo1.content)))
                QtGui.QPixmap.loadFromData(t2,QtCore.QByteArray.fromBase64(base64.b64encode(logo2.content)))
                ui.Team1logo.setPixmap(t1)
                ui.Team2logo.setPixmap(t2)
                                
                
        def Otkir_math(self,monber_game,map_game): 
                element3 = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/a[{}]'.format(str(monber_game),str(map_game)))
                self.driver.get(element3.get_attribute('href'))
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div[1]/div[3]/div/img")))


        def ChampName(self):
                ui.ChampName.setText(self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div').text)
        
        def Kol_kart(self,chet):
                self.maps = 0

                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/a[{}]'.format(str(chet),str(self.maps + 1)))))

                while 0 != len(self.driver.find_elements(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/a[{}]'.format(str(chet),str(self.maps + 1)))):
                        self.maps += 1  
                
        def Spisok_igr(self):
                self.mass_igr = []
                chet = 1
                while 0 != len(self.driver.find_elements(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/div/div[1]/span'.format(str(chet)))):
                        element1 = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/div/div[1]/span'.format(str(chet)))
                        element2 = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/div[{}]/div/div[3]/span'.format(str(chet)))
                        chet += 1
                        self.mass_igr.append(element1.text + " vs " + element2.text)

                                
        def Png_graf(self):
                elem = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[3]/div[1]/canvas')
                canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", elem)
                canvas_png_graf_money = base64.b64decode(canvas_base64)
                ff = QtGui.QPixmap()
                QtGui.QPixmap.loadFromData(ff,QtCore.QByteArray.fromBase64(base64.b64encode(canvas_png_graf_money)))
                ui.GoldGraph.setPixmap(ff)

        def Png_kart(self):
                elem = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/div[3]/div[2]/canvas')
                canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", elem)
                canvas_png_kart = base64.b64decode(canvas_base64)
                ff = QtGui.QPixmap()
                QtGui.QPixmap.loadFromData(ff,QtCore.QByteArray.fromBase64(base64.b64encode(canvas_png_kart)))
                ui.map.setPixmap(ff)

        def Png_pickgraf(self):
                elem = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div[3]/div/div[1]/span/canvas')
                canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", elem)
                canvas_png_pickgraf = base64.b64decode(canvas_base64)
                ff = QtGui.QPixmap()
                QtGui.QPixmap.loadFromData(ff,QtCore.QByteArray.fromBase64(base64.b64encode(canvas_png_pickgraf)))
                ui.PowerGraph.setPixmap(ff)

        def TeamNames(self):
                ui.Team1Name.setText(self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div[1]/span').text)
                ui.Team2Name.setText(self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div[3]/span').text)

        def Open_hawk(self):
                self.driver.get(url_hawk_start)
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[1]/header/div[1]/nav/ul/li[2]/a"))).click()
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/label[2]"))).click()
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located
                        ((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/button/span[2]/span"))).click()
                
        def swapHeroes(self):
                mass_picters = [[ui.r1,ui.r2,ui.r3,ui.r4,ui.r5],[ui.d1,ui.d2,ui.d3,ui.d4,ui.d5]]
                for j in range(2):
                        for i in range(5):
                                element = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[{}]/div[{}]/img".format(str(j+1),str(i+1)))
                                p = element.get_attribute('title')
                                picth = mass_picters[j][i]
                                picth.setPixmap(QtGui.QPixmap("source\\heroes\\"+ p + ".png"))


        def Creat_driver(self):
                self.options = Options()
                if Heatless:
                        self.options.headless = True
                        self.options.add_argument('--disable-gpu')
                serv = Service("source\\geckodriver.exe")
                self.driver = webdriver.Firefox(service=serv, options=self.options)
                
                



class Procces():

        def __init__(self):
                self.UpDate = False
                self.LogCheck = False
                self.GetPick = False
                self.NomberMath = 0
                self.NomberMap = 0

                self.driver_selenium = Selenium_meme()
                exem = Example()
                serv = Server()

                while serv.check_kode(exem.showDialog()):
                        break

                Thread(target= self.Nada()).start()
                Thread(target= self.AutoUpDate).start()


        def Nada(self):
                self.Refresh()
                self.Click_button()

        def Click_button(self):
                ui.reButton.clicked.connect(lambda: Thread(target=process.Refresh).start())
                ui.scButton.clicked.connect(lambda: Thread(target=process.Scan).start())
                ui.calcButton.clicked.connect(lambda: Thread(target=process.Calc).start())
                ui.clearButton.clicked.connect(lambda: Thread(target=process.Clear).start())
                ui.gayButton.clicked.connect(lambda: Thread(target=process.Gay).start())
                

        def print_kef(self,kef1,stavka1,koef):
                kef2 = round(stavka1 / ((kef1-1)*stavka1 * koef) + 1.005,2)

                str_line = "{:4.4}|".format(str(kef2)) 
                stavka2 = round((kef1-1)*stavka1 * koef)
                profit1 = round((kef1-1)*stavka1 - stavka2)
                profit2 = stavka2 * (kef2 - 1) - stavka1
                procent = (profit1 + profit2) / (stavka1 + stavka2) * 100
        
                str_line += '{:6.6}|{:7.7}|{:7.7}|{:5.5}'.format(str(stavka2), str(profit1), str(profit2), str(procent)) + "|||"
                kef2 = round(stavka1 / ((kef1-1)*stavka1 * koef) + 1.005,2)
                stavka2 = (stavka1 * (kef1 - 1) + stavka1) / kef2
                profit1 = round((kef1-1)*stavka1 - stavka2)
                profit2 = stavka2 * (kef2 - 1) - stavka1    
                procent = (profit1 + profit2) / (stavka1 + stavka2)* 100
        
                str_line += '{:6.6}|{:7.7}|{:7.7}|{:5.5}'.format(str(stavka2), str(profit1), str(profit2), str(procent)) + "|||"
                kef2 = round(stavka1 / ((kef1-1)*stavka1 * koef) + 1.005,2)
                stavka2 = round((kef1-1)*stavka1)
                profit1 = round((kef1-1)*stavka1 - stavka2)
                profit2 = stavka2 * (kef2 - 1) - stavka1   
                procent = (profit1 + profit2) / (stavka1 + stavka2)* 100
        
                str_line += '{:6.6}|{:7.7}|{:7.7}|{:5.5}'.format(str(stavka2), str(profit1), str(profit2), str(procent)) + "|||"
                return str_line + "\n"

        def Calc(self):
                print("calc")
                kef = float(ui.kfInput.text().replace(",", "."))
                stavka = ui.monInput.text()
                if kef <= 1:
                        return
                if len(stavka) == 0:
                        return
                stroka = self.print_kef(kef,int(stavka),0.95)
                stroka += self.print_kef(kef,int(stavka),0.80)
                stroka += self.print_kef(kef,int(stavka),0.85)
                ui.kfOutput.setText("    |Профит первой               |||Равный профит               |||Профит второй\n" + "Кеф |"
                                        + "Ставка|Профит1|Профит2|  %  |||"*3 + "\n" + stroka)
        
        
        def Refresh(self):
                ui.defaultOp()
                if str(self.driver_selenium.driver.current_url) != url_hawk_start:
                        self.driver_selenium.Open_hawk()
                ui.GameSelect.clear()
                ui.GameSelect.addItem("Select Game")
                ui.MapSelect.clear()
                ui.MapSelect.addItem("Select Map")
                self.driver_selenium.Spisok_igr()
                for i in self.driver_selenium.mass_igr:
                        ui.GameSelect.addItem(i)
                return

        def AutoUpDate(self):
                while True:
                        if self.UpDate:
                                self.driver_selenium.Have_money()
                                self.driver_selenium.Png_graf()
                                self.driver_selenium.Png_kart()
                                
                                if self.LogCheck:
                                        self.driver_selenium.ChampName()
                                        self.driver_selenium.GetTeamlogo()
                                        self.driver_selenium.TeamNames()
                                        self.LogCheck = False
                                
                                element = self.driver_selenium.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/img")
                                if self.GetPick and str(element.get_attribute("src"))  != urt_defolt_hero:
                                        self.driver_selenium.swapHeroes()
                                        self.driver_selenium.Analis_pika()
                                        self.GetPick = False
                                 
                        time.sleep(0.5)

        def Scan(self):
                if ui.GameSelect.currentIndex() == 0:
                        self.UpDate = False
                
                elif ui.GameSelect.currentIndex() != self.NomberMath:
                        self.UpDate = False
                        if(str(self.driver_selenium.driver.current_url) != url_hawk_start):
                                self.driver_selenium.Open_hawk()
                        self.driver_selenium.Kol_kart(ui.GameSelect.currentIndex())
                        ui.MapSelect.clear() 
                        ui.MapSelect.addItem("Select Map")
                        self.NomberMath = ui.GameSelect.currentIndex()
                        for i in range(self.driver_selenium.maps):
                                ui.MapSelect.addItem('Map ' + str(i+1))
                        self.GetPick = True
                        self.LogCheck = True
                        self.NomberMap = 0

                elif ui.MapSelect.currentIndex() != self.NomberMap:
                        if ui.MapSelect.currentIndex != 0:
                                self.UpDate = False
                                if(str(self.driver_selenium.driver.current_url) != url_hawk_start):
                                        self.driver_selenium.Open_hawk()
                                self.driver_selenium.Otkir_math(ui.GameSelect.currentIndex(),ui.MapSelect.currentIndex())
                                self.NomberMap = ui.MapSelect.currentIndex()
                                self.UpDate = True
                                self.GetPick = True
                                self.LogCheck = True

                        
                                               
                        
                return

        def Clear(self):
                ui.kfOutput.setText("")
                ui.kfInput.setValue(0)
                ui.monInput.setText("0")  
                return

        def Gay(self):
                ui.sound.stop()
                ui.sound.play()
                return



class Example(QWidget):


        first_get = True
        def showDialog(self):
                text, ok = QInputDialog.getText(self, 'Input Dialog',
                "Enter key:" if self.first_get else "Invalid:")
                self.first_get = False
                return text






class Ui_Prog(object):
    def setupUi(self, Prog):
        Prog.setObjectName("Prog")
        Prog.setWindowTitle("Vilkiss")
        Prog.setWindowModality(QtCore.Qt.NonModal)
        Prog.resize(1000, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Prog.sizePolicy().hasHeightForWidth())
        Prog.setSizePolicy(sizePolicy)
        Prog.setMinimumSize(QtCore.QSize(1000, 650))
        Prog.setMaximumSize(QtCore.QSize(1000, 650))
        Prog.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        Prog.setFont(font)
        Prog.setFocusPolicy(QtCore.Qt.NoFocus)
        Prog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Prog.setAcceptDrops(False)
        Prog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Prog.setAutoFillBackground(False)
        Prog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(Prog)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.BG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BG.setPixmap(QtGui.QPixmap("source\\bG.jpg"))
        self.BG.setObjectName("BG")
        self.kfInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.kfInput.setGeometry(QtCore.QRect(10, 500, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.kfInput.setFont(font)
        self.kfInput.setStyleSheet("background-color: rgb(71, 71, 71);" "color: rgb(85, 255, 0);" "selection-color: rgb(71, 71, 71);" "selection-background-color: rgb(85, 255, 255);")
        self.kfInput.setWrapping(False)
        self.kfInput.setFrame(False)
        self.kfInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kfInput.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.kfInput.setAccelerated(False)
        self.kfInput.setDecimals(2)
        self.kfInput.setMaximum(20.0)
        self.kfInput.setMinimum(1.01)
        self.kfInput.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.kfInput.setObjectName("kfInput")
        self.monInput = QtWidgets.QLineEdit(self.centralwidget)
        self.monInput.setGeometry(QtCore.QRect(70, 500, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.monInput.setFont(font)
        self.monInput.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(85, 255, 0);" "border-color: rgb(71, 71, 71);")
        self.monInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.monInput.setFrame(False)
        self.monInput.setAlignment(QtCore.Qt.AlignCenter)
        self.monInput.setObjectName("monInput")
        self.GameSelect = QtWidgets.QComboBox(self.centralwidget)
        self.GameSelect.setGeometry(QtCore.QRect(10, 10, 210, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.GameSelect.setFont(font)
        self.GameSelect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameSelect.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.GameSelect.setObjectName("GameSelect")
        self.GameSelect.addItem("")
        self.MapSelect = QtWidgets.QComboBox(self.centralwidget)
        self.MapSelect.setGeometry(QtCore.QRect(10, 50, 101, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.MapSelect.setFont(font)
        self.MapSelect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MapSelect.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.MapSelect.setObjectName("MapSelect")
        self.MapSelect.addItem("")
        self.reButton = QtWidgets.QPushButton(self.centralwidget)
        self.reButton.setGeometry(QtCore.QRect(10, 90, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.reButton.setFont(font)
        self.reButton.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);")
        self.reButton.setObjectName("reButton")
        self.scButton = QtWidgets.QPushButton(self.centralwidget)
        self.scButton.setGeometry(QtCore.QRect(80, 90, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.scButton.setFont(font)
        self.scButton.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);")
        self.scButton.setObjectName("scButton")
        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(10, 530, 50, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.calcButton.setFont(font)
        self.calcButton.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(85, 255, 0);")
        self.calcButton.setObjectName("calcButton")
        self.kfOutput = QtWidgets.QLabel(self.centralwidget)
        self.kfOutput.setGeometry(QtCore.QRect(130, 450, 861, 191))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setKerning(True)
        
        self.kfOutput.setFont(font)
        self.kfOutput.setStyleSheet("color: rgb(255, 255, 255);")
        self.kfOutput.setFrameShape(QtWidgets.QFrame.Panel)
        self.kfOutput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kfOutput.setLineWidth(1)
        self.kfOutput.setTextFormat(QtCore.Qt.AutoText)
        self.kfOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.kfOutput.setObjectName("kfOutput")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(70, 530, 50, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);")
        self.clearButton.setObjectName("clearButton")
        self.Radiant = QtWidgets.QLabel(self.centralwidget)
        self.Radiant.setGeometry(QtCore.QRect(10, 130, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Radiant.setFont(font)
        self.Radiant.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Radiant.setStyleSheet("color: rgb(62, 185, 0);")
        self.Radiant.setAlignment(QtCore.Qt.AlignCenter)
        self.Radiant.setObjectName("Radiant")
        self.Dire = QtWidgets.QLabel(self.centralwidget)
        self.Dire.setGeometry(QtCore.QRect(130, 130, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Dire.setFont(font)
        self.Dire.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Dire.setStyleSheet("color: rgb(170, 0, 0);")
        self.Dire.setAlignment(QtCore.Qt.AlignCenter)
        self.Dire.setObjectName("Dire")
        self.r1 = QtWidgets.QLabel(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(20, 170, 70, 40))
        self.r1.setStyleSheet("color: rgb(255, 255, 255);")
        self.r1.setFrameShape(QtWidgets.QFrame.Box)
        
        self.r1.setScaledContents(True)
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QLabel(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(20, 220, 70, 40))
        self.r2.setStyleSheet("color: rgb(255, 255, 255);")
        self.r2.setFrameShape(QtWidgets.QFrame.Box)
       
        self.r2.setScaledContents(True)
        self.r2.setObjectName("r2")
        self.r3 = QtWidgets.QLabel(self.centralwidget)
        self.r3.setGeometry(QtCore.QRect(20, 270, 70, 40))
        self.r3.setStyleSheet("color: rgb(255, 255, 255);")
        self.r3.setFrameShape(QtWidgets.QFrame.Box)
      
        self.r3.setScaledContents(True)
        self.r3.setObjectName("r3")
        self.r4 = QtWidgets.QLabel(self.centralwidget)
        self.r4.setGeometry(QtCore.QRect(20, 320, 70, 40))
        self.r4.setStyleSheet("color: rgb(255, 255, 255);")
        self.r4.setFrameShape(QtWidgets.QFrame.Box)
        
        self.r4.setScaledContents(True)
        self.r4.setObjectName("r4")
        self.r5 = QtWidgets.QLabel(self.centralwidget)
        self.r5.setGeometry(QtCore.QRect(20, 370, 70, 40))
        self.r5.setStyleSheet("color: rgb(255, 255, 255);")
        self.r5.setFrameShape(QtWidgets.QFrame.Box)
       
        self.r5.setScaledContents(True)
        self.r5.setObjectName("r5")
        self.d4 = QtWidgets.QLabel(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(140, 320, 70, 40))
        self.d4.setStyleSheet("color: rgb(255, 255, 255);")
        self.d4.setFrameShape(QtWidgets.QFrame.Box)
        
        self.d4.setScaledContents(True)
        self.d4.setObjectName("d4")
        self.d5 = QtWidgets.QLabel(self.centralwidget)
        self.d5.setGeometry(QtCore.QRect(140, 370, 70, 40))
        self.d5.setStyleSheet("color: rgb(255, 255, 255);")
        self.d5.setFrameShape(QtWidgets.QFrame.Box)
       
        self.d5.setScaledContents(True)
        self.d5.setObjectName("d5")
        self.d3 = QtWidgets.QLabel(self.centralwidget)
        self.d3.setGeometry(QtCore.QRect(140, 270, 70, 40))
        self.d3.setStyleSheet("color: rgb(255, 255, 255);")
        self.d3.setFrameShape(QtWidgets.QFrame.Box)
        
        self.d3.setScaledContents(True)
        self.d3.setObjectName("d3")
        self.d1 = QtWidgets.QLabel(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(140, 170, 70, 40))
        self.d1.setStyleSheet("color: rgb(255, 255, 255);")
        self.d1.setFrameShape(QtWidgets.QFrame.Box)
        
        self.d1.setScaledContents(True)
        self.d1.setObjectName("d1")
        self.d2 = QtWidgets.QLabel(self.centralwidget)
        self.d2.setGeometry(QtCore.QRect(140, 220, 70, 40))
        self.d2.setStyleSheet("color: rgb(255, 255, 255);")
        self.d2.setFrameShape(QtWidgets.QFrame.Box)
       
        self.d2.setScaledContents(True)
        self.d2.setObjectName("d2")
        self.gayButton = QtWidgets.QPushButton(self.centralwidget)
        self.gayButton.setGeometry(QtCore.QRect(10, 610, 30, 30))
        self.gayButton.setStyleSheet("background-color: rgb(71, 71, 71);""color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.gayButton.setObjectName("gayButton")
        self.ChampName = QtWidgets.QLabel(self.centralwidget)
        self.ChampName.setGeometry(QtCore.QRect(230, 10, 210, 20))
        self.ChampName.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.ChampName.setAlignment(QtCore.Qt.AlignCenter)
        self.ChampName.setObjectName("ChampName")
        self.Team1logo = QtWidgets.QLabel(self.centralwidget)
        self.Team1logo.setGeometry(QtCore.QRect(240, 50, 70, 70))
        self.Team1logo.setStyleSheet("color: rgb(255, 255, 255);")
        self.Team1logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        self.Team1logo.setScaledContents(True)
        self.Team1logo.setObjectName("Team1logo")
        self.Team2logo = QtWidgets.QLabel(self.centralwidget)
        self.Team2logo.setGeometry(QtCore.QRect(350, 50, 70, 70))
        self.Team2logo.setStyleSheet("color: rgb(255, 255, 255);")
        self.Team2logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        self.Team2logo.setScaledContents(True)
        self.Team2logo.setObjectName("Team2logo")
        self.vs = QtWidgets.QLabel(self.centralwidget)
        self.vs.setGeometry(QtCore.QRect(318, 80, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        self.vs.setFont(font)
        self.vs.setStyleSheet("color: rgb(255, 255, 255);")
        self.vs.setObjectName("vs")
        self.Team1Name = QtWidgets.QLabel(self.centralwidget)
        self.Team1Name.setGeometry(QtCore.QRect(240, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.Team1Name.setFont(font)
        self.Team1Name.setStyleSheet("color: rgb(255, 255, 255);")
        self.Team1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Team1Name.setObjectName("Team1Name")
        self.Team2Name = QtWidgets.QLabel(self.centralwidget)
        self.Team2Name.setGeometry(QtCore.QRect(350, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.Team2Name.setFont(font)
        self.Team2Name.setStyleSheet("color: rgb(255, 255, 255);")
        self.Team2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Team2Name.setObjectName("Team2Name")
        self.RadSolo = QtWidgets.QLabel(self.centralwidget)
        self.RadSolo.setGeometry(QtCore.QRect(280, 220, 31, 20))
        self.RadSolo.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.RadSolo.setFrameShape(QtWidgets.QFrame.Box)
        self.RadSolo.setAlignment(QtCore.Qt.AlignCenter)
        self.RadSolo.setObjectName("RadSolo")
        self.RadTeam = QtWidgets.QLabel(self.centralwidget)
        self.RadTeam.setGeometry(QtCore.QRect(280, 250, 31, 20))
        self.RadTeam.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.RadTeam.setFrameShape(QtWidgets.QFrame.Box)
        self.RadTeam.setAlignment(QtCore.Qt.AlignCenter)
        self.RadTeam.setObjectName("RadTeam")
        self.DireTeam = QtWidgets.QLabel(self.centralwidget)
        self.DireTeam.setGeometry(QtCore.QRect(320, 250, 31, 20))
        self.DireTeam.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.DireTeam.setFrameShape(QtWidgets.QFrame.Box)
        self.DireTeam.setAlignment(QtCore.Qt.AlignCenter)
        self.DireTeam.setObjectName("DireTeam")
        self.DireSolo = QtWidgets.QLabel(self.centralwidget)
        self.DireSolo.setGeometry(QtCore.QRect(320, 220, 31, 20))
        self.DireSolo.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.DireSolo.setFrameShape(QtWidgets.QFrame.Box)
        self.DireSolo.setAlignment(QtCore.Qt.AlignCenter)
        self.DireSolo.setObjectName("DireSolo")
        self.SoloRes = QtWidgets.QLabel(self.centralwidget)
        self.SoloRes.setGeometry(QtCore.QRect(360, 220, 31, 20))
        self.SoloRes.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.SoloRes.setFrameShape(QtWidgets.QFrame.Box)
        self.SoloRes.setAlignment(QtCore.Qt.AlignCenter)
        self.SoloRes.setObjectName("SoloRes")
        self.TeamRes = QtWidgets.QLabel(self.centralwidget)
        self.TeamRes.setGeometry(QtCore.QRect(360, 250, 31, 20))
        
        self.TeamRes.setFrameShape(QtWidgets.QFrame.Box)
        self.TeamRes.setAlignment(QtCore.Qt.AlignCenter)
        self.TeamRes.setObjectName("TeamRes")
        self.RoudRadiant = QtWidgets.QLabel(self.centralwidget)
        self.RoudRadiant.setGeometry(QtCore.QRect(290, 200, 10, 10))
        self.RoudRadiant.setPixmap(QtGui.QPixmap("source\\Radiant.png"))
        self.RoudRadiant.setScaledContents(True)
        self.RoudRadiant.setObjectName("RoudRadiant")
        self.RoundDire = QtWidgets.QLabel(self.centralwidget)
        self.RoundDire.setGeometry(QtCore.QRect(330, 200, 10, 10))
        self.RoundDire.setPixmap(QtGui.QPixmap("source\\Dire.png"))
        self.RoundDire.setScaledContents(True)
        self.RoundDire.setObjectName("RoundDire")
        self.solostat = QtWidgets.QLabel(self.centralwidget)
        self.solostat.setGeometry(QtCore.QRect(250, 220, 20, 20))
        self.solostat.setPixmap(QtGui.QPixmap("source\\solostat.png"))
        self.solostat.setScaledContents(True)
        self.solostat.setObjectName("solostat")
        self.teamstat = QtWidgets.QLabel(self.centralwidget)
        self.teamstat.setGeometry(QtCore.QRect(250, 250, 20, 20))
        self.teamstat.setPixmap(QtGui.QPixmap("source\\teamstat.png"))
        self.teamstat.setScaledContents(True)
        self.teamstat.setObjectName("teamstat")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(820, 30, 150, 150))
        self.map.setStyleSheet("color: rgb(255, 255, 255);")
        self.map.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        self.map.setScaledContents(True)
        self.map.setObjectName("map")
        self.GoldGraph = QtWidgets.QLabel(self.centralwidget)
        self.xx = 500
        self.yy = int(self.xx/(518/256))
        self.GoldGraph.setGeometry(QtCore.QRect(480, 180, self.xx, self.yy))
        self.GoldGraph.setStyleSheet("color: rgb(255, 255, 255);")
        self.GoldGraph.setFrameShape(QtWidgets.QFrame.NoFrame)
     
        self.GoldGraph.setScaledContents(True)
        self.GoldGraph.setObjectName("GoldGraph")
        self.PowerGraph = QtWidgets.QLabel(self.centralwidget)
        self.PowerGraph.setGeometry(QtCore.QRect(250, 300, 200, 150))
        self.PowerGraph.setStyleSheet("color: rgb(255, 255, 255);")
        self.PowerGraph.setFrameShape(QtWidgets.QFrame.NoFrame)
        
        self.PowerGraph.setScaledContents(True)
        self.PowerGraph.setObjectName("PowerGraph")
        self.moneyGold = QtWidgets.QLabel(self.centralwidget)
        self.moneyGold.setGeometry(QtCore.QRect(550, 20, 30, 30))
        self.moneyGold.setStyleSheet("color: rgb(255, 255, 255);")
        self.moneyGold.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.moneyGold.setPixmap(QtGui.QPixmap("source\\money.png"))
        self.moneyGold.setScaledContents(True)
        self.moneyGold.setObjectName("moneyGold")
        self.MoneyCount = QtWidgets.QLabel(self.centralwidget)
        self.MoneyCount.setGeometry(QtCore.QRect(590, 20, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.MoneyCount.setFont(font)
        self.MoneyCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MoneyCount.setStyleSheet("color: rgb(62, 185, 0);")
        self.MoneyCount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MoneyCount.setObjectName("MoneyCount")
        self.deltaGold = QtWidgets.QLabel(self.centralwidget)
        self.deltaGold.setGeometry(QtCore.QRect(550, 60, 30, 30))
        self.deltaGold.setStyleSheet("color: rgb(255, 255, 255);")
        self.deltaGold.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.deltaGold.setPixmap(QtGui.QPixmap("source\\deltamoney.png"))
        self.deltaGold.setScaledContents(True)
        self.deltaGold.setObjectName("deltaGold")
        self.MoneyCount_2 = QtWidgets.QLabel(self.centralwidget)
        self.MoneyCount_2.setGeometry(QtCore.QRect(590, 60, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.MoneyCount_2.setFont(font)
        self.MoneyCount_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MoneyCount_2.setStyleSheet("color: rgb(62, 185, 0);")
        self.MoneyCount_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MoneyCount_2.setObjectName("MoneyCount_2")
        Prog.setCentralWidget(self.centralwidget)
        
        self.sound = QMediaPlayer()
        self.sound.setMedia(QMediaContent(QUrl.fromLocalFile("source\\gay.mp3")))
        self.sound.setVolume(5)

        self.reButton.setText("Refresh")
        self.scButton.setText("Scan")
        self.calcButton.setText("Calc")
 
        self.clearButton.setText("Clear")
        self.Radiant.setText("Radiant")
        self.Dire.setText("Dire")
        self.gayButton.setText("Gay")
        self.vs.setText("VS") 
        QtCore.QMetaObject.connectSlotsByName(Prog)
        self.defaultOp()

    def defaultOp(self):
        self.Team2logo.setPixmap(QtGui.QPixmap("source\\TeamUnknown.jpg"))
        self.Team1logo.setPixmap(QtGui.QPixmap("source\\TeamUnknown.jpg"))
        self.map.setPixmap(QtGui.QPixmap("source\\map.png"))
        self.GoldGraph.setPixmap(QtGui.QPixmap("source\\GoldGraph.png"))
        self.PowerGraph.setPixmap(QtGui.QPixmap("source\\PowerGraph.png"))
        self.Team1Name.setText("Team1")
        self.Team2Name.setText("Team2")
        self.MoneyCount.setText("")
        self.MoneyCount_2.setText("")
        self.r1.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.r2.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.r3.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.r4.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.r5.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.d1.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.d2.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.d3.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.d4.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.d5.setPixmap(QtGui.QPixmap("source\\kr3rAKn96RE.jpg"))
        self.ChampName.setText("")
        self.DireSolo.setText("")
        self.DireTeam.setText("")
        self.RadSolo.setText("")
        self.RadTeam.setText("")
        self.SoloRes.setText("")
        self.TeamRes.setText("")
        self.TeamRes.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
        self.SoloRes.setStyleSheet("background-color: rgb(71, 71, 71);""color: rgb(255, 255, 255);""border-color: rgb(255, 255, 255);")
    
    

        
                

    
        

if __name__ == "__main__":
        #windows size for high monitor 
        if NormalSizeWindow:
                QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        if NormalSizeText:
                QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)    


      
        
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        
        ui = Ui_Prog()
        ui.setupUi(MainWindow)
        MainWindow.show()
        process = Procces()
        
        sys.exit(app.exec_())
        
        
