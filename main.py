import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str, file_names: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href_json = self.get_upload_link(file_path=file_path)
        href = href_json['href']
        responce = requests.put(href, data=open(file_names, 'br'))
        responce.raise_for_status()
        if responce.status_code == 201:
            print('success')

    def get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


if __name__ == '__main__':
    you_token = input('Введите токен: ')
    file_name = input('Ведите путь файла: ')
    path_to_file = os.path.basename(f'r{file_name}')
    uploader = YaUploader(you_token)
    uploader.upload(path_to_file, file_name)
