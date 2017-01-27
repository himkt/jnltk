import re
from lxml.etree import iterparse


def remove_emphasis(line):
    pattern = r'(\')+(.*?)(\')+'
    return re.sub(pattern, r'\2', line)


def remove_internal_link(line):
    pattern = r'\[\[(.*\|)?(.*?)\]\]'
    return re.sub(pattern, r'\2', line)


def clean_title(title):
    """
    "aaa|bbb" -> "aaa"
    """

    return re.sub(r'\|.*', '', title)


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



class JParser(object):
    """
    parser for Wikipedia dump data
    """

    def __init__(self,\
            enable_remove_internal_link=True, enable_remove_external_link=True,\
            enable_remove_emphasis=True, enable_clean_title=True,\
            ignore_category=True, ignore_template=True, ignore_heading=True, ignore_listing=True):

        self.enable_remove_internal_link = enable_remove_internal_link
        self.enable_remove_external_link = enable_remove_external_link
        self.enable_remove_emphasis = enable_remove_emphasis

        self.enable_clean_title = enable_clean_title
        self.ignore_category    = ignore_category
        self.ignore_heading     = ignore_heading
        self.ignore_listing     = ignore_listing
        self.ignore_template    = ignore_template


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


    def __preprocess(self, page):
        elements = []

        for line in page.split('\n'):

            if line.startswith('='):
                if self.ignore_heading:
                    line = ''

            elif line.startswith('*') or line.startswith('#'):
                if self.ignore_listing:
                    line = ''

            elif line.startswith('{{'):
                if self.enable_remove_internal_link:
                    line = ''

            elif line.startswith('[[Category:'):
                if self.ignore_category:
                    line = ''

            else:
                if self.enable_remove_internal_link:
                    line = remove_internal_link(line)

                if self.enable_remove_emphasis:
                    line = remove_emphasis(line)

            elements.append(line)

        return '\n'.join(filter(None, elements))


    def parse(self, xmlf):
        """
        cleaning title and text for each __parges elements
        """

        for title, page in self.__pages(xmlf):

            # log elements are ignored
            if title.startswith('Wikipedia:') or \
                    title.startswith('Template:') or \
                    title.startswith('Category:') or \
                    title.startswith('画像:') or \
                    title.startswith('ファイル:'):
                continue

            categories = extract_categories(page)

            if self.enable_clean_title:
                title = clean_title(title)

            page  = self.__preprocess(page)

            yield title, categories, page


if __name__ == '__main__':
    xmlf = 'data/20170127/jawiki-latest-pages-articles.xml'
    parser = JParser()

    for title, categories, page in parser.parse(xmlf):
        import time
        time.sleep(1)
        print(page)
