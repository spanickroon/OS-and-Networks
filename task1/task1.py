import os


class SearchingFiles:
    def __init__(self, search_dir, search_assign, file_to_write, count_files):
        self.search_dir = search_dir
        self.search_assign = search_assign
        self.file_to_write = file_to_write
        self.count_files = count_files

    def __search_files(self):
        result = []
        count = 0
        for root, dirs, files in os.walk(self.search_dir):
            for file_name in files:
                if file_name.endswith(self.search_assign):
                    result.append(file_name)
                    count += 1
            if self.count_files > 0 and count > self.count_files:
                break
        return result

    def __dump_to_file(self, list_of_files):
        if not os.path.isfile(self.file_to_write):
            self.file_to_write = 'result.txt'

        with open(self.file_to_write, 'a') as wf:
            wf.write('\n'.join(list_of_files))

    def search_and_record(self):
        self.__dump_to_file(self.__search_files())


def main():
    try:
        search_dir = input('Enter the directory to search: ')
        search_assignment = input('Enter the extension to search: ')
        file_to_write = input('Enter file to write: ')
        count_files = int(input('Enter the number to search or -1 for all: '))

        search_f = SearchingFiles(
            search_dir,
            search_assignment,
            file_to_write,
            count_files)
        search_f.search_and_record()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
