# python-upload-s3-example

> [twiiks](http://redmine.twiiks.co/) 파이썬에서의 이미지 버퍼 가지고 놀기 예제

## Requirements
- Pillow
- boto3
- [AWS credentials](http://boto3.readthedocs.io/en/latest/guide/quickstart.html)

## What this project do ?
1. `twiiks.jpg` 파일을 읽어들여 `PIL Image` 객체로 만듭니다.
2. 만들어진 `PIL Image` 객체를 `base64 로 인코딩된 buffer` 형태로 만듭니다.
3. `s3` 에 업로드합니다.
4. `s3` 로부터 이미지를 읽어들여 `PIL Image`로 만듭니다.
5. 해당 이미지를 보여줍니다.