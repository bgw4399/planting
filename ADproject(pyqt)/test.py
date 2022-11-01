import sys
import time
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from pymongo import MongoClient
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet, QtStyleTools
from plyer import notification
import paho.mqtt.client as mqtt
import json

client2 = MongoClient("mongodb+srv://overhyeon:ghfkd02dl.@cluster0.df2ugfu.mongodb.net/?retryWrites=true&w=majority")
db = client2["test"] # test라는 이름의 데이터베이스에 접속


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))

# 새로운 클라이언트 생성형으로
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
# address : localhost, port: 1883 에 연결
client.connect('localhost', 1883)
client.loop_start()
# common topic 으로 메세지 발행

client.loop_stop()
# 연결 종료
client.disconnect()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 554)
        
        self.now_tmp = 27
        self.now_hum = 45
        self.now_soilhum = 2

        self.isAuto = True

        self.tmp = QLabel(str(self.now_tmp),MainWindow)
        self.hum = QLabel(str(self.now_hum), MainWindow)
        self.soilhum = QLabel(str(self.now_soilhum), MainWindow)

        self.tmp.setText(str(self.now_tmp))
        self.hum.setText(str(self.now_hum))
        self.soilhum.setText(str(self.now_soilhum))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 280, 31, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        

        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 280, 31, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 340, 31, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(260, 340, 31, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(440, 400, 31, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(260, 400, 31, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 280, 51, 16))

        self.tmp = QtWidgets.QLabel(self.centralwidget)
        self.tmp.setGeometry(QtCore.QRect(360, 300, 51, 16 ))

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 340, 51, 16))
        self.label_2.setObjectName("label_2")
        
        self.hum = QtWidgets.QLabel(self.centralwidget)
        self.hum.setGeometry(QtCore.QRect(360, 360, 51, 16))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 400, 91, 16))
        self.label_3.setObjectName("label_3")

        self.soilhum = QtWidgets.QLabel(self.centralwidget)
        self.soilhum.setGeometry(QtCore.QRect(360, 420, 51, 16))

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 230, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 50, 171, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(170, 50, 150, 150))
        self.horizontalLayoutWidget_3.setMaximumSize(QtCore.QSize(150, 150))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./assignment/withered.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        self.timer = QTimer(MainWindow)
        self.timer.start(100000)
        self.timer.timeout.connect(self.dynamic_sensor)
        self.timer.timeout.connect(self.Auto)

        self.pushButton.clicked.connect(self.button_tmp_plus)
        self.pushButton_2.clicked.connect(self.button_tmp_minus)
        self.pushButton_3.clicked.connect(self.button_hum_minus)
        self.pushButton_4.clicked.connect(self.button_hum_plus) 
        self.pushButton_5.clicked.connect(self.button_solidHum_minus)
        self.pushButton_6.clicked.connect(self.button_solidHum_plus)
        self.pushButton_7.clicked.connect(self.button_mode_clicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label_4.setPixmap(QtGui.QPixmap("./withered.png"))
        apply_stylesheet(app, theme='dark_lightgreen.xml')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "식물 실시간 상태 확인"))
        self.tmp.setText(_translate("MainWindow", str(self.now_tmp)))
        self.soilhum.setText(_translate("MainWindow", str(self.now_soilhum)))
        self.hum.setText(_translate("MainWindow", str(self.now_hum)))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        #온도
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        #습도
        self.pushButton_5.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "+"))
        #토양 습도
        self.label.setText(_translate("MainWindow", "목표 온도"))
        self.label_2.setText(_translate("MainWindow", "목표 습도"))
        self.label_3.setText(_translate("MainWindow", "목표 토양 습도"))
        self.pushButton_7.setText(_translate("MainWindow", "상태: 자동"))
        self.label_5.setText(_translate("MainWindow", '이름:\n\n'
        '적정 습도: \n\n'
        '적정 온도: \n\n'
        '적정 토양 습도: '))

    def button_tmp_plus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_tmp += 1
        self.tmp.setText(str(self.now_tmp))
        client.publish('common', json.dumps({"1"}), 1)
    def button_tmp_minus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_tmp -= 1
        self.tmp.setText(str(self.now_tmp))
        client.publish('common', json.dumps({"2"}), 2)
      
    def button_solidHum_plus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_soilhum += 1
        self.soilhum.setText(str(self.now_soilhum))
        client.publish('common', json.dumps({"3"}), 3)

    def button_solidHum_minus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_soilhum -= 1
        self.soilhum.setText(str(self.now_soilhum))
        client.publish('common', json.dumps({"4"}), 4)
      
    def button_hum_plus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_hum += 1
        self.hum.setText(str(self.now_hum))
        client.publish('common', json.dumps({"5"}), 5)

    def button_hum_minus(self):
      if self.isAuto:
        notification.notify(
            title='Error',
            message='자동모드에선 실행할 수 없습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        self.now_hum -= 1
        self.hum.setText(str(self.now_hum))
        client.publish('common', json.dumps({"6"}), 6)
      
    def button_mode_clicked(self):
      if self.isAuto:
        # change auto -> manual
        self.isAuto = False
        self.pushButton_7.setText("상태: 수동")

        notification.notify(
            title='Manual Mode',
            message='수동으로 변경되었습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  #'C:\\icon_32x32.ico'
        )
      else:
        # change manual -> auto
        self.isAuto = True
        self.pushButton_7.setText("상태: 자동")

        notification.notify(
            title='Auto Mode',
            message='자동으로 변경되었습니다.',
            app_name="앱 이름",
            app_icon='bluemen_white.ico',  # 'C:\\icon_32x32.ico'
        )

    def Auto(self):
      if self.isAuto:
        if self.tmp > '받아올 온도 값':
          while self.tmp == '받아올 온도 값':
            self.now_tmp -= 1
            self.tmp.setText(str(self.now_tmp))
            client.publish('common', json.dumps("2"), 2)
            time.sleep(1)
        elif self.tmp < '받아올 온도 값':
          while self.tmp == '받아올 온도 값':
            self.now_tmp += 1
            self.tmp.setText(str(self.now_tmp))
            client.publish('common', json.dumps("1"), 1)
            time.sleep(1)
        elif self.soilhum > '받아올 토양습도 값':
          while self.soilhum == '받아올 토양습도 값':
            self.now_soilhum -= 1
            self.soilhum.setText(str(self.now_soilhum))
            client.publish('common', json.dumps("4"), 4)
            time.sleep(1)
        elif self.soilhum < '받아올 토양습도 값':
          while self.soilhum == '받아올 토양습도 값':
            self.now_soilhum += 1
            self.soilhum.setText(str(self.now_soilhum))
            client.publish('common', json.dumps("3"), 3)
            time.sleep(1)
        elif self.hum > '받아올 습도 값':
          while self.hum == '받아올 습도 값':
            self.now_hum -= 1
            self.hum.setText(str(self.now_hum))
            client.publish('common', json.dumps("6"), 6)
            time.sleep(1)
        elif self.hum < '받아올 습도 값':
          while self.hum == '받아올 토양습도 값':
            self.now_hum += 1
            self.soilhum.setText(str(self.now_soilhum))
            client.publish('common', json.dumps("5"), 5)
            time.sleep(1)
        else:
          pass
    def dynamic_sensor(self):
      count = []
      hum = []
      soilHum = []
      tmp = []

      for i in db['sensors'].find():
        count.append(i)
      count = count[len(count)-10:]
      
      for i in range(len(count)):
        hum.append(int(tmp[i]["hum"]))
        soilHum.append(int(tmp[i]["soilHum"]))
        tmp.append(int(tmp[i]["tmp"]))
        # tm = str(tmp[i]["created_at"])
        # time.append(tm[11:])
  
      plant_hum = ['적정 습도']
      plant_soilHum = ['적정 토양 습도']
      plant_tmp = ['적정 온도']


      # if abs(hum[-1] - plant_hum[-1]) <= 5 or abs(soilHum[-1] - plant_soilHum[-1]) <= 5  or abs(tmp[-1]- plant_tmp[-1]) <= 5:
      #   self.label_4.setPixmap(QtGui.QPixmap("./assignment/flower.png"))
      #   apply_stylesheet(app, theme='dark_lightgreen.xml')
      # else:
      #   self.label_4.setPixmap(QtGui.QPixmap("./assignment/wither.png"))
      #   apply_stylesheet(app, theme='light_lightgreen.xml')




if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())