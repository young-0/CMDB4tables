## 参考 https://github.com/feixuelove1009/CMDB

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
