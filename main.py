import os
import urllib
import base64
import boto3
from PIL import Image
from io import BytesIO

# AWS credentials 파일을 체크합니다.
# 구글닥스 공유폴더 /twiiks/keys/accessKeys.csv
# 참고 : http://boto3.readthedocs.io/en/latest/guide/quickstart.html
if not os.path.isfile(os.environ['HOME'] + '/.aws/credentials'):
    print('THERE IS NO CREDENTIALS FILE!!!')
    exit(0)

# jpg Image to PIL Image
# 로컬 파일 (./twiiks.jpg) 를 읽어서 PIL 이미지 객체로 만듭니다.
print('1. jpg to PIL Image')
img = Image.open('twiiks.jpg')
print('  finished\n')

# PIL Image to base64 encoded buffer
# PIL 이미지 객체를 base64 로 인코딩된 buffer 형태로 만듭니다.
print('2. PIL Image to base64 encoded buffer')
buffer = BytesIO()
img.save(buffer, format='JPEG')
imgBase64 = base64.b64encode(buffer.getvalue())
print('  Base64 Encoded Image : ' + str(imgBase64))
print('  finished\n')


# put base64 encoded buffer to s3
# Base64 로 인코딩된 buffer 를 S3 에 업로드합니다.
# Key 는 폴/더/파일명 형태가 됩니다.
# ContentType 이 지정되지 않으면, chrome 에서 바로 볼 수 없습니다.
# ACL 이 public-read 로 되어있지 않으면, 인증되지 않은 사용자는 읽을 수 없습니다.
print('3. upload image to s3')
s3 = boto3.resource('s3')
s3.Bucket('fontto'). \
    put_object(Key='example/twiiks.jpg',
               Body=base64.b64decode(imgBase64),
               ContentType='image/jpeg',
               ACL='public-read')
print('  finished\n')


# get PIL Image from s3
# 위에서 업로드한 이미지를 불러들여서 Byte 형태로 만듭니다.
# PIL Image 형태로 변환 후에 보여줍니다.
print('4. get PIL Image from s3')
bytesFromS3 = BytesIO(urllib.request
                      .urlopen('https://s3.ap-northeast-2.amazonaws.com/fontto/example/twiiks.jpg')
                      .read())
imgFromS3 = Image.open(bytesFromS3)
imgFromS3.show()
print('  finished\n')
