import qrcode

dado = 'Bem vindo ao Python'

qr = qrcode.QRCode(version=1, box_size=20, border=5)
qr.add_data(dado)

qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

img.save('A:\Programação Geral\Python 2022\qrc.png')
