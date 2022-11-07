# qrcode library needed, install it with: pip install qrcode Image
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 3,
        # restore data if the code is dirty or damaged
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 1,
    )
    # QR Code Error Corection Capability
    # Level L - 7%
    # Level M - 15%
    # Level Q - 25%
    # Level H - 30%

    qr.add_data(text)
    qr.make(fit=True)
    # The make function with (fit=True) ensures that the entire dimension of the QR Code is utilized, 
    # even if our input data could fit into less number of boxes
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_img.png")

# Image is saved into Home directory (Linux)
url = input("Enter yout URL: ")
generate_qrcode(url)
print("Image is saved in your home directory!")