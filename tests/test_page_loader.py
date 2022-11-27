from page_loader.html_download import download
import tempfile


def test_download_html(requests_mock):
    url = 'http://test.com'
    requests_mock.get(url, text='data')
    with tempfile.TemporaryDirectory() as tmp:
        download(url, tmp)
        file_way = (f'{tmp}/test-com.html')
        with open(file_way) as f:
            actual = f.read()
            assert actual == 'data'
