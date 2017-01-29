from urllib.request import urlopen
from bz2 import BZ2File
from os import remove, mkdir
from os.path import isfile, exists
from datetime import datetime
from sklearn.externals.joblib import Parallel, delayed


class Crawler(object):

    def __init__(self, multithread, prefix):
        self.multithread = multithread

        self.prefix = prefix
        self.timestamp = datetime.today().strftime('%Y%m%d')
        self.output_dir = '{p}/{t}'.format(p=self.prefix, t=self.timestamp)

        self.url_list = [
            "https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2",
            "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"
        ]
        self.fname_list = [
            "jawiki-latest-pages-articles.xml",
            "enwiki-latest-pages-articles.xml"
        ]

        self.cleanup()

    def cleanup(self):
        if not exists(self.output_dir):
            mkdir(self.output_dir)

        for fname in self.fname_list:
            if isfile(self.output_dir + '/' + fname):
                remove(self.output_dir + '/' + fname)

    def crawl(self):
        if self.multithread:
            Parallel(n_jobs=-1)(
                delayed(self.download)(url, fname) for url, fname
                in zip(self.url_list, self.fname_list)
            )
        else:
            for url, fname in zip(self.url_list, self.fname_list):
                self.download(url, fname)

    def download(self, url, fname):
        response_bz2 = urlopen(url)
        response = BZ2File(response_bz2)

        with open(self.output_dir + '/' + fname, 'w') as fp:
            for index, line in enumerate(response):
                if index % 100000 == 0:
                    print(fname, index)
                fp.write(line.decode('utf-8'))


if __name__ == '__main__':
    crawler = Crawler(multithread=True, prefix='./data')
    crawler.crawl()
