import folium
import os
import csv

def draw_gps(color1,color2):
    """
    绘制gps轨迹图
    :param locations: list, 需要绘制轨迹的经纬度信息，格式为[[lat1, lon1], [lat2, lon2], ...]
    :param output_path: str, 轨迹图保存路径
    :param file_name: str, 轨迹图保存文件名
    :return: None
    """
    
    locations1 = []
    with open('6d420c983dc4ad2cffb51f647c4361dd_track.csv') as f:
      reader = csv.reader(f)
      next(reader) # skip header
      
      for row in reader:
        location = [float(row[1]), float(row[2])]
        locations1.append(location)
    print(locations1)
    
    locations2 = []
    with open('6d420c983dc4ad2cffb51f647c4361dd.tgj') as f:
      reader = csv.reader(f)
      next(reader) # skip header
      
      for row in reader:
        location = [float(row[1]), float(row[2])]
        locations2.append(location)
    print(locations2)
    
    m1 = folium.Map(locations1[0], zoom_start=15, attr='default')  # 中心区域的确定
    m2 = folium.Map(locations2[0], zoom_start=15, attr='default')  # 中心区域的确定

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations1,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color=color1,  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m1)  # 将这条线添加到刚才的区域m内

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations2,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color=color2,  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m2)  # 将这条线添加到刚才的区域m内

    # 起始点，结束点
    folium.Marker(locations1[0], popup='<b>Starting Point</b>').add_to(m1)
    folium.Marker(locations2[-1], popup='<b>End Point</b>').add_to(m2)

    m1.save(os.path.join('.','12.HTML'))  # 将结果以HTML形式保存到指定路径~
    m2.save(os.path.join('.', '21.HTML'))  # 将结果以HTML形式保存到指定路径
    


draw_gps('red','orange')

