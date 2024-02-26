import iometa

doc = Document.getCurrentDocument()
symbol_file = doc.askFile("File", ".txt", False)

doc.log("start restore symbol…")
io_meta = iometa.ParseIOMeta(symbol_file)
objects = io_meta.getObjects()

for obj_value in objects.values():
    for obj in obj_value:
        if type(obj) is list:
            for symbol in obj:
                name = symbol['name']
                methodAddr = symbol['methodAddr']
                doc.setNameAtAddress(methodAddr, name)

doc.log("end restore symbol…")
