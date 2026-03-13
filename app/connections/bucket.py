import re
import requests
from typing import List
from boto_orm.s3_manager import S3Manager
from app.config import s3_config, session, service

class ImageMover:
    def __init__(self, html_string: str, bucket_name='termex-bot', folder='images'):
        self.bucket_name = bucket_name
        self.s3 = S3Manager(bucket_name, config=s3_config, session_aws=session)
        self.folder = folder
        self._html_text = html_string

    def _get_urls(self) -> List[str]:
        pattern = r'src="([^"]+)"'
        return re.findall(pattern, self._html_text)

    def _get_image(self, url: str) -> bytes:
        response = requests.get(url)
        return response.content

    def update_url(self, url_old: str, path_new: str):
        path = f"{service.s3_config['endpoint_url']}/{self.bucket_name}/{path_new}"
        self._html_text = self._html_text.replace(url_old, path)

    def upload_image(self, data: bytes, path: str):
        try:
            self.s3.put_object(data, name_file=path)
            print('File', path, 'is upload to bucket', self.bucket_name)
        except Exception as e:
            print(e)

    def replace_url(self):
        for url in self._get_urls():
            name = url.split(sep='/')[-1]
            path = f'{self.folder}/{name}.jpg'
            img = self._get_image(url)
            self.upload_image(img, path)
            self.update_url(url, path)

    @property
    def html(self):
        return self._html_text
