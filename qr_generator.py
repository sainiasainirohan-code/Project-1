import qrcode
data = "https://1drv.ms/i/c/8d0aa61786a6db0d/IQByNcBkJeiWQYcZ9Z7nVKQxAeLb6xg9jT_5uH4ColDlROQ?e=MkEpiV"
img = qrcode.make(data)
img.save("basic_qr.png")
img.show()