import pathlib


class FileSearchEngine:
    
    def __init__(self, file_dir, exts = ['txt']):
        self.exts = exts
        self.file_dir = file_dir
        self.__found_files = {ext: [[], 0] for ext in self.exts}
    
    
    def add_found_files(self, files, ext):
        for file in files:
            self.__found_files[ext][0].append(file)
            self.__found_files[ext][1] += 1
    
    
    def search_recursively(self):
        for e in self.__found_files.keys():
            file_ext = r"**\*." + e
            files = list(pathlib.Path(self.file_dir).glob(file_ext))
            
            if files:
                self.add_found_files(files, e)
            
            return self.__found_files


def main():
    fs = FileSearchEngine(r'd:\\')
    for ext, files in fs.search_recursively().items():
        print(f'{ext} ({files[1]}): ')
        if files[1] > 0:
            for file in files[0]:
                print(file)


if __name__ == '__main__':
    main()
