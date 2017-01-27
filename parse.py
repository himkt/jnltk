import re
from lxml.etree import iterparse


class Parser(object):
    """
    parser for Wikipedia dump data
    """

    def __init__(self):
        pass


    def __pages(self, xmlf):
        """
        parse xml document

        generate pairs of title and text
        """
        for event, elem in iterparse(xmlf):
            if event == 'end':
                if elem.tag.endswith('title'):
                    title = elem.text

                elif elem.tag.endswith('text'):
                    text = elem.text
                    yield title, text


    def parse(self, xmlf):
        """
        cleaning title and text for each __parges elements
        """

        for title, page in self.__pages(xmlf):

            # log elements are ignored
            if title.startswith('Wikipedia:') or \
                    title.startswith('Template:') or \
                    title.startswith('Category:') or \
                    title.startswith('ファイル:'):
                continue

            yield self.clean_title(title), self.extract_categories(page), self.demarkup(page)


    @staticmethod
    def clean_title(title):
        """
        "aaa|bbb" -> "aaa"
        """

        return re.sub(r'\|.*', '', title)


    @staticmethod
    def extract_categories(page):
        """
        extract category from a page
        """
        categories = []
        pattern = r'\A\[\[Category:(.*?)(\|.*)?\]\]\Z'

        for line in page.split('\n'):
            for category in re.finditer(pattern, line):
                categories.append(category.group(1))

        return categories


    @staticmethod
    def demarkup(page):
        return page


if __name__ == '__main__':
    xmlf = '/data2/wikipedia_dump/20170105/jawiki-latest-pages-articles.xml'
    parser = Parser()

    for title, categories, text in parser.parse(xmlf):
        print(title)
        print(categories)
