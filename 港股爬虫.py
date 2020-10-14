from bs4 import BeautifulSoup
from urllib import request
import xlwt
value=1
while value <= 98:
    value0 = str(value)
    url = "http://www3.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY_C.HTM "
    response = request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')

    # 内容处理
    content = bs.find_all('td')
    data_list_content = []
    for data in content:
        data_list_content.append(data.text.strip())
    new_list = [data_list_content[i:i + 16] for i in range(0, len(data_list_content), 16)]

    # 存入excel表格
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)


    i = 1
    for list in new_list:
        j = 0
        for data in list:
            sheet1.write(i, j, data)
            j += 1
        i += 1

    # 文件保存
    book.save('sum.xls')
    print("写入完成！")
    print("全部完成")
