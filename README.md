# Labelme2Coco
Make your own dataset for object detection and transform the format to coco json format

## labelme安装步骤

系统：win10(推荐)；电脑上配置好python环境（py3.5；3.6；3.7均可）或anconda虚拟环境；<br>
方式一：python环境<br>
```
python –m pip install –-upgrade pip
pip3 install PyQt5-sip
pip3 install PyQt5
pip install labelme
```

方式二：anconda虚拟环境<br>
// base环境测试成功（不用conda create新环境）<br>
```pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ PyQt5 labelme```

## labelme使用
打开cmd, 输入labelme；Open Dir，Edit->Create Recangle  <br>
Note:                  <br>
1）bbox的label命名格式如：car 则无需修改labelme2coco.py的代码  <br>
2）bbox的label命名格式如：vehicle_car  (含有父类信息)则看labelme2coco.py对应部分注释,做相应修改 <br>

## 转coco格式
Note: <br>
1) MyEncoder类可以防止json.dump()错误：Object of type 'int64' is not JSON serializable <br>
2) 读写文件的路径需要在labelme2coco.py的最后做相应地修改  <br>
