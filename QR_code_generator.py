import qrcode

data = input("Enter the data or link to generate QR: ")

qr = qrcode.QRCode(
    version=1,   #controls how dense the qr is
    error_correction=qrcode.constants.ERROR_CORRECT_L,   #how much damage the code can handle
    box_size=10,  #size of each small square
    border=4,
)

qr.add_data(data)
qr.make(fit=True)  #generates the internal QR structure

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr.png")

print("✅ QR Code saved as my_qr.png")
