import pyqrcode
import png
from pyzbar.pyzbar import decode
from PIL import Image

banner = """
:'#######::'########::'########::'#######:::'#######::'##::::::::'######::
'##.... ##: ##.... ##:... ##..::'##.... ##:'##.... ##: ##:::::::'##... ##:
 ##:::: ##: ##:::: ##:::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ##:::..::
 ##:::: ##: ########::::: ##:::: ##:::: ##: ##:::: ##: ##:::::::. ######::
 ##:'## ##: ##.. ##:::::: ##:::: ##:::: ##: ##:::: ##: ##::::::::..... ##:
 ##:.. ##:: ##::. ##::::: ##:::: ##:::: ##: ##:::: ##: ##:::::::'##::: ##:
: ##### ##: ##:::. ##:::: ##::::. #######::. #######:: ########:. ######::
:.....:..::..:::::..:::::..::::::.......::::.......:::........:::......:::
ver. 0.1

Code by  : Bang Hans
Greet    : GreyMedia.ID
Github   : https://www.github.com/GreyMediaID
"""

def createQR(val, imgname):
    qr_gen = pyqrcode.create(val)
    qr_gen.png(imgname+'.png', scale=5)

def decodeQR(imgname):
    img = decode(Image.open(imgname))
    print(img[0].data.decode('ascii'))

def main():
    print(banner)
    print("""
    Menu:
    1.) Create QR code
    2.) Read QR code
    3.) Exit""")
    choose = int(input(">"))
    if choose == 1:
        val = str(input('Masukan Value (link/txt)> '))
        imgname = str(input('\nSave gambar dengan nama (nama_file.png)\n> '))
        createQR(val, imgname)
    elif choose == 2:
        imgname = str(input("Masukan nama file yang ingin di baca QR codenya\n>"))
        decodeQR(imgname)
    elif choose == 3:
        print("Terimakasih...")
    else:
        print("Maaf, command/pilihan yang anda masukan tidak ada dalam list...")

main()