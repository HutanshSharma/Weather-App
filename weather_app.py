import sys,requests,os
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QGridLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QFontDatabase,QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "weather-app.png")))

        self.input=QLabel("Enter the name of the place",self)
        self.button=QPushButton("Submit",self)
        self.enterhere=QLineEdit(self)
        self.temperatureC=QLabel(self)
        self.temperatureF=QLabel(self)
        self.temperatureK=QLabel(self)
        self.emoji=QLabel(self)
        self.description=QLabel(self)
        self.humidity=QLabel(self)
        self.myfont=QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "Lato-black.ttf"))
        self.fontfamily=QFontDatabase.applicationFontFamilies(self.myfont)[0]
        self.fontstyle=QFont(self.fontfamily)
        self.initgui()

    def initgui(self):

        layout=QGridLayout()
        layout.addWidget(self.input,0,0,1,3)
        layout.addWidget(self.button,1,2)
        layout.addWidget(self.enterhere,1,0,1,2)
        layout.addWidget(self.temperatureC,2,0)
        layout.addWidget(self.temperatureF,2,1)
        layout.addWidget(self.temperatureK,2,2)
        layout.addWidget(self.emoji,3,0,1,1)
        layout.addWidget(self.description,4,0,1,3)
        layout.addWidget(self.humidity,3,1,1,2)
        self.setLayout(layout)

        self.input.setFont(self.fontstyle)
        self.button.setFont(self.fontstyle)
        self.enterhere.setFont(self.fontstyle)
        self.temperatureC.setFont(self.fontstyle)
        self.temperatureF.setFont(self.fontstyle)
        self.temperatureK.setFont(self.fontstyle)
        self.description.setFont(self.fontstyle)
        self.humidity.setFont(self.fontstyle)

        self.input.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.emoji.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.description.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.temperatureC.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.temperatureF.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.temperatureK.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)
        self.humidity.setAlignment(Qt.AlignHCenter |Qt.AlignVCenter)

        self.enterhere.setPlaceholderText("Enter here")

        self.input.setObjectName("input")
        self.button.setObjectName("button")
        self.enterhere.setObjectName("textbox")
        self.emoji.setObjectName("emoji")
        self.description.setObjectName("text")
        self.temperatureC.setObjectName("temp")
        self.temperatureF.setObjectName("temp")
        self.temperatureK.setObjectName("temp")
        self.humidity.setObjectName("text")

        self.setStyleSheet("""
                QWidget{
                           background-color:#123456;
                           }
                QLabel{
                           color:white;
                           border-radius:10px
                           }
                QLabel#input{
                           font-size:50px;
                           padding:30px 50px;
                           background-color:#4356b5;
                           }
                QPushButton#button{
                           font-size:30px;
                           padding:30px 50px;
                           color:White;
                           border-radius:10px;
                           background-color:#445191
                           }
                QPushButton#button:hover{
                           background-color:#6f79ad;
                           }
                QLineEdit{
                           font-size:30px;
                           padding:30px 50px;
                           color:white;
                           border-radius:10px;
                           border:1px solid white
                           }
                QLabel#temp{
                           font-size:35px;
                           padding:10px 50px;
                           padding-top:40px
                           }
                QLabel#emoji{
                           font-size:75px;
                           padding:10px 50px;
                           font-family:Segoe UI emoji;
                            }
                QLabel#text{
                           font-size:40px;
                           padding:30px 50px;}
                    """)
        
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        city_name=self.enterhere.text()
        api_key="10bb801e502fdc8ce58638b3af77ff64"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response=requests.get(url)
        if response.json()["cod"]==200:

            temp=response.json()["main"]["temp"]
            self.temperatureK.setText(str(temp)+" K")
            temp_in_C=f"{temp-273:.2f}"
            self.temperatureC.setText(temp_in_C+"°C")
            temp_in_f=f"{((9/5)*float(temp_in_C))+32:.2f}"
            self.temperatureF.setText(temp_in_f+"°F")

            desc=response.json()["weather"][0]["description"]
            self.description.setText(f"Description  :  {desc.capitalize()}")

            humidity=response.json()["main"]["humidity"]
            self.humidity.setText(f"Humidity : {humidity}%")

            id=response.json()["weather"][0]["id"]
            self.emojicall(id)

        else:
            self.temperatureF.setText("Invalid Input !!!")
            self.temperatureC.setText("")        
            self.temperatureK.setText("")        
            self.description.setText("")        
            self.emoji.setText("")        
            self.humidity.setText("")
            self.emoji.setStyleSheet("background-color:#123456")               

    def emojicall(self,id):
        if id>=200 and id<=232:
            self.emoji.setText("⛈️")
        elif id>=300 and id<=321:
            self.emoji.setText("☔")
        elif id>=500 and id<=531:
            self.emoji.setText("🌧️")
        elif id>=600 and id<=622:
            self.emoji.setText("☃️")
        elif id==800:
            self.emoji.setText("☀️")
        elif id>=800 and id<=804:
            self.emoji.setText("⛅")
        elif id==781:
            self.emoji.setText("🌪️")
        elif id>=701 and id<=771:
            self.emoji.setText("🌫️")
        
        self.emoji.setStyleSheet("background-color:#189ab4")
            

app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec_())