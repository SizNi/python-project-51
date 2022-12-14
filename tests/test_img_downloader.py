from page_loader.img_download import img_downloader
import tempfile
import os

current_dir = os.getcwd()
print(current_dir)


def test_download_img(requests_mock):
    url = 'http://test.com'
    p = open(f'{current_dir}/tests/fixtures/test_img.png', 'rb')
    requests_mock.get(url, content=p.read())
    with tempfile.TemporaryDirectory() as tmp:
        with open(f'{tmp}/test-com.html', 'w') as f:
            f.write('<img src="http://test.com" alt="альтернативный текст">')
        with open(f'{tmp}/test-com.html', 'r') as f:
            print(tmp)
            img_downloader(tmp, 'test-com', url)
            size_expected = os.stat(
                f'{current_dir}/tests/fixtures/test_img.png'
            ).st_size
            size_actual = os.stat(f'{tmp}/test-com_files/test-com.png').st_size
            assert size_expected == size_actual
