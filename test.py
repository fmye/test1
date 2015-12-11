# -*- coding: utf-8 -*-
__author__ = 'yey'
import xlrd;
import xlwt;
import sys;
import datetime;
from xlutils.copy import copy;
from xlwt import *
reload(sys)
sys.setdefaultencoding('utf-8')

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER

styleBoldRed   = xlwt.easyxf('font: color-index red ,height 180');
styleBoldRed.alignment=alignment
styleBoldGreen   = xlwt.easyxf('font: color-index green ,height 180');
styleBoldGreen.alignment=alignment
headerRedStyle = styleBoldRed;
headerGreenStyle = styleBoldGreen;
headerDateStyle = xlwt.XFStyle()
headerDateStyle.num_format_str = 'YYYY-MM-DD'

#wb = xlwt.Workbook();
#ws = wb.add_sheet('sheetName');
#ws.write(0, 0, "Col1",        headerStyle);
#ws.write(0, 1, "Col2", headerStyle);
#ws.write(0, 2, "Col3",    headerStyle);
#wb.save('fileName.xls');

#open existed xls file

oldWb = xlrd.open_workbook("C:\Users\yey\Desktop\dfcf.xls", formatting_info=True);
oldWbS = oldWb.sheet_by_index(0)
newWb = copy(oldWb);
newWs = newWb.get_sheet(0);
inserRowNo = 2
newWs.write(inserRowNo, 0, "value1");
newWs.write(inserRowNo, 1, "value2");
newWs.write(inserRowNo, 2, "value3");
newWs.write(inserRowNo, 3, "value1");
newWs.write(inserRowNo, 4, "value2");
newWs.write(inserRowNo, 5, "value3");
newWs.write(inserRowNo, 6, "value1");
newWs.write(inserRowNo, 7, "value2");
newWs.write(inserRowNo, 8, "value3");
newWs.write(inserRowNo, 9, "value1");
newWs.write(inserRowNo, 10, "value2");
newWs.write(inserRowNo, 11, "value3");
newWs.write(inserRowNo, 12, "value1");
newWs.write(inserRowNo, 13, "value2");
newWs.write(inserRowNo, 14, "value3");



first_col=newWs.col(0)       #xlwt中是行和列都是从0开始计算的
first_col.width=128*20

for rowIndex in range(inserRowNo, oldWbS.nrows):
    for colIndex in range(oldWbS.ncols):
        print(str(oldWbS.cell(rowIndex, colIndex).value).find ('-'))
        if 0==colIndex:
            print(datetime.datetime.now())
            newWs.write(rowIndex + 1, colIndex, datetime.datetime.now(), headerDateStyle);
            print(datetime.datetime.now())
        else:
            if 0==str(oldWbS.cell(rowIndex, colIndex).value).find ('-'):
                    newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value, headerRedStyle);
            else:
                     newWs.write(rowIndex + 1, colIndex, oldWbS.cell(rowIndex, colIndex).value, headerGreenStyle);
newWb.save('C:\Users\yey\Desktop\dfcf.xls');
print "save with same name ok";