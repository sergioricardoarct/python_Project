import matplotlib.pyplot as plt

# valores base dos dados #
x = [2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 2, 8, 3, 7, 4, 6, 5]

# graficos basico

plt.plot(x, y, 'b--', color='yellow')
plt.scatter(x, y, marker="*", color='black')

plt.title('Ganhos em dezembro')
plt.xlabel('Quantidade de produtos')
plt.ylabel('Quantidade de vendas')

plt.show()