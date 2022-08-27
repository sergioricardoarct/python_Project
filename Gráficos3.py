import matplotlib.pyplot as plt

# valores base dos dados #
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]

# graficos basico

plt.plot(x, y2, color='red', label='Item')
plt.plot(x, y1, color='black', label='Variação')
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.title('Ganhos em dezembro')
plt.xlabel('Quantidade de produtos')
plt.ylabel('Quantidade de vendas')

plt.legend()
plt.show()