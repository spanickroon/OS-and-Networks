import os


class LargestFile:
    def __init__(self, search_dir):
        self.search_dir = search_dir

    def search_max_file(self):
        result = {}
        for root, dirs, files in os.walk(self.search_dir):
            for file_name in files:
                file_name = os.path.join(root, file_name)

                if os.path.isfile(file_name):
                    result.update({os.stat(file_name)[6]: file_name})

        return result[max(result)], max(result)


def main():
    search_dir = input('Enter the directory to search: ')
    lagest_file = LargestFile(search_dir)
    file_path, file_size = lagest_file.search_max_file()

    print(f'File path = {file_path}, size = {file_size} bytes.')


if __name__ == '__main__':
    main()
