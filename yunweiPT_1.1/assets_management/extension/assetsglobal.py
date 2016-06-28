#!/usr/bin/env python
#coding:utf8
from django.utils.safestring import mark_safe

def Init(page):
    try:
        default = int(page)
    except Exception,e:
        default = 1
    return default


#中间获取关键参数
class getitems(object):
    def __init__(self,currentpage,totalt,row=10):
        self.__page = currentpage
        self.__row = row
        self.__total = totalt

    def From(self):
        items = (self.__page - 1) * self.__row
        itemsfrom = items
        return itemsfrom


    def To(self):
        itemsto = self.__page * self.__row
        return itemsto

    def totalpage(self):
        Page01 = divmod(self.__total,self.__row)
        if Page01[1] > 0:
            totalpage = Page01[0] + 1
        else:
            totalpage = Page01[0]
        return totalpage



def getmark(url,totalpage,currentpage):

    #总页数小于等于11

    #总页数大于11
        #当前页小于等于5
        #当前页大于5
    if totalpage <= 11:
        Begin =1
        End = totalpage + 1
    else:
        if currentpage <= 5:
            Begin =1
            End = 12
        elif currentpage >= 5 and (currentpage + 7) <= totalpage:
            Begin = currentpage - 4
            End = currentpage + 7
        else:
            Begin = totalpage - 10
            End = totalpage + 1

    if currentpage > 1:
        uppage = currentpage - 1
    else:
        uppage = 1

    if currentpage < totalpage:
        downpage = currentpage + 1
    else:
        downpage = currentpage

    Mark = """<nav>
  <ul class="pagination">
    <li>
      <a href="%s%d" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    """% (url,uppage)
    for items in xrange(Begin,End):
        if items == currentpage:
            Mark = Mark + '<li class="active"><a href="%s%d">%s</a></li>'% (url,items,items)
        else:
            Mark = Mark + '<li><a href="%s%d">%s</a></li>'% (url,items,items)
    Mark = Mark + """<li>
      <a href="%s%d" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
        """% (url,downpage)
    #mark_safe把字符串转为html可以真接被认别
    return mark_safe(Mark)