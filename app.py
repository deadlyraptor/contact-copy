import xlrd
import xlwt
import settings

wb = xlrd.open_workbook(settings.location)
sh = wb.sheet_by_index(0)
total_rows = sh.nrows
first_row = 6


class Column():
    def __init__(self, col, caps):  # col = column number, caps = True or False
        self.col = col
        self.caps = caps

c = Column(2, True)  # first name
b = Column(1, True)  # last name
d = Column(3, False)  # email
k = Column(10, False)  # Address 1
l = Column(11, False)  # Address 2
m = Column(12, True)  # City
n = Column(13, False)  # State
o = Column(14, False)  # Zip
p = Column(15, False)  # Phone

classes = [c, b, d, k, l, m, n, o, p]


def copy(variable):
    rowx = 6
    colx = variable.col
    temp_list = []
    for row in range(first_row, total_rows):
        if not sh.cell_value(rowx, colx=4):
            rowx += 1
        else:
            temp_list.append(sh.cell_value(rowx, colx))
            rowx += 1
    if variable.caps:
        final_list = [name.capitalize() for name in temp_list]
        # print('The capitalized list printed.')
        # print(final_list)
        return final_list
    else:
        # print('The temp_list printed.')
        # print(temp_list)
        return temp_list

for item in classes:
    copy(item)


book = xlwt.Workbook()
sheet = book.add_sheet('Email Adds')


def wfname():
    first_names = firstName()
    column_number = 0
    for row_number, item in enumerate(first_names):
        sheet.write(row_number, column_number, item)


def wlname():
    last_names = lastName()
    column_number = 1
    for row_number, item in enumerate(last_names):
        sheet.write(row_number, column_number, item)


def wemail():
    emails = email()
    column_number = 2
    for row_number, item in enumerate(emails):
        sheet.write(row_number, column_number, item)

wfname()
wlname()
wemail()

book.save('Email Adds.xls')
