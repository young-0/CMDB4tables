## 这是一个教程版的CMDB资产管理系统
## 该教程发布在www.liujiangblog.com上
## 该教程更新于2019年4月
## 项目基于**Django2.2**、**Adminlet-2.4.10**、Python3.7、Pycharm2018、windows10
## 该项目已经录制了[视频教程](http://www.liujiangblog.com/video/)

初始化数据库

python3 manage.py help 查看帮助

python3 manage.py migrate 生成数据库表

运行

python3 manage.py runserver 0:8000

访问  
http://172.16.80.101:8000/assets/index/

写入数据

curl -H "Content-Type:application/json" -X POST 
-d '{"name":"service","sn":"imageTags","env":"ENV"}' http://127.0.0.1:8000/assets/uploadtags

访问  
http://172.16.80.101:8000
