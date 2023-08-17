#Fed Model
import matplotlib.pyplot as plt
import openpyxl
path = "/Users/macbook/desktop/GF-FedModel/data.xlsx"

x_data = []
nominal_yield = []
earnings_yield = []

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
            earnings_yield.append(1.0/(float(cell2.value)))

readData(path)
x_data = [i for i in range(1,len(earnings_yield)+1)]


plt.figure()
plt.plot(x_data, nominal_yield, label='Treasury Bonds', color='blue', marker='o')
plt.plot(x_data, earnings_yield, label='CSI 300', color='red', marker='x')
plt.xlabel('Time(2013.8.15 - 2023.8.15)')
plt.ylabel('Rate %')
plt.title('Fed Model')
plt.legend()
plt.show()






