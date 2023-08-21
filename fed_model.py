#Fed Model
import matplotlib.pyplot as plt
import openpyxl
path = "/Users/macbook/desktop/GF-FedModel/data.xlsx"

x_data = []
nominal_yield = []
earnings_yield = []
name = "Fed Model by Day"
def readData(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for i in range(11,sheet.max_row +1):
        cell1 = sheet.cell(row = i, column = 2)
        cell2 = sheet.cell(row = i, column = 3)
        if (int(cell1.value)==0 or int(cell2.value)==0):
            continue
        else:
            nominal_yield.append(float(cell1.value))
            earnings_yield.append(100.0/(float(cell2.value)))

def readWeek(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for i in range(11,sheet.max_row +1,7):
        cell1 = sheet.cell(row = i, column = 2)
        cell2 = sheet.cell(row = i, column = 3)
        count = 0
        while (int(cell1.value)==0 or int(cell2.value)==0):
            count+=1
            cell1 = sheet.cell(row = i+count,column = 2)
            cell2 = sheet.cell(row = i+count,column = 3)
        
        nominal_yield.append(float(cell1.value))
        earnings_yield.append(100.0/(float(cell2.value)))
    name = "Fed Model by Week"

def readMonth(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for i in range(11,sheet.max_row +1,30):
        cell1 = sheet.cell(row = i, column = 2)
        cell2 = sheet.cell(row = i, column = 3)
        count = 0
        while (int(cell1.value)==0 or int(cell2.value)==0):
            count+=1
            cell1 = sheet.cell(row = i+count,column = 2)
            cell2 = sheet.cell(row = i+count,column = 3)
        
        nominal_yield.append(float(cell1.value))
        earnings_yield.append(100.0/(float(cell2.value)))
    name = "Fed Model by Month"

def readYear(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for i in range(11,sheet.max_row +1,365):
        cell1 = sheet.cell(row = i, column = 2)
        cell2 = sheet.cell(row = i, column = 3)
        count = 0
        while (int(cell1.value)==0 or int(cell2.value)==0):
            count+=1
            cell1 = sheet.cell(row = i+count,column = 2)
            cell2 = sheet.cell(row = i+count,column = 3)
        
        nominal_yield.append(float(cell1.value))
        earnings_yield.append(100.0/(float(cell2.value)))
    name = "Fed Model by Year"

readWeek(path)
x_data = [i for i in range(1,len(earnings_yield)+1)]

plt.figure()
plt.plot(x_data, nominal_yield, label='Treasury Bonds', color='blue')
plt.plot(x_data, earnings_yield, label='CSI 300', color='red')
plt.xlabel('Time(2013.8.15 - 2023.8.15)')
plt.ylabel('Rate %')
plt.title(name)
plt.legend()
plt.show()

# print(len(nominal_yield))
# print(len(earnings_yield))

# print(x_data)

# print(earnings_yield)

#243





