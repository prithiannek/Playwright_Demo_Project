import openpyxl


class NewExcelReader:

    def read_excel_cell(self, row_no, col_no):
        book = openpyxl.load_workbook('C:\\Users\\HP\\Downloads\\Python Data_Login.xlsx')
        sheet = book["login_credentials"]
        return sheet.cell(row=row_no, column=col_no).value