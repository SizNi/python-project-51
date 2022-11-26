import argparse
from project.page_loader import download
import os


current_dir = os.getcwd()


def main():
    description = 'download html page'
    parser = argparse.ArgumentParser(prog='page_loader', description=description)
    parser.add_argument('url')
    parser.add_argument('-v', '--version', action='version',
                        version='Current version is 1.0')
    parser.add_argument(
        '-o', '--output',
        help='save to', default=current_dir
    )
    args = parser.parse_args()
    download(args.url, args.output)

if __name__ == '__main__':
    main()