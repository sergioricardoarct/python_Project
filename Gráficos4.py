import matplotlib.pyplot as plt

# valores base dos dados #
x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 2, 4, 7, 8, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]

# graficos

plt.bar(x1, y1, label="Área A", color='g')
plt.bar(x2, y2, label="Terrenos B", color='b')
plt.plot()

plt.xlabel("Região Propicia")
plt.ylabel("Número de clientes")
plt.title("Comparativo de desejo entre empresas e clientes")
plt.legend()
plt.show()

