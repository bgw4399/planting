# 조원
* 배진우 : PyQt , 웹
* 하은영 : 아두이노, 웹
* 이상현 : 아두이노, 웹

# 목표
* 평소 식물을 기르기 어려워하는 사람들이나 난이도가 높은 식물들을 보다 잘 키울 수 있게 도와주는 프로그램을 구현하고자한다.
* 웹, 아두이노, 파이큐티, mongoDB를 모두 이용하여 구현하고자한다.

# 기능
##  ARDUINO
* 아두이노에서 센서를 이용해 현재 온도, 습도, 토양 습도 값을 측정한다.
* 측정된 값들을 와이파이를 연결해 mongoDB로 데이터를 보내준다.
![image](https://user-images.githubusercontent.com/104902657/199431982-08e87d05-4502-41b1-9edb-aabdb63dcab9.png)


##  WEB
* 자신이 키우고자 하는 식물에 대한 정보를 저장한다.

![image](https://user-images.githubusercontent.com/104902657/199142742-51a13ad1-d56f-4566-ac11-d20e174b5885.png)

* 식물을 등록할 경우 나뭇잎의 색깔이 채워지고 밑에 이름이 나타난다. 나뭇잎 클릭시 그 식물에 필요한 온도,수분, 토양습도의 범위를 표시한다.

![image](https://user-images.githubusercontent.com/104902657/199142757-ba8ca397-ea8a-4cae-8f9a-96759e1ef5dc.png)

* 식물이 정상 범위가 아닐 때, 그림과 같은 화면이 출력되고 각 그림 밑에 mongoDB에서 가져온 현재 온도,수분,토양습도의 수치를 표시한다. 기준치보다 현재 값이 높다면 위 화살표, 아니라면 아래 화살표로 표시한다.

![image](https://user-images.githubusercontent.com/104902657/199142772-9c8f5948-ed3e-4792-ad6d-6398af747988.png)

* 식물이 정상 범위일 때 그림과 같은 화면이 출력되고 각 그림 밑에 현재 온도,수분,토양습도의 수치 표시한다.

![image](https://user-images.githubusercontent.com/104902657/199143120-6c3742a2-0aa6-448d-8374-bb6e9b54142a.png)

##  PyQT
* 식물이 정상 범위 내에 있다면 다음 그림처럼 밝은 꽃과 밝은 화면이 나타난다. 웹에서 가져온 식물의 정보,목표 수치들의 값을 기준으로 삼는다. 밑에 있는 숫자는 실시간 정보이고, 이는 mongoDB에서 데이터를 가져온다. 이 때 자동 모드라면 목표치로 자동으로 바뀌며 센서에 신호를 보낸다.

![image](https://user-images.githubusercontent.com/104902657/199149547-3b698cb1-70a2-44b2-908c-36a05d5eeaa7.png)

* 식물이 정상 범위 내에 있지 않다면 다음 그림처럼 시든 꽃과 어두운 화면이 나타난다.

![image](https://user-images.githubusercontent.com/104902657/199149492-fa50e9a3-5959-4401-a760-4ce62355f8d7.png)

* 자동 모드에서 +나 -를 누를 경우 다음과 같은 알람과 함께 수치가 바뀌지 않는다.

![image](https://user-images.githubusercontent.com/104902657/199144456-eb6bbb15-6b8d-46b2-a75d-e1aa52d5c44a.png)

* 자동 모드를 누르면 수동 모드로 바뀌게 되는데 이 때는 +나 -를 직접 눌러 센서로 신호를 보낼 수 있다.

![image](https://user-images.githubusercontent.com/104902657/199149293-354693cc-f47c-4c3e-a94b-d5588fa9f4ed.png)
