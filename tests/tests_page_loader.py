from unittest.mock import Mock
import tempfile
import os
from page_loader import download

current_dir = os.getcwd()
print(current_dir)

url = f'{current_dir}/tests/fixtures/download.html'
def test_download():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir_name = tmp
    download(url, tmp_dir_name)
    file_way = f'{tmp_dir_name}/download-html.html'
    with open(file_way) as actual:
        with open('tests/fixtures/test_download_explain.txt') as expected:
            assert expected == actual