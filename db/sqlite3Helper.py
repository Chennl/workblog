import sqlite3
import os
import time
from datetime import datetime

class sqliteTool(object):
    def __init__(self,db='test.db'):
        self.db=db
        self.display=False
    def connect(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.statement=''
        self.connected = True
    def close(self):
        self.connection.commit()
        self.connection.close()
        self.connected = False

    def query(self,statement):
        statement = statement.strip()
        if not self.connected:
            self.connect()
        try:
            self.cursor.execute(statement)
            data = self.cursor.fetchall()
        except sqlite3.Error as error:
            print('An error occurred:', error.args[0])
            print('For the statement:', statement)



print(time.time())
# path = os.getcwd()
# print(path)
# files = os.listdir(path)
conn =sqlite3.connect('workblog.db')
cur =  conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,createtime TIME)")
now =time.time()
# n=cur.execute("DELETE FROM test ")
# cur.execute("INSERT INTO test VALUES (1,'name1',22,%d)"%now)
# cur.execute("INSERT INTO test values(?,?,?,?)",(2,"name2",20,now))
# cur.executemany('INSERT INTO test VALUES (?,?,?,?)',[(3,'name3',19,now),(4,'name4',26,now),(5,'name5',19,now),(6,'name6',26,now)])
# cur.execute("UPDATE test SET name=? WHERE id=?",("甲",1))
# cur.execute("UPDATE test SET name='乙' WHERE id=2")
#n=cur.execute("DELETE FROM test WHERE id=?",(1,))
#n=cur.execute("DELETE FROM test WHERE id=2")
#conn.commit()

# cur.execute('SELECT *  from test')
# for row in cur:
#     print(row)
#print(cur.fetchone())
# print(cur.fetchmany(3))
# all_data = cur.fetchall()
# count = len(all_data)
# print('共有 '+ str(count) + ' 条记录')
##查表结构
#cur.execute("PRAGMA table_info(test)")
#print(cur.fetchall())
## [(0, 'id', 'integer', 0, None, 1), (1, 'number', 'varchar(20)', 1, None, 0)]
#cur.execute('drop table test;')


## dict to db
mylist = [
            {
                "id": 56,
                "name": "雅诗兰黛（Estee Lauder）持妆无瑕气垫粉霜 17# SPF30+/PA+++ 12g（1W1 BONE 自然偏白肤色）新老包装随机  ",
                "price": 369.00,
                "privilegePrice": 420.00,
                "imgUrl": "https://img11.360buyimg.com/n7/s370x370_jfs/t22306/277/1526836895/190400/1f662473/5b2c90c8N87f619ac.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t23023/35/468034734/203240/d969c336/5b30bac1N7cac0f4c.jpg;https://img30.360buyimg.com/sku/jfs/t23656/57/473977005/169479/1ccfab1e/5b30bac1N937c5918.jpg;https://img30.360buyimg.com/sku/jfs/t21418/50/1690364234/57472/5410ac22/5b30bac1Nbc5203f9.jpg;https://img30.360buyimg.com/sku/jfs/t24295/105/563158282/64093/b731726d/5b359d55Na8f62971.jpg;https://img30.360buyimg.com/sku/jfs/t22762/225/464364516/106407/65d0f278/5b30bac1Nfad8f2cd.jpg;https://img30.360buyimg.com/sku/jfs/t21421/72/1689395488/44217/b1498e6d/5b30bac1Nb72cd089.jpg;https://img30.360buyimg.com/sku/jfs/t21412/165/1760284332/77072/5090b482/5b30bac1Nf244a651.jpg;https://img30.360buyimg.com/sku/jfs/t24439/61/479709911/56910/d6c592ea/5b30bac1N8e62a761.jpg;https://img30.360buyimg.com/sku/jfs/t24439/61/479709911/56910/d6c592ea/5b30bac1N8e62a761.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 6958,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.8",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 55,
                "name": "雅诗兰黛 Estee Lauder 专研紧塑精华素  50ml  (线雕 精华，  紧致上扬）",
                "price": 979.00,
                "privilegePrice": 1089.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t18601/67/2327946788/116068/a8bd4a43/5aefe87aN2bab70b6.jpg!q80.dpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t16804/7/2353293106/105081/7e822f50/5aefe704Nd1fe86c2.jpg; https://img30.360buyimg.com/sku/jfs/t17932/302/2306136735/63684/efdd9c37/5aefe704N669f5693.jpg;uhttps://img30.360buyimg.com/sku/jfs/t16801/40/2334287936/129167/bd0f9306/5aefe70bN403644d6.jpg;https://img30.360buyimg.com/sku/jfs/t20077/34/311258456/108994/1f97a01a/5aefe709N555641d4.jpg;https://img30.360buyimg.com/sku/jfs/t18448/146/2268502375/81804/f27bc1d2/5aefe702N57ea8da0.jpg;https://img30.360buyimg.com/sku/jfs/t18046/195/2364128791/137799/1049ea44/5aefe70fN6f52ca27.jpg;https://img30.360buyimg.com/sku/jfs/t18277/88/2271445578/84492/dd0a2c9/5aefe70cN590137e7.jpg;https://img30.360buyimg.com/sku/jfs/t17503/341/2345340921/54264/b3169d17/5aefe70eNdc4144bb.jpg;https://img30.360buyimg.com/sku/jfs/t17593/10/2295824543/58328/db493003/5aefe70eN5b0ddea4.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 2181,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.0",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 54,
                "name": "雅诗兰黛（ESTEELAUDER）红石榴鲜养焕亮女士护肤化妆品套装 正装水+洁面+日霜+眼霜+精华+粉底",
                "price": 880.00,
                "privilegePrice": 934.00,
                "imgUrl": "https://img10.360buyimg.com/n7/s370x370_jfs/t20437/289/1725616899/353585/614763/5b31a0ceN7f4f913f.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/popWaterMark/jfs/t19417/150/2646023481/229973/898a4533/5aff9a6aN3b763fe8.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t18664/83/2630069693/142080/60f3f444/5aff9a6aN99cf1e67.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t16975/286/2570793976/98319/655adbef/5aff9a6aNcf59ba1c.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t22348/195/159928765/208036/b6ce9180/5aff9a6aN1029e5fd.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t19261/146/2521216762/64088/4eeaa231/5aff9a6aN52c1e98f.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t16783/2/2609245928/89780/dda11e3e/5aff9a6aNba3c72e7.jpg.dpg;http://img30.360buyimg.com/popWaterMark/jfs/t17926/38/2606507283/65229/aae7adf0/5aff9a6bN1972e5cc.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t18430/180/2528308859/201934/9f651bab/5aff9a6bNd7eedae2.jpg.dpg;https://img30.360buyimg.com/popWaterMark/jfs/t18976/356/2614161303/55352/5e3d96d4/5aff9a75Nde4cc645.jpg.dpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1873,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.4",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 53,
                "name": "雅诗兰黛（Estee Lauder）鲜活亮采果萃水（滋润型）200ml（爽肤水 红石榴 补水保湿 干性肌肤）",
                "price": 399.00,
                "privilegePrice": 466.00,
                "imgUrl": "https://img11.360buyimg.com/n7/s370x370_jfs/t17110/221/817454081/71160/c0a639d0/5aab69deNe0c975f7.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t5926/135/9587596423/110905/f7bd526e/59940f2bNdfb56a4b.jpg;https://img30.360buyimg.com/sku/jfs/t7930/292/502689290/84445/4df3f823/59940f2bNe92dc647.jpg;https://img30.360buyimg.com/sku/jfs/t7753/364/513099891/145114/e412386d/59940f2bN6be55ce9.jpg;https://img30.360buyimg.com/sku/jfs/t5953/220/9689612416/52624/f81cf54/59940f2bNf9491510.jpg;https://img30.360buyimg.com/sku/jfs/t7786/358/515598076/95240/dcda6822/59940f2bN30d4e0d1.jpg;https://img30.360buyimg.com/sku/jfs/t7405/328/510674265/52259/b978864d/59940f2bN49ff4132.jpg;https://img30.360buyimg.com/sku/jfs/t7534/344/509271536/80864/295da304/59940f2bNd145d192.jpg;https://img30.360buyimg.com/sku/jfs/t7687/332/514833675/77271/3a8bb2b7/59940f2bNd0a645a0.jpg;https://img30.360buyimg.com/sku/jfs/t7669/8/557968565/50155/b271d718/59940f2bNda023d51.jpg;https://img30.360buyimg.com/sku/jfs/t7375/332/516598563/66730/57e872a0/59940f2fNc61ca8d3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1437,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.6",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 52,
                "name": "雅诗兰黛（Estee Lauder）肌初赋活原生液200ml(护肤精华 化妆水 保湿补水收缩毛孔)",
                "price": 789.00,
                "privilegePrice": 830.00,
                "imgUrl": "https://img13.360buyimg.com/n7/s370x370_jfs/t6082/110/283779492/177938/4777ed9d/59278aa7N6184a2a7.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t7762/211/596627530/158129/e114b194/59950a30Nd0954785.jpg;https://img30.360buyimg.com/sku/jfs/t7087/297/2342012803/143179/dbb61f07/59950a30N0d740ad5.jpg;https://img30.360buyimg.com/sku/jfs/t7720/239/612920808/190684/9567dfdb/59950a36Nc1cf7a79.jpg;https://img30.360buyimg.com/sku/jfs/t7369/129/575950154/131595/f854d3/59950a3bN8bde8f40.jpg; https://img30.360buyimg.com/sku/jfs/t7405/194/582328689/113983/1fcf8044/59950a3cNb45812ad.jpg;https://img30.360buyimg.com/sku/jfs/t7543/227/604818492/61207/be368306/59950a3fN1e99583d.jpg;https://img30.360buyimg.com/sku/jfs/t7150/215/2311699304/134385/9d284f1d/59950a3fN965f7096.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 886,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.5",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 51,
                "name": "雅诗兰黛（Estee Lauder）新肌透修护眼部密集精华15ml （眼霜 眼部精华）",
                "price": 579.00,
                "privilegePrice": 612.00,
                "imgUrl": "https://img11.360buyimg.com/n2/s350x350_jfs/t9172/137/1477928132/173142/818b28aa/59ba1769N9c9b7660.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t9220/313/1466732076/281478/bacc5253/59ba148eN2ed8e131.jpg;https://img30.360buyimg.com/sku/jfs/t8248/341/1478174160/295419/9f84cc2a/59ba1483N4679ccbf.jpg;https://img30.360buyimg.com/sku/jfs/t8305/284/1459181835/293444/62b3f471/59ba148eN98be0bf4.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 693,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.5",
                "activityId": 3,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 50,
                "name": "欧莱雅 LOREAL 男士水能保湿酷爽水凝露120ml（保湿露 保湿乳 渗透补水 滋润肌肤）",
                "price": 80.00,
                "privilegePrice": 96.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t2485/63/1124159075/138072/23f993a/567a57a8N2b78637b.jpg!q80.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t18790/311/1703785993/130517/ead29478/5ad41d19Ne24533d7.jpg;https://img30.360buyimg.com/sku/jfs/t18430/119/1674078028/243123/89b96b5f/5ad41d19Nd11f1e72.jpg;https://img30.360buyimg.com/sku/jfs/t18262/107/1621910801/273269/d67a0d81/5ad41d19N37fea36e.jpg;https://img30.360buyimg.com/sku/jfs/t18265/330/1683439864/181669/633b783b/5ad41d19N3a546bfc.jpg;https://img30.360buyimg.com/sku/jfs/t17032/281/1674652732/133031/1447ac31/5ad41d19Ne58feb49.jpg;https://img30.360buyimg.com/sku/jfs/t19780/104/1710555938/196959/cf308621/5ad41d19Nb79580da.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1002,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.3",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 49,
                "name": "欧莱雅(LOREAL)复颜玻尿酸化妆品护肤套装(晶露130ml+乳液110ml+晶露65ml+乳液50ml+导入霜15ml(赠品随机发))",
                "price": 129.00,
                "privilegePrice": 134.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t19711/150/2470548977/494387/9d4aba06/5af699aaNc796b9f2.png!q80.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t19681/25/2211634922/224287/191b4eab/5aec3acbN626f89d4.jpg;https://img30.360buyimg.com/sku/jfs/t2467/315/1479078334/2361/4757d7d6/566010f4N01f5d17a.png;https://img30.360buyimg.com/sku/jfs/t16642/306/2220348263/237236/7a8104c9/5aec3af5N9813656b.jpg;https://img30.360buyimg.com/sku/jfs/t9727/247/1192461728/260447/b2a56938/59dddb16Ne97d12c9.jpg;https://img30.360buyimg.com/sku/jfs/t10876/185/1189988925/237051/caeaf09f/59dddb23N88df21ff.jpg;https://img30.360buyimg.com/sku/jfs/t14422/331/2526414129/205527/11b1b27b/5aa5f151Nf20af9d3.jpg;https://img30.360buyimg.com/sku/jfs/t2467/315/1479078334/2361/4757d7d6/566010f4N01f5d17a.png",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 521,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.6",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 48,
                "name": "欧莱雅（LOREAL）三合一卸妆洁颜水深层清洁魔力水套装（倍润型400ml+95mlx3（随机发)）",
                "price": 129.00,
                "privilegePrice": 134.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t15238/58/712902288/156770/2353e01c/5a364885N51145b5f.jpg!q80.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t14401/144/2085783970/231641/69229849/5a7ab846N8f9106b2.jpg;https://img30.360buyimg.com/sku/jfs/t2467/315/1479078334/2361/4757d7d6/566010f4N01f5d17a.png;https://img30.360buyimg.com/sku/jfs/t20563/281/1399665309/202489/eda62271/5b27aabaNd42e4aa1.jpg;https://img30.360buyimg.com/sku/jfs/t21274/261/1374564555/286328/3c29ac9c/5b27ab05Nc91ab167.jpg;https://img30.360buyimg.com/sku/jfs/t23767/308/172580340/208361/fef0db6/5b27aabfNa0b1602c.jpg;https://img30.360buyimg.com/sku/jfs/t7525/166/1132029644/187066/d63ee227/599aaa3eN99d283ae.jpg;https://img30.360buyimg.com/sku/jfs/t7882/103/1148017296/231718/90bd1c2d/599aaa3eNda158c72.jpg;https://img30.360buyimg.com/sku/jfs/t7636/202/1167823696/378127/73068b16/599aaa3eNefe16087.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 646,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.6",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 47,
                "name": "欧莱雅(LOREAL)金致臻颜化妆品护肤套装(洁面+活肤水+乳液+眼霜；赠活源液*3+日霜+眼霜旅行装)",
                "price": 899.00,
                "privilegePrice": 912.00,
                "imgUrl": "https://img10.360buyimg.com/evalpic/s750x750_jfs/t18412/313/1972566277/119773/84b93707/5adfe0c0N2d3afb08.jpg.dpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t20773/174/189321095/124383/34d408e5/5b027095N114edd30.jpg;https://img30.360buyimg.com/sku/jfs/t22054/195/194589200/113441/6d7cc199/5b027096N5250a046.jpg;https://img30.360buyimg.com/sku/jfs/t21415/23/192126494/138668/126bd835/5b027095N41797db2.jpg;https://img30.360buyimg.com/sku/jfs/t18187/26/2640598371/206476/b9bd39a9/5b027096Nfb2fe414.jpg;https://img30.360buyimg.com/sku/jfs/t19744/242/2669201655/117277/503ff0db/5b027095Na8564fbc.jpg;https://img30.360buyimg.com/sku/jfs/t19675/281/2657017683/76454/6ee7c792/5b027094N2cff2eab.jpg;https://img30.360buyimg.com/sku/jfs/t21412/25/192896743/80548/558c9d21/5b027095Na7af23f1.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 533,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.9",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 46,
                "name": "欧莱雅（LOREAL）男士劲能醒肤露8重功效50ml(持久滋润保湿抗肌肤疲劳护肤霜)(雷神版随机发货)",
                "price": 110.00,
                "privilegePrice": 132.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t13123/170/1228546971/230973/f33806f3/5a1cdae5Nf9b9a09f.jpg!q80.jpg",
                "details": "https://img30.360buyimg.com/sku/jfs/t18538/233/1344003468/105227/98998097/5ac490dcN0bf620a1.jpg; https://img30.360buyimg.com/sku/jfs/t19288/276/1334216833/136017/5b819810/5ac490dcN25b14019.jpg;https://img30.360buyimg.com/sku/jfs/t18481/154/1503488414/345954/58182c52/5acc5b4eN2da3fd68.jpg;https://img30.360buyimg.com/sku/jfs/t17365/132/1523000228/102696/bd368f34/5acc5b82Ne6494a6c.jpg;https://img30.360buyimg.com/sku/jfs/t18109/162/1631357177/314771/e69f8165/5ad06a24N8f0515f6.jpg;https://img30.360buyimg.com/sku/jfs/t19624/27/1250909160/294007/ba1d3fc0/5ac3330aNe5d8326d.jpg;https://img30.360buyimg.com/sku/jfs/t18655/17/1315441024/114547/43f24fd0/5ac490dcN409d46af.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 271,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.3",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 45,
                "name": "欧莱雅（LOREAL）复颜抗皱紧致滋润眼霜15ml (欧莱雅女士 抗皱 紧致 淡化黑眼圈 眼袋)",
                "price": 240.00,
                "privilegePrice": 297.00,
                "imgUrl": "https://img10.360buyimg.com/evalpic/s750x750_jfs/t18676/216/1129511635/97830/7a0e0d59/5abc92e7Nc4ae3ea2.jpg.dpg",
                "details": "https://img30.360buyimg.com/cms/jfs/t3265/156/5618045534/354226/ece91dee/5875ab5dN359c4194.jpg.dpg;https://img13.360buyimg.com/cms/jfs/t3937/115/1437846119/206722/4575f112/5875ab5cNf4dfdd59.jpg.dpg;https://img12.360buyimg.com/cms/jfs/t3229/137/5609962983/209345/79fb4818/5875ab5dN291da545.jpg.dpg;https://img11.360buyimg.com/cms/jfs/t3934/147/1393534393/89660/a4a27d26/58761158N043f484c.jpg.dpg;https://img12.360buyimg.com/cms/jfs/t3952/106/1379861376/237979/f94ac718/5875ab5dN2c5ad596.jpg.dpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 207,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.1",
                "activityId": 2,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 44,
                "name": "欧莱雅集团小美盒 馥妍悦妆盒 YSL圣罗兰 反转巴黎黑鸦片香水/纯口红13号色/兰蔻菁纯口红 防晒隔离乳/植村秀大师粉底液 旅行彩妆套装",
                "price": 499.00,
                "privilegePrice": 512.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t17095/312/2066965985/178109/ac606a82/5ae4110cN85cbb1fd.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdcvis/2018/05/15/26/ba79a67e894f4b3aaa229922119d78f9-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/05/15/153/0454a43ce21d4c2b8af70ebce0648e6e-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/05/15/193/66715b0a207b4612996cdf386a2b601e-651.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 263,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.7",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 43,
                "name": "兰蔻Lancome珍爱香水 30ml 持久留香 女士香水",
                "price": 515.00,
                "privilegePrice": 567.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t19120/183/929770392/331686/57cb6ac3/5ab31e68N10109948.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/523/406/3119587166887406523/4/3147758034905-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/523/406/3119587166887406523/4/3147758034905-110_2.jpg;https://a.vimage1.com/upload/merchandise/pdc/523/406/3119587166887406523/4/3147758034905-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 325,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.1",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 42,
                "name": "兰蔻Lancome男仕新塑颜面霜 50ml 男士乳液",
                "price": 709.00,
                "privilegePrice": 756.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t1660/202/82960845/138699/754d1e0a/55cd8a54Neaf683d7.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/499/068/2259681113038068499/5/3605530304122-110_1.jpg;https://a.vimage1.com/upload/merchandise/lap/2017/03/29/34/36107765.jpg;https://a.vimage1.com/upload/merchandise/pdc/499/068/2259681113038068499/5/3605530304122-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 245,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.4",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 41,
                "name": "兰蔻Lancome臻白晚霜 50ml3件套 美白 修复 淡斑 修复 护肤套装",
                "price": 710.00,
                "privilegePrice": 788.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t20260/195/791600249/102527/ebaa58e3/5b17d3c7Nb513ecb1.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/877/071/30194448949071877/0/HBLC1805291085-655.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 191,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.0",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 40,
                "name": "兰蔻Lancome新立体塑颜焕活精华乳 30ml保湿 滋润 美白 淡斑 修复 面部精华",
                "price": 788.00,
                "privilegePrice": 832.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t4420/336/3580516889/138884/1d32af26/59004d81Nc9d2a5a1.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/058/100/9027465453069100058/7/3605533094266-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/058/100/9027465453069100058/7/3605533094266-110_2.jpg;https://a.vimage1.com/upload/merchandise/pdc/058/100/9027465453069100058/7/3605533094266-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 211,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.5",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 39,
                "name": "兰蔻Lancome菁纯臻颜润养美容液 150ml4件套 菁纯 爽肤水 护肤套装",
                "price": 820.00,
                "privilegePrice": 888.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t21994/150/1017730007/128949/f89974a4/5b1de979Nae222f11.png!q80.jpg",
                "details": "https:////a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-655.jpg;https://a.vimage1.com/upload/merchandise/pdc/857/745/98311390826745857/0/LCHB2018052355-656.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 91,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.2",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 38,
                "name": "兰蔻水光润养精华露 50ml",
                "price": 432.00,
                "privilegePrice": 465.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t18868/331/1513666742/107451/d8ce4d8a/5acc2a73N29727731.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/944/442/229760183039442944/0/3614271254979-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/944/442/229760183039442944/0/3614271254979-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/944/442/229760183039442944/0/3614271254979-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/944/442/229760183039442944/0/3614271254979-653.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 314,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.3",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 37,
                "name": "兰蔻Lancome『温和去角质』清滢洁面摩丝 200ml 洁面摩丝 洗面奶",
                "price": 298.00,
                "privilegePrice": 312.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t17299/105/1399542368/47231/5a77c837/5ac75098N57b4f2eb.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/076/085/5934899883949085076/5/3605530741385-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/076/085/5934899883949085076/5/3605530741385-110_2.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 235,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.6",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 36,
                "name": "兰蔻Lancome『干泡』新清滢柔肤洁面乳(干性)125ml 洁面 洗面奶",
                "price": 275.00,
                "privilegePrice": 323.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t21454/300/289801771/79149/76bf0240/5b07e06aNf301677d.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/270/572/8518277220199572270/11/3605530744560-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/270/572/8518277220199572270/11/3605530744560-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/270/572/8518277220199572270/11/3605530744560-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/270/572/8518277220199572270/11/3605530744560-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/270/572/8518277220199572270/9/3605530744560-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 70,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.5",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 34,
                "name": "兰蔻Lancome肌底精华浸润修复面膜 28g*7 小黑瓶精华 修复面膜",
                "price": 512.00,
                "privilegePrice": 580.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t18442/305/1780035627/266335/511498b7/5ad9750aNead807ab.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-655.jpg;https://a.vimage1.com/upload/merchandise/pdc/749/727/455784559533727749/2/4935421656931-655.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 53,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.8",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 35,
                "name": "兰蔻Lancome水光润养活力霜50ml 水光针 滋润 日霜",
                "price": 515.00,
                "privilegePrice": 588.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t12217/128/1282342481/168743/efb9e97f/5a1e6598N1501b8ff.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/722/246/27097994217246722/1/3614271304698-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/722/246/27097994217246722/1/3614271304698-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/722/246/27097994217246722/1/3614271304698-652.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 59,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.8",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 33,
                "name": "兰蔻Lancome新精华肌底液 50ml6件套 滋润 修护 护肤套装",
                "price": 1080.00,
                "privilegePrice": 1321.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t3385/88/2072669169/69916/a50306b2/583d49a5N084ee4b9.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/495/823/5143176021823495/0/HBLC1805288734-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/495/823/5143176021823495/0/HBLC1805288734-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/495/823/5143176021823495/0/HBLC1805288734-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/495/823/5143176021823495/0/HBLC1805288734-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/495/823/5143176021823495/0/HBLC1805288734-655.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 75,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.2",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 31,
                "name": "兰蔻Lancome美肤修护乳液 100ml 保湿 滋润 乳液",
                "price": 621.00,
                "privilegePrice": 678.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t16951/118/1653335814/98607/226203c2/5ad442bfN4dda2e8b.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/349/526/2051108155295526349/6/4992944850055-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/349/526/2051108155295526349/6/4992944850055-110_2.jpg;https://a.vimage1.com/upload/merchandise/pdc/349/526/2051108155295526349/6/4992944850055-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 47,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.2",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 32,
                "name": "兰蔻Lancome塑颜紧致焕白霜 紧致 美白 日霜",
                "price": 789.00,
                "privilegePrice": 810.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t18667/352/900792104/319492/e054eed1/5aaf8104Nba2e118f.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-655.jpg;https://a.vimage1.com/upload/merchandise/pdc/833/992/462258508783992833/0/3614271575203-656.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 43,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.7",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 30,
                "name": "兰蔻Lancome『舒缓晚霜』新水份缘舒缓晚霜 50ml 保湿 补水 舒缓 晚上",
                "price": 512.00,
                "privilegePrice": 624.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t17863/47/887158064/186698/a1c14f20/5ab06f44N3c6396a1.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/547/996/7425309885631996547/10/3605532533919-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/547/996/7425309885631996547/10/3605532533919-110_2.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 46,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.2",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 29,
                "name": "兰蔻眼部精华肌底液 20ml4件套",
                "price": 680.00,
                "privilegePrice": 872.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t18388/103/834146742/118433/c58df256/5aab5f83Nb410316c.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-651.jpg;https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-655.jpg;https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-656.jpg;https://a.vimage1.com/upload/merchandise/pdc/235/527/311669417218527235/0/HBLK20180511-657.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 42,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.8",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 28,
                "name": "兰蔻Lancome『微整精华』美肤修护美容液 200ml 微精华美容液",
                "price": 418.00,
                "privilegePrice": 534.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t16618/248/951624854/294232/ff5d22dd/5ab38093N4de72f48.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/707/785/6516990135786785707/11/4992944849554-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/707/785/6516990135786785707/11/4992944849554-110_2.jpg;https://a.vimage1.com/upload/merchandise/pdc/707/785/6516990135786785707/11/4992944849554-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 57,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.8",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 27,
                "name": "兰蔻Lancome『保湿水』臻白晶透精华水150ml 臻白精华水",
                "price": 530.00,
                "privilegePrice": 675.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t17146/6/1620296874/189364/d0eb2a9f/5ad069d3N9240373e.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/842/651/89866987583651842/0/4935421638722-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/842/651/89866987583651842/0/4935421638722-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/842/651/89866987583651842/0/4935421638722-653.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 49,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.9",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 26,
                "name": "欧莱雅集团小美盒 星耀彩妆盒 YSL圣罗兰口红 女神粉底液/兰蔻香水 小黑瓶/科颜氏金盏花爽肤水/植村秀卸妆油 彩妆护肤旅行套装",
                "price": 349.00,
                "privilegePrice": 563.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t19105/84/1946573122/120027/800966fe/5add9290Nae4473da.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdcvis/2018/03/26/41/a0d77a808e51492ba740346eca16827b-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/03/26/91/2a129a3f3ad64982a1060b6002693750-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/03/26/18/f5afb16cadb249dbaf83ec6317d28eb2-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/03/26/67/0b548769428f48b7801919cc56887789-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/03/26/110/d0afd67107654ed4a4e37b0f85628e0d-651.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 92,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "6.2",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 25,
                "name": "欧莱雅集团小美盒 美肤水盈盒（520礼盒） 全明星美容液 兰蔻粉水 水分缘啫喱 水光润养气泡爽肤水/科颜氏黄瓜水 金盏花水 旅行护肤套装",
                "price": 249.00,
                "privilegePrice": 332.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t22534/113/298670096/265728/73a65bed/5b2bcaa1N7eb493a2.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdcvis/2018/04/27/117/ecd93ab697204ce5b2761f6e993e493f-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/04/27/117/ecd93ab697204ce5b2761f6e993e493f-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/04/27/104/8128acd9b1a4475e8323b1d3b35df239-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/04/27/149/86c97a64fd534afba61f628edab737c1-651.jpg;https://a.vimage1.com/upload/merchandise/pdcvis/2018/04/27/194/27b0a4cfe8d0401c8e35b5c382cea1c5-651.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 45,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.5",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 24,
                "name": "兰蔻Lancome『小黑瓶』新精华肌底液 50ml 小黑瓶 面部精华",
                "price": 880.00,
                "privilegePrice": 1023.00,
                "imgUrl": "https://m.360buyimg.com/mobilecms/s750x750_jfs/t5344/45/384305013/97147/e26f3ee0/58feb0cdN927353e2.jpg!q80.jpg",
                "details": "https://a.vimage1.com/upload/merchandise/pdc/656/221/6643935350283221656/18/3605532978734-110_1.jpg;https://a.vimage1.com/upload/merchandise/pdc/656/221/6643935350283221656/18/3605532978734-652.jpg;https://a.vimage1.com/upload/merchandise/pdc/656/221/6643935350283221656/18/3605532978734-653.jpg;https://a.vimage1.com/upload/merchandise/pdc/656/221/6643935350283221656/18/3605532978734-654.jpg;https://a.vimage1.com/upload/merchandise/pdc/656/221/6643935350283221656/11/3605532978734-110_3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 34,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.6",
                "activityId": 1,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 23,
                "name": "日本 资生堂CPB肌肤之钥保湿露化妆水保湿润肤滋润型170ml",
                "price": 775.00,
                "privilegePrice": 827.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t10657/4/2676826589/85281/7ccbca40/59fbffcbN08c35916.jpg!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t11212/112/941452233/317511/554cf0a3/59fc0359N981364c3.png;https://img10.360buyimg.com/imgzone/jfs/t11647/345/955084931/93629/ac02571e/59fc0359N5a8a5ef7.png;https://img10.360buyimg.com/imgzone/jfs/t11674/332/928667938/228303/83c3286e/59fc0359Nd92eeb15.png;https://img10.360buyimg.com/imgzone/jfs/t11458/30/928297559/130827/4b21b5a3/59fc035aNbd2055e1.jpg;https://img10.360buyimg.com/imgzone/jfs/t9742/289/2649914887/115539/c6797f63/59fc0341Ndfefedf1.jpg;https://img10.360buyimg.com/imgzone/jfs/t11725/313/977472497/140168/9c47a6b4/59fc0342N83e3f807.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 166,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.4",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 22,
                "name": "韩国进口 A.by Bom艾柏梵超能婴儿冰凝叶子面膜10片",
                "price": 129.00,
                "privilegePrice": 138.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t16969/88/1564110409/175802/5a26675e/5acf2422N76c30469.png!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t15079/250/1378141301/90210/c5411bbb/5a4ce51aNda84dc5a.jpg;https://img10.360buyimg.com/imgzone/jfs/t14554/230/1355421978/43906/d1b2e3d/5a4ce518N95b58aa5.jpg;https://img10.360buyimg.com/imgzone/jfs/t16174/26/1128731260/160481/c88be136/5a4ce512N58d61b46.jpg;https://img10.360buyimg.com/imgzone/jfs/t14737/209/1338124278/63666/481bb308/5a4ce520Nb26519d4.jpg;https:////img30.360buyimg.com/sku/jfs/t19075/243/1609006120/266561/710d3aa3/5ad06f17N4f7f152b.jpg;https://img10.360buyimg.com/imgzone/jfs/t15916/327/1199031650/68490/b0082cc/5a4ce521N64d24657.jpg\n",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 160,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.3",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 21,
                "name": "韩国进口 A.by Bom艾柏梵超能婴儿基因再生桃花面膜5片",
                "price": 89.00,
                "privilegePrice": 101.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t17983/118/1563399958/139443/efd76f63/5acf23d7Nd76e0a77.png!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t15802/158/1316273396/120942/2d01b87d/5a4efea2N8cc2fbe3.jpg;https://img10.360buyimg.com/imgzone/jfs/t14800/333/1703088600/38534/80f023c7/5a55855fNd5ef51de.jpg;https://img10.360buyimg.com/imgzone/jfs/t16276/276/1177227900/150449/af90e7d4/5a4efea2N0318e978.jpg;https://img10.360buyimg.com/imgzone/jfs/t14197/175/1423119730/94268/fc1265f1/5a4efe9bNc80c86d0.jpg;https://img10.360buyimg.com/imgzone/jfs/t14506/328/1440386772/118215/43d5e0b6/5a4efea2Ncef088fa.jpg;https://img10.360buyimg.com/imgzone/jfs/t14611/174/1709964950/130347/76ddd87d/5a558557N1873ca8e.jpg;https://img10.360buyimg.com/imgzone/jfs/t15082/240/1448420653/68120/a4cfb8f7/5a4efe8eNdd413c20.jpg;https://img10.360buyimg.com/imgzone/jfs/t14605/306/1440959264/63911/a25b2d3b/5a4efea2N2abb2c5e.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 84,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.8",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 20,
                "name": "品牌直采 捷俊（JAYJUN）防雾霾透白修护面膜27ml 10片/盒",
                "price": 170.00,
                "privilegePrice": 189.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t8449/52/2392309676/452472/94321a74/59cca5d0Nce6b2c02.jpg!q70.jpg",
                "details": "https://img13.360buyimg.com/cms/jfs/t17965/171/354796120/303498/7f82de87/5a6eb0a8N578f2343.jpg;https://img13.360buyimg.com/cms/jfs/t17947/171/361108889/190428/dda759b/5a6eb0afN8ea3ec36.jpg;https://img12.360buyimg.com/cms/jfs/t16561/339/1923038925/133524/1143567d/5a6eb0b6N2b31e442.jpg;https://img20.360buyimg.com/cms/jfs/t16711/196/352610166/148325/6dde9ab7/5a6eb0cfN2c4746af.jpg;https://img30.360buyimg.com/cms/jfs/t19267/208/346999378/156410/1c807d8c/5a6eb0d2N7dbac4b3.jpg;https://img30.360buyimg.com/cms/jfs/t15454/106/2105960102/124164/d99166ef/5a6eb12eN19dcc83a.jpg;https://img11.360buyimg.com/cms/jfs/t16606/208/349833968/155296/6d8db454/5a6eb147Nf8344ead.jpg;https://img20.360buyimg.com/cms/jfs/t15748/64/2000451802/89546/7fedc0f7/5a6eb153Neee61999.jpg;https://img10.360buyimg.com/cms/jfs/t17749/303/356150240/232440/52fed16a/5a6eb169N778e8c12.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 129,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.0",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 19,
                "name": "品牌直采 捷俊(JAYJUN)玫瑰精华面膜25ml*10 补水保湿",
                "price": 135.00,
                "privilegePrice": 168.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t3085/190/8770910845/187674/11f0949d/58c89972N2e5c175a.jpg!q70.jpg",
                "details": "https://img20.360buyimg.com/vc/jfs/t5140/134/330610343/294446/9e31bdf4/58fdcd46N6419e6f3.jpg;http://img20.360buyimg.com/vc/jfs/t4684/19/4035557253/114995/7d35afc3/59092f1dN6860e95d.jpg;https://img20.360buyimg.com/vc/jfs/t4438/148/4036236532/135006/14271bef/59092f1cNbffc9a5f.jpg;https://img10.360buyimg.com/cms/jfs/t11683/102/133142231/306297/f0da95c6/59e8606aNbefec256.jpg;https://img20.360buyimg.com/vc/jfs/t5131/283/899507858/141629/75e93696/59092f21N58eba3d9.jpg;https://img13.360buyimg.com/cms/jfs/t11245/200/139867059/59473/256356fc/59e8608fNdb60d364.jpg;https://img11.360buyimg.com/cms/jfs/t7873/161/2797699140/225589/d34008c6/59e855a5N6539c5a5.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 180,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.0",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 18,
                "name": "SNP 熊猫动物面膜贴 10片/盒 嫩白嫩肤",
                "price": 99.00,
                "privilegePrice": 128.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t4636/150/2567807586/195397/84a288e3/58f08f6dN6e4d3f68.jpg!q70.jpg",
                "details": "https://img20.360buyimg.com/vc/jfs/t4420/82/2561615509/99651/26cf187b/58f03228N816bf65b.jpg;https://img20.360buyimg.com/vc/jfs/t4576/357/2914412627/102245/601e8bcf/58f48268N29c4b295.jpg;https://img20.360buyimg.com/vc/jfs/t4546/61/2903516973/91037/4e0ffab5/58f48268N988c19da.jpg;https://img20.360buyimg.com/vc/jfs/t4504/72/2480847299/100868/6ac17ea5/58f0322bNadf17bec.jpg;https://img20.360buyimg.com/vc/jfs/t5722/225/4553703286/98604/5c7b7ab5/5950ac14N2916289f.jpg;https://img20.360buyimg.com/vc/jfs/t4432/211/2365321936/102059/705ff735/58f0322dNb83b7327.jpg;https://img20.360buyimg.com/vc/jfs/t4654/71/2479480452/70583/4d08c08b/58f0322cNa845be74.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 122,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.7",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 17,
                "name": "韩国 自然乐园（Nature Republic）芦荟胶 300ml 韩国直采",
                "price": 35.00,
                "privilegePrice": 49.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t2269/284/449279584/97279/1bcf80c/560c8fe8Na69a580c.jpg!q70.jpg",
                "details": "https://img20.360buyimg.com/vc/jfs/t3016/342/1393480875/1247220/6863631f/57c42076N35d9bf92.jpg;https://img20.360buyimg.com/vc/jfs/t3271/147/1028349851/1128600/72edba47/57c4207fNbaaae691.jpg;https://img20.360buyimg.com/vc/jfs/t3187/150/1021300626/872012/8f448a94/57c42088N951e9187.jpg;https://img20.360buyimg.com/vc/jfs/t3301/357/1001327127/998159/d997566e/57c42090Nf4f46414.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 70,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.1",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 16,
                "name": "碧然德（BRITA）过滤净水器 新升级Maxtra+滤芯标准版6枚装",
                "price": 135.00,
                "privilegePrice": 180.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t10612/138/1430171340/245025/2d556b52/59e09bcbN10a79d7d.jpg!q70.jpg",
                "details": "https://img10.360buyimg.com/cms/jfs/t13222/31/322143641/297295/36ff29ef/5a092e14N31a2fc1d.jpg;https://img30.360buyimg.com/cms/jfs/t13810/21/341016100/292908/f9f11971/5a092e2bN72b8e545.jpg;https://img10.360buyimg.com/cms/jfs/t11983/28/1638381672/299150/6137b604/5a092e30N86144004.jpg;https://img12.360buyimg.com/cms/jfs/t11152/80/1762432924/301645/40cf6a4a/5a092e33N8f261509.jpg;https://img11.360buyimg.com/cms/jfs/t13003/359/335098958/300660/7abe1160/5a092e37N59563879.jpg;https://img10.360buyimg.com/cms/jfs/t12148/296/344198962/305588/bc4c99df/5a092e3bNbe18cbba.jpg;https://img13.360buyimg.com/cms/jfs/t7936/323/4323192930/296621/fad3ca9a/5a092e3fN3d34ad92.jpg;https://img11.360buyimg.com/cms/jfs/t11146/47/1856621285/299612/81901c44/5a092e43N8d6762ba.jpg;https://img10.360buyimg.com/cms/jfs/t7396/301/4635100158/304891/2d9676ca/5a092e6fN9ce9b10c.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 19,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.5",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 15,
                "name": "朵玺Dr.Douxi赋活新生卵壳膜100g 紧致毛孔 锁水保湿 白色",
                "price": 249.00,
                "privilegePrice": 280.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t15760/240/2364180613/156292/ef903739/5aa1f8d5Ndd42acd3.jpg!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t15274/79/2422919843/349134/17bcd260/5a9e880fNff929e75.jpg;https://img10.360buyimg.com/imgzone/jfs/t17044/228/668258528/204068/838bea39/5a9e880fNaea3579d.jpg;https://img10.360buyimg.com/imgzone/jfs/t18841/260/639063252/306396/137e665f/5a9e8810N06aedfa4.jpg;https://img10.360buyimg.com/imgzone/jfs/t19258/148/662223497/297520/28ff243a/5a9e8810Nf2f538c2.jpg;https://img10.360buyimg.com/imgzone/jfs/t19453/254/653770633/308718/77c99727/5a9e8811Nc19aac86.jpg;https://img10.360buyimg.com/imgzone/jfs/t15340/267/2439419638/355328/e0b26f3f/5a9e8811Na42a7292.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1422,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.9",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 14,
                "name": "资生堂（Shiseido） uno吾诺润肤乳 乳液 温和补水型 160ml",
                "price": 69.00,
                "privilegePrice": 74.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t14245/264/2640031642/90352/2b2d65e6/5ab0d170Na0dbfc6b.jpg!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t18601/100/1488193806/455710/715ee1eb/5acc7dbaN394b07c7.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t4435/24/1347119550/338397/d2f1183b/58dc7f79Nd4a578ff.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t4399/108/1299140071/648400/50847ef3/58dc7f7bN026453ff.jpg;https://img20.360buyimg.com/imgzone/jfs/t18415/357/1511316267/201463/a4c2ea93/5acd6e90Nc695aed4.jpg;https://img30.360buyimg.com/popWareDetail/jfs/t6094/343/4783275113/493381/c64f4fa9/5966ea52N3d199f29.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t4285/139/746539837/193963/2c3f8b8f/58b9381cN4179d716.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 366,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.3",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 13,
                "name": "菲诗小铺（The Face Shop）草本洗面奶 芦荟洁面膏 舒缓保湿 170ml",
                "price": 34.00,
                "privilegePrice": 49.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t17719/147/802204468/122356/6e810e00/5aaa1492N4523d8f5.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/popWaterMark/jfs/t16921/140/728074494/189145/fabe6cc4/5aa23c7fNee473b86.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t19381/269/257490754/133067/e0c9854d/5a66cc62Ncb8808a1.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t18727/262/257641816/43609/c28d03a7/5a66cc62Na35b9f26.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t19234/275/257491352/178454/fbe2242a/5a66cc63N8579e997.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t16444/162/1935726472/177120/4f872b02/5a66cc62Ne8c9f6ca.jpg;",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 597,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "6.9",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 12,
                "name": "雅漾（Avene） 舒护活泉喷雾 300ml 爽肤水 补水保湿舒缓定妆",
                "price": 79.00,
                "privilegePrice": 88.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t19426/169/1079101854/93418/bddfc677/5aba62feN9915aca9.jpg!q70.jpg",
                "details": "https://img30.360buyimg.com/imgzone/jfs/t15778/152/2018388292/283487/78b4226/5a7199abN377c5acc.jpg;https://img13.360buyimg.com/imgzone/jfs/t15307/143/2153811354/528347/bbe080a5/5a7199afN7bbe70c9.jpg;https://img14.360buyimg.com/imgzone/jfs/t15340/321/2146593792/211921/a1ba5559/5a7199b2Ncd635447.jpg;https://img10.360buyimg.com/imgzone/jfs/t15967/323/2029792112/280335/4855c4f6/5a7199b4N9a6efde8.jpg;https://img14.360buyimg.com/imgzone/jfs/t18499/261/398515014/200226/4a7badf5/5a7199b4N36224b7f.jpg;https://img14.360buyimg.com/imgzone/jfs/t14458/223/2150936673/117725/934e5dda/5a7199b4N770eb9ec.jpg;https://img10.360buyimg.com/imgzone/jfs/t15196/226/2168341031/222946/32acabf5/5a7199b7N0f4522e1.jpg;https://img13.360buyimg.com/imgzone/jfs/t17677/313/379268295/86694/904ba8d/5a7199b7Na5e77c0a.jpg\n",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 254,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.0",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 11,
                "name": "韩国进口 蒂佳婷（Dr.Jart+）水动力活力水润面膜25ml*5片/盒",
                "price": 99.90,
                "privilegePrice": 102.50,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t5551/160/329741133/205414/3ac1307/58fdb6a5N68dde194.jpg!q70.jpg",
                "details": "https://img10.360buyimg.com/imgzone/jfs/t4837/126/1458842939/76890/a7ef907e/58f0a2e4Nff3c0aba.jpg;https://img10.360buyimg.com/imgzone/jfs/t4504/150/2557666272/35785/f46a13c7/58f0a2e9N308932a6.jpg;https://img10.360buyimg.com/imgzone/jfs/t4801/250/1450796110/65450/aaafe714/58f0a306Nab80de4f.jpg;https://img10.360buyimg.com/imgzone/jfs/t5284/49/1157123501/91674/aba646af/590c40ccN65851c26.jpg;https://img10.360buyimg.com/imgzone/jfs/t5449/47/1129291465/91044/d2388fc2/590bdfe7N117b6701.jpg;https://img10.360buyimg.com/imgzone/jfs/t4660/38/4268046310/44601/dc55f658/590c4089Nb198ef2b.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 103,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.7",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 10,
                "name": "品牌直采 韩国 捷俊(JAYJUN)水光樱花面膜三部曲25ml 10片/盒",
                "price": 150.00,
                "privilegePrice": 172.50,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t3124/255/8602351009/241617/559927c2/58c899b3N8df4bd72.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/cms/jfs/t17017/2/340545752/172027/27e48839/5a6e88e9Nce1160de.jpg;https://img13.360buyimg.com/cms/jfs/t14668/344/2119312842/177873/384d37a2/5a6e88f0Ned4ec6c6.jpg;https://img30.360buyimg.com/cms/jfs/t18931/364/367076441/98073/4ee13acd/5a6e88f7Ne742e30c.jpg;https://img30.360buyimg.com/cms/jfs/t18766/341/352628783/129184/442b28ec/5a6e88feN3b1d4730.jpg;https://img30.360buyimg.com/cms/jfs/t19456/339/358546634/110763/719b8d65/5a6e8906N286d8766.jpg;https://img10.360buyimg.com/cms/jfs/t15085/282/2032906665/182238/569f4f77/5a6e890eNabd2ced7.jpg;https://img13.360buyimg.com/cms/jfs/t18466/357/345693950/213982/77f33df5/5a6e8916N22aa3a4e.jpg;https://img20.360buyimg.com/cms/jfs/t19513/79/353672782/227873/3ff2ee4f/5a6e8928N04049c5a.jpg;https://img14.360buyimg.com/cms/jfs/t16141/300/1987302595/122333/2ecaa01c/5a6e8930N5d6fd252.jpg;https://img14.360buyimg.com/cms/jfs/t13543/219/2385328042/225589/d34008c6/5a6e893fNf0560a14.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 46,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.7",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 9,
                "name": "韩国 美迪惠尔(Mediheal) 可莱丝 N.M.F针剂水库面膜贴10片/盒 ",
                "price": 109.00,
                "privilegePrice": 118.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t15052/115/2139262461/423349/5957e91f/5a712387N0365d980.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img10.360buyimg.com/imgzone/jfs/t17545/197/418825931/103385/d0e303f0/5a742eb2Nc1421032.jpg;https://img10.360buyimg.com/imgzone/jfs/t18136/283/404256508/300888/436357fe/5a742eb2N8499ed83.jpg;https://img10.360buyimg.com/imgzone/jfs/t16789/337/414130656/298203/7d33cfb7/5a742eb3Nf4153453.jpg;https://img10.360buyimg.com/imgzone/jfs/t17578/18/409122228/224890/6ab90be6/5a742eb2N894426b2.jpg;https://img10.360buyimg.com/imgzone/jfs/t16696/347/430880407/17875/f0fa9615/5a742eb2Nbca4e689.jpg;https://img14.360buyimg.com/cms/jfs/t11032/271/1584395193/57051/a878fd8/5a043166N881eb0c9.jpg;https://img20.360buyimg.com/cms/jfs/t13240/263/5509684/245444/712e644/5a018433N8469d2b1.jpg;https://img10.360buyimg.com/cms/jfs/t12544/274/7251752/305141/5f03d2f4/5a018436N11ec41e5.jpg;https://img11.360buyimg.com/cms/jfs/t14026/244/7105757/296438/9f8b0330/5a018435Nb2209323.jpg;https://img14.360buyimg.com/cms/jfs/t13528/244/7720805/205355/5cd86d41/5a018433N937a3a6f.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 36,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.2",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 8,
                "name": "韩国爱茉莉 兰芝(Laneige) 气垫隔离防晒 BB霜15g*2",
                "price": 279.00,
                "privilegePrice": 320.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t19285/285/1134361100/143022/a11e2ceb/5abde9b7Ndadbb0dd.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/cms/jfs/t7603/168/1586589786/198347/9c60f7bb/599e2ceeN07662657.jpg;https://img13.360buyimg.com/cms/jfs/t7603/182/1560648931/99181/4814ac9e/599e2cedNf522bb5a.jpg;https://img30.360buyimg.com/cms/jfs/t7714/201/1585056903/139367/cdb046c5/599e2ceeNe752824b.jpg;https://img11.360buyimg.com/cms/jfs/t7792/164/1578503490/79823/28dc4de3/599e2ce4Ncd46d39e.jpg;https://img30.360buyimg.com/cms/jfs/t7546/9/1590956286/60907/9bed04a9/599e45c8N925c7879.jpg;https://img13.360buyimg.com/cms/jfs/t7930/73/1569418812/218603/41c00c70/599e2cdbN5e2d8d0b.jpg;https://img20.360buyimg.com/cms/jfs/t7648/219/1641255617/202693/291554a6/599e2ceeN076e36e0.jpg;https://img10.360buyimg.com/cms/jfs/t7597/176/1573538171/107982/c6734086/599e2ceeN6b2758c2.jpg\n",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 136,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.7",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 7,
                "name": "日本城野医生Dr.Ci.Labo毛孔细致化妆水100ml/瓶",
                "price": 85.00,
                "privilegePrice": 89.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t18067/352/1303510983/58673/cf7b2280/5ac4cff1N63f73a22.jpg!q70.jpg",
                "details": "https://img11.360buyimg.com/cms/jfs/t16906/54/833236005/285759/a76b529c/5aab7897N99b5ff48.jpg;https://img10.360buyimg.com/imgzone/jfs/t15508/352/1652696048/105724/c31328ca/5a583251N697ca464.png;https://img10.360buyimg.com/imgzone/jfs/t16048/81/1438197820/113734/98e09ca/5a583251N982ede7e.png;https://img10.360buyimg.com/imgzone/jfs/t17359/171/21457964/229892/63ac5339/5a583252Nffc86622.png;https://img10.360buyimg.com/imgzone/jfs/t18445/363/19488915/114532/7c718ac7/5a583252N5e711663.png;https://img10.360buyimg.com/imgzone/jfs/t16024/251/1629757050/165967/1f46986c/5a583252Ne988de2a.png;https://img10.360buyimg.com/imgzone/jfs/t19456/351/18597451/130829/b2312ada/5a583252Nbfbcdaad.png;https://img10.360buyimg.com/imgzone/jfs/t16723/358/25683295/60168/4cbca657/5a58324fNe91693c3.png;https://img10.360buyimg.com/imgzone/jfs/t18712/275/1283423874/84742/cffa4517/5ac202ddN752e0532.jpg;https://img10.360buyimg.com/imgzone/jfs/t18982/99/1234677650/108066/4e586e7e/5ac202e3N27e086e8.jpg;https://img10.360buyimg.com/imgzone/jfs/t18604/88/1216756183/91530/8ee5a8b0/5ac202e8N1c959bf7.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 213,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.6",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 6,
                "name": "蜜浓MINON保湿氨基酸化妆水干燥肌1号清爽型150ml",
                "price": 120.00,
                "privilegePrice": 134.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t11317/136/1884111176/211775/3542f11f/5a0ea60dNbda1e1b2.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t13423/77/599425883/227205/b686f603/5a0ea625N8bed3a2f.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t13813/67/549698794/288838/f1e40476/5a0ea625N037d736d.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t11137/246/2037892138/241468/d9a835ac/5a0ea623Na6078b08.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t12652/18/570642179/135879/fcbd068e/5a0ea625N6e8a3c30.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 87,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "9.0",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 4,
                "name": "狮王（LION）足贴休足时间腿部按摩贴 18枚装",
                "price": 58.00,
                "privilegePrice": 69.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t19429/296/228039148/225880/ded60256/5a6555c3N9dbb115f.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img10.360buyimg.com/imgzone/jfs/t15175/199/2248157393/595853/8bc34fb9/5a7f9ad8Nab2a058a.jpg;https://img10.360buyimg.com/imgzone/jfs/t15919/198/2111453949/332017/e3305f48/5a7f9ad8N6dcdfa48.jpg;https://img10.360buyimg.com/imgzone/jfs/t18748/11/485020002/476277/a5165732/5a7f9ad8N3e947904.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 802,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.4",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 5,
                "name": "日本 KOSE 高丝 Softymo 卸妆油/卸妆乳啫喱 温和型卸妆油 230mL",
                "price": 55.00,
                "privilegePrice": 64.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t18610/76/237290611/158630/3e18be33/5a65b300N1c9655b0.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t19450/229/492270126/703676/15d6f3df/5a7fb806N6a7d57c3.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t19150/228/500504275/437763/365ed16/5a7fb805Ne22c7f21.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 242,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.6",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 3,
                "name": "日本肌美精（Kracie）3D浸透高保湿补水面膜4片/盒（玫红）",
                "price": 60.00,
                "privilegePrice": 81.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t12682/83/568380680/582254/a6481400/5a0e8e23Nc9175fe5.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t11434/316/2014606650/429795/65aa49a9/5a0e8e57N9dcafb7b.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t13564/216/573238045/312020/520e1cc6/5a0e8e2eNce0011c3.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t14155/191/564000039/355656/1af845be/5a0e8e57N69a2c7fa.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t13738/205/551957394/367934/5a1c4046/5a0e8e54N0cf8650e.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t14074/213/560401806/495535/e8d3f7dd/5a0e8e47Nd5aeb138.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1150,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "7.4",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 2,
                "name": "日本MINON氨基酸保湿清透面膜 敏感干燥肌肤4片装",
                "price": 70.00,
                "privilegePrice": 79.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t9673/329/1417107173/307150/652b84da/59e04a12N3ff644f7.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/popWareDetail/jfs/t7303/110/2499776167/1315871/adc54d2f/59b0c407Nba790691.jpg;https://img30.360buyimg.com/popWareDetail/jfs/t7891/36/2579605999/2038887/dc6e5dd/59b0c407Nc3c7b7e2.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1039,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.9",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            },
            {
                "id": 1,
                "name": "日本资生堂（Shiseido）洗颜专科洗面奶洁面乳120ml",
                "price": 49.00,
                "privilegePrice": 56.00,
                "imgUrl": "https://m.360buyimg.com/n12/jfs/t18736/261/941932619/72745/c6e929e3/5ab05c6fN30744488.jpg!q70.jpg",
                "details": "https://img14.360buyimg.com/cms/jfs/t12343/316/887057782/88519/4f284e41/5a150e8aN196a8ddf.jpg;https://img30.360buyimg.com/popWareDetail/jfs/t7519/163/2579412574/2717557/15183116/59b25453N4b18df13.png;https://img30.360buyimg.com/popWaterMark/jfs/t7903/192/2911505409/810278/276f63e/59e019a5N44f1daa3.jpg;https://img30.360buyimg.com/popWaterMark/jfs/t7903/192/2911505409/810278/276f63e/59e019a5N44f1daa3.jpg",
                "remark": None,
                "createDate": None,
                "updateDate": None,
                "clickRate": 1469,
                "buyRate": 0,
                "stock": 0,
                "isHot": "0",
                "isNew": "1",
                "classifyId": None,
                "discount": "8.8",
                "activityId": None,
                "shopGoodsImageList": None,
                "desc": None
            }
    ]

table_name='mall_goods'
def close():
    cur.close()
    conn.close()

def data_init():
    cur.execute('DELETE FROM %s'%(table_name))
    for mydict in mylist:
        placeholders  = ','.join(['?']*len(mydict))
        # print(placeholders )
        # values = tuple(x for x in mydict.values())
        # print(values)
        sql = 'INSERT INTO %s values(%s)'%(table_name,placeholders)
        cur.execute(sql,tuple(mydict.values()))
    conn.commit()

def query(statement):
    cur.execute(statement)
    data = cur.fetchall()
    #cur.close()
    return data

#data_init()

rows = query('SELECT count(1) as row_count FROM mall_goods')
print(rows)

path = os.getcwd()
print(path)
path = os.path.abspath('.')
print(path)
dbfile = os.path.join(path,'workblog.db')
print(dbfile)
# files = os.listdir(path)
#



from sqlalchemy import exists,Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()



""" 
class MallGoods(Base):
    '商品类'
    __tablename__ = 'mall_goods'
    id = Column(Integer, primary_key=True)
    name= Column(String(128))
    privilegePrice = Column(Numeric(10,2))
    price = Column(Numeric(10,2))
    imgUrl = Column(String(256))
    details = Column(String(512))
    remark= Column(String(128))
    createDate = Column(DateTime, default=func.now())
    updateDate = Column(DateTime, default=func.now())
    clickRate= Column(Integer)
    buyRate= Column(Integer)
    stock= Column(Integer)
    isHot= Column(Integer)
    isNew= Column(Integer)
    classifyId= Column(Integer)
    discount = Column(Numeric(10,2))
    activityId= Column(Integer)
    desc= Column(String(128))
    shopGoodsImageList= Column(String(512))
 """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///' + dbfile)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

s = session()

def init_db():
  Base.metadata.create_all(engine)
 
 
def drop_db():
  #Base.metadata.drop_all(engine)
  pass
 
def init_data():
    IT = Department(name="IT")
    emp1 = Employee(name="John", department=IT)
    emp2 = Employee(name="Mike", department=IT)
    emp3 = Employee(name="Tom", department=IT)
    emp4 = Employee(name="Susan", department=IT)
    emp5 = Employee(name="Wanglin", department=IT)
    emp6 = Employee(name="Simon", department=IT)

    Financial = Department(name="Financial")
    emp11 = Employee(name="Cathy", department=Financial)
    emp12 = Employee(name="Marry", department=Financial)
    emp13 = Employee(name="Jack", department=Financial)
    emp14 = Employee(name="Jame", department=Financial)
    emp15 = Employee(name="Shirley", department=Financial)
    emp16 = Employee(name="Anne", department=Financial)

    Market = Department(name="Market")
    emp21 = Employee(name="Billy", department=Market)
    emp22 = Employee(name="Eric", department=Market)
    emp23 = Employee(name="Alan", department=Market)
    emp24 = Employee(name="张大山", department=Market)
    emp25 = Employee(name="陈永生", department=Market)
    emp26 = Employee(name="朱国庆", department=Market)

    s = session()
    s.add(IT)
    s.add(emp1)
    s.add(emp2)
    s.add(emp3)
    s.add(emp4)
    s.add(emp5)
    s.add(emp6)
    dept_list=[Financial,Market]
    emp_list=[emp11,emp12,emp13,emp14,emp15,emp16,emp21,emp22,emp23,emp24,emp25,emp26]
    s.add_all(dept_list)
    s.add_all(emp_list)
    s.commit() 

# 查询是否存在 结果是布尔值
it_exists = session.query(
    exists().where(Employee.id == '3')
  ).scalar()
 # 改 更新数据
  # 数据更新，将值为Mack的serviceDesc修改为Danny
update_obj = session.query(Employee).filter(Employee.name == 'Mack').update({"remark": "update remark"})
# 或则
update_objp = session.query(Employee).filter(Employee.name == 'Mack').first()
update_objp.remark = 'update remark'
session.commit()

# 删除
update_objk = session.query(Employee).filter(Employee.name == 'Mack').delete()
# 或则
update_objkp = session.query(Employee).filter(Employee.name == 'Mack').one()
update_objkp.delete()
session.commit()


results = s.query(Department).filter(Department.name.like('%{0}%'.format('IT'))).all()
print(type(results))
for d in results:
    print(d.__dict__)


e=s.query(Employee).join(Employee.department).filter(Employee.name.startswith('C'), Department.name == 'Financial').all()[0]
print(e.__dict__)

d=s.query(Department).filter(Department.employees.any(Employee.name == 'John')).all()[0]
print(d.__dict__)

#engine = create_engine("mysql://user:password@hostname/dbname?charset=utf8")



#def query(id=None,classifyId=None,name=None):
#query=session.query(Employee).filter(Employee.name.like('%{0}%'.format(name)))
#query.all()
 
# 打印类型和对象的name属性:
#print('type:', type(qry))


# 关闭Session:
#session.close()



