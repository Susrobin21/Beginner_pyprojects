import qrcode


def gen_qrcode(word) :

    code = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 9,
        border = 4,
    )
    code.add_data(word)
    code.make(fit= True)
    img = code.make_image(fill_color = 'white', back_color = 'black')
    img.save('qrimg.png')

gen_qrcode('https://aniwatch.to/')
