import pymysql



class mysql_:
    def __init__(self):
        self.sql_connect = pymysql.connect(user='root',password='123456',host='localhost',db='ASer')

    def get_minister(self):
        cor = self.sql_connect.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select * from minister '
        cor.execute(sql)
        #../static/images/none.png
        res = cor.fetchall()
        print(res)
        return res
    def insert_news(self):
        insert_sql = 'INSERT INTO anime_news (name,content) VALUES (%s,%s)'
        name = 'U35「白沙的水族馆」新绘公开'
        content = '''<section class="atl">
              <div class="article">
 <div class="hd">
  <h1 class="title">
   U35「白沙的水族馆」新绘公开
  </h1>
  <div class="info">
   <span class="tag">
    动漫
   </span>
   <span class="author">资讯速递</span>
   <span class="ico">
    ▪
   </span>
   <span class="time">
    2021-11-12 12:01:40
   </span>
  </div>
 </div>
 <div class="bd">
<p>原文出处：<a rel="nofollow" href="http://acg.178.com/202111/430689700026.html" target="_blank">http://acg.178.com/202111/430689700026.html</a></p>

  <p>
   近日，TV动画「白沙的水族馆」角色原案的插画师U35老师公开了最新绘制。
  </p>
  <p style="text-align:center">
   <img alt="" referrerpolicy="no-referrer" src="https://pic.rmb.bdstatic.com/bjh/1d3853c9962f4fe38ba861240da88f45.jpeg"/>
  </p>
  <p>
   同时，插画师U35老师还公开了第19话的应援绘。
  </p>
  <p style="text-align:center">
   <img alt="" referrerpolicy="no-referrer" src="https://pic.rmb.bdstatic.com/bjh/2c4b2ae5a268b22969f1f212806b55a2.jpeg"/>
  </p>
  <p>
   「白沙水族馆」以冲绳南城市的一家将要闭馆的海洋馆为舞台，讲述了代理馆长海咲野括和在东京失去了梦想的原偶像宫泽风花相遇后发生的故事。
  </p>
 </div>
</div>

            </section>
'''
        cor = self.sql_connect.cursor()
        try:
            cor.execute(insert_sql, [name, content])
            self.sql_connect.commit()
        except:
            self.sql_connect.rollback()
        cor.close()

if __name__=='__main__':
    con = mysql_()
    con.insert_news()