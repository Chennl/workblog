from zipfile import ZipFile
import os
with ZipFile('c:/users/chennl/downloads/nginx-1.18.0.zip','r') as zf:
 
    for zi in zf.infolist():
        print(zi.filename,zi.compress_type)
        fn = os.path.basename(zi.filename)
        if  fn == 'nginx.conf':
            content = zf.read(zi.filename)
            print(content.decode('utf8'))
    zf.close()
