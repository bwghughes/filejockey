import sys
import ntpath
import requests
import magic
from logzero import logger as log


def main(filename):
    mime = magic.Magic(mime=True).from_file(filename)
    log.debug(f'Uploading {filename} with mime-type of {mime}...')
    files = {'file': (ntpath.basename(filename), open(filename, 'rb'), mime, {'Expires': '0'})}
    resp = requests.post("https://file.io", files=files)
    log.debug(resp)
    log.debug(resp.json())
    return resp.json().get('link')


if __name__ == '__main__':
    print(main(sys.argv[1]))