

def main():
	result_arquivo = open("../data/ListaMacrofitasResult.csv", 'r')#eles forneceram
	flora_arquivo = open("../data/floraDoBrasil.csv")#obtida da api
	plant_arquivo = open("../data/plantList.csv")#obtida da api

	final_result = open("../data/result.csv", 'w')

	list_result = []
	list_flora = []
	list_plant = []

	for name in result_arquivo:
		list_result.append(name.split('\n')[0])

	for line in flora_arquivo:
		list_flora.append(line)

	for line in plant_arquivo:
		list_plant.append(line)


	for i in range(0, len(list_result)):
		for j in range(0, len(list_flora)):
			name = list_flora[j].split(',')[0]
			tipo = list_flora[j].split(',')[1]
			if tipo == "SINONIMO":
				sinonimo = list_flora[j].split(',')[2]

			if list_result[i] == name and tipo == "NOME_ACEITO":
				list_result[i] = list_result[i] + " ok"
				final_result.write(list_result[i] + '\n')
				break
			elif list_result[i] == name and tipo == "SINONIMO":
				list_result[i] = list_result[i] + "," + sinonimo
				final_result.write(list_result[i] + '\n')
				break





if __name__ == '__main__':
	main()
