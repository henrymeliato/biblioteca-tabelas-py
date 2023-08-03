import openpyxl

book = openpyxl.Workbook()

book.create_sheet('CIDADES') #para criar uma página

cidade_page = book['CIDADES'] #selecionar a página
cidade_page.append(['Três Corações', 'Santana', '75 mil'])
cidade_page.append(['Varginha', 'Santana', '110 mil'])


book.save('Planilha de cidades.xlsx')