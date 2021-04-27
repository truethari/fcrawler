import sys
import optparse

from file_crawler.version           import __version__
from file_crawler.application       import worker

def main():
    usage = "usage: %prog [-s | --src] source_folder [-d | --dst] desination_folder \
            [-t | --type] file_type [options]"
    parser = optparse.OptionParser(description="FILE-CRAWLER v" + __version__, usage=usage)

    parser.add_option("-s", "--src",
            default=False,
            help="source folder"
            )
    parser.add_option("-d", "--dst",
            default=False,
            help="desination folder"
            )
    parser.add_option("-t", "--type",
            default=False,
            help="files type to crawl"
            )
    parser.add_option("-l", "--list",
            default=False,
            help="use files list"
            )
    parser.add_option("-f", "--file-list",
            default=False,
            help="generate files list file"
            )
    parser.add_option("-n", "--not-tree",
            action="store_true",
            default=False,
            help="don’t specify any sub directory"
            )
    parser.add_option("-v", "--version",
            action="store_true",
            default=False,
            help="show file-crawler version and exit"
            )
    (options, _) = parser.parse_args()
    options = vars(options)

    if options['version']:
        sys.exit(__version__)

    if options == {
                  'src': False,
                  'dst': False,
                  'type': False,
                  'list': False,
                  'file_list': False,
                  'not_tree': False,
                  'version': False
                  }:
        pass

    else:
        worker(options['src'], options['dst'], options['type'], options['list'],
               options['file_list'], options['not_tree'])

if __name__ == '__main__':
    main()
