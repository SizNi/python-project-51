import tempfile
import os
from project.page_loader import download


def test_download():
    current_dir = os.getcwd()
    url = f'{current_dir}/tests/fixtures/download.html'
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir_name = tmp
        # запуск тестируемой функции с сохранением во временную директорию
        download(url, tmp_dir_name)
        file_way = (
            f'{tmp_dir_name}/-home-ovechka-python'
            '-project-51-tests-fixtures-download-html.html'
        )
        # открываем получившийся файл как актуальный
        with open(file_way) as f:
            actual = f.read()
            print(actual)
            # открываем файл как ожидаемый
            with open(
                f'{current_dir}/tests/fixtures/test_download_explain.txt'
            ) as f1:
                expected = f1.read()
                # сравниваем
                assert actual == expected
