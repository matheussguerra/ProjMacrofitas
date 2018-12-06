import pandas as pd

def xlsxToCsv(path):
	data_xlsx = pd.read_excel(path, index_col=None)
	data_xlsx.to_csv(path[0:-5] + ".csv", encoding='utf-8', index=False)


def main():
	xlsxToCsv("data/ListaMacrofitas.xlsx")

	ref_arquivo = open("data/ListaMacrofitas.csv", 'r')
	result_arquivo = open("data/ListaMacrofitasResult.csv", 'w')

	for linha in ref_arquivo.readlines():
		especie = linha.split()
		result_arquivo.writelines(especie[0] + " " + especie[1] + "\n")

	ref_arquivo.close()
	result_arquivo.close()


if __name__ == '__main__':
	main()
