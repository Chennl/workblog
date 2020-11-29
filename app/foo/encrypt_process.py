

# conding = gbk
# python version 3.8.6
# pycryptodome进行RSA生成公钥、私钥，加密、解密、签名、验签

import hashlib
#这个模块包含了符合 FIPS（美国联邦信息处理标准）的安全哈希算法，包括 SHA1，SHA224，SHA256，SHA384，SHA512 以及 RSA 的 MD5 算法。

##例子1  md5 哈希 
def hash_md5():
    md5 = hashlib.md5()
    md5.update(b'My name is chennl')
    #binary   b'\xd0\xb3\xdd\t\xd5\xf9\xcb4\xe2b7\x15\xf6uR\xa5'
    md5.digest()
    #hexstring  'd0b3dd09d5f9cb34e2623715f67552a5'
    md5.hexdigest()

    ## sha1 哈希
    sha = hashlib.sha1(b'Hello Python').hexdigest()
    print(sha)
    #'422fbfbc67fe17c86642c5eaaa48f8b670cbed1b'


#密钥导出  
#例子2 使用 SHA-256 加密方法对密码进行哈希
import binascii

def hash_sha256():
    dk = hashlib.pbkdf2_hmac(hash_name='sha256',
            password=b'@Thisispasswordsha256!', 
            salt=b'my_random_salt!', 
            iterations=100000)
    binascii.hexlify(dk)
    #b'6e97bad21f6200f9087036a71e7ca9fa01a59e1d697f7e0284cd7f9b897d7c02'

#PyCryptodome   linux: pip install pycryptodome   windows: pip install pycryptodomex
#例子1: 使用 DES 算法来加密一个字符串
def encrypt_des():
    from Cryptodome.Cipher import DES
    import binascii

    # DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
    text = 'Welcome to DES'
    if len(text) % 8 != 0:
        text = text + "+" * (8 - len(text) % 8)
    # 密钥：必须为8字节
    key = b'12345678'
    # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
    des = DES.new(key, DES.MODE_ECB)
    # 加密
    result = des.encrypt(text.encode())

    print('加密后的数据：', result)
    # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
    print('转为十六进制：', binascii.b2a_hex(result))
    # 解密
    print('解密后的数据：', des.decrypt(result))


#加密方式
# 单向加密：MD5
#       只能对数据进行加密，而不能解密
# 对称加密：DES、AES
#       数据加密与解密使用相同的密钥
# 非对称加密：RSA
#       比对称加密更安全、但速度慢千倍、通常用来做身份认证

#例子  使用AES加密
def encrypt_aes():
    from Cryptodome.Cipher import AES
    from Cryptodome import Random
    import binascii

    text = 'Welcome to AES'
    # 密钥key 长度必须为16（AES-128）、24（AES-192）或 32（AES-256）的Bytes长度
    key = b'1234567890ABCDEF'
    # 生成长度等于AES块大小的不可重复的密钥向量
    iv = Random.new().read(AES.block_size)
    # 使用 key 和 iv 初始化AES对象，使用 AES.MODE_CFB 模式
    aes = AES.new(key, AES.MODE_CFB, iv)
    # 加密
    result = aes.encrypt(text.encode())
    # 解密
    # 不能在encrypt()之后调用decrypt()
    # 需要用相同的key和iv初始化新的AES对象
    decrypt_aes = AES.new(key, AES.MODE_CFB, iv)

    print('密钥：', key)
    print('iv：', iv)
    print('十六进制的iv：', binascii.b2a_hex(iv))
    print('加密后的数据：', result)
    print('转为十六进制：', binascii.b2a_hex(result))
    print('解密后的数据：', decrypt_aes.decrypt(result))


#RSA
#公钥加密、私钥解密




# pycryptodome进行RSA生成公钥、私钥，加密、解密、签名、验签
from Cryptodome.Hash import SHA
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Cryptodome.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
#base64是一种用64个字符来表示任意二进制数据的方法（将二进制数据编码成ASCII字符）,使用了A-Z、a-z、0-9、 + 、 / 这64个字符
#base64.b64encode(s) 　　　　　　　　　　对二进制数据进行base64编码#
#base64.b64decode(s) 　　　　　　　　　　对通过base64编码的数据进行解码
# Base64编码后的数据可能会含有 + / 两个符号，如果编码后的数据用于URL或文件的系统路径中，就可能导致Bug，所以base模块提供了专门编码url的方法
# base64.urlsafe_ b64encode(s) 　　　　　　 对URL进行base64编码
# base64.urlsafe_ b64decode(s) 　　　　　　 对URL进行base64解码

import base64


'''
加密的 plaintext 最大长度是 证书key位数/8 - 11
1024 bit的证书，被加密的最长 1024/8 - 11=117
2048 bit的证书，被加密的最长 2048/8 - 11 =245
'''
encode_gbk_utf8 = 'utf-8'  # 全局编码方式 utf-8 | gbk
key_num = 1024  # 证书key位数

# RSA的公私钥生成
def RSA_Create_Key():
    random_generator = Random.new().read  # 伪随机数生成器
    rsa = RSA.generate(key_num, random_generator)  # rsa算法生成实例
    private_pem = rsa.exportKey()  # master的秘钥对的生成
    # 生成公私钥对文件
    with open('master-private.pem', 'wb') as f:
        f.write(private_pem)
 
    public_pem = rsa.publickey().exportKey()
    with open('master-public.pem', 'wb') as f:
        f.write(public_pem)
    # ghost的秘钥对的生成,与master内容一样，如果想不一样请重新生成rsa实例
    private_pem = rsa.exportKey()
    with open('ghost-private.pem', 'wb') as f:
        f.write(private_pem)
 
    public_pem = rsa.publickey().exportKey()
    with open('ghost-public.pem', 'wb') as f:
        f.write(public_pem)

# ghost使用公钥加密
def RSA_gKey_Encrypt(message):
    with open('ghost-public.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的公钥
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
        # 加密message明文，python3加密的数据必须是bytes，不能是str
        cipher_text = base64.b64encode(cipher.encrypt(
            message.encode(encoding=encode_gbk_utf8)))
        return cipher_text

# ghost使用私钥解密
def RSA_gKey_Decrypt(cipher_text):
    with open('ghost-private.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)  # 导入读取到的私钥
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
        # 将密文解密成明文，返回的是bytes类型，需要自己转成str,主要是对中文的处理
        text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")
        return text.decode(encoding=encode_gbk_utf8)

# master 使用私钥对内容进行签名
def RSA_mKey_Sign(message):
    with open('master-private.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode(encoding=encode_gbk_utf8))
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)  # 对结果进行base64编码
    return signature
 
 
# master 使用公钥对内容进行验签
def RSA_mKey_CheckSign(message, signature):
    with open('master-public.pem', 'rb') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # 注意内容编码和base64解码问题
        digest.update(message.encode(encoding=encode_gbk_utf8))
        is_verify = verifier.verify(digest, base64.b64decode(signature))
    return is_verify


if __name__ == "__main__":
 
    '''
    # 如果要加密的内容是超长字符串或大文件，直接for一下进行分块操作就行
    try:
        with open('test_100MB.txt','rb') as f:
            while True:
            message = f.read(64) #长度由证书位数决定
            #rsa操作代码
    except EOFError:
        pass
    '''
    message = 'hello world, 你好世界 !'
    RSA_Create_Key()
    try:
        cipher_text = RSA_gKey_Encrypt(message)
        print(cipher_text)
        text = RSA_gKey_Decrypt(cipher_text)
        print(text)
 
        signature = RSA_mKey_Sign(message)
        print(signature)
        is_verify = RSA_mKey_CheckSign(message, signature)
        print(is_verify)
    except:
        print('rsa run error')