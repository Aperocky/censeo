import sys, os
import re
from preprocessor.utility.article import Article

class Preprocessor:

    def set_file_path(self, path, out=""):
        self.input_path = path
        self.compiled_lines = []
        self.set_output_path(out)

    def set_output_path(self, path=""):
        if not path:
            self.output_path = self.input_path + "_out"
        else:
            self.output_path = path

    def read_file(self):
        with open(self.input_path, "r") as fin:
            verbis = [word for line in fin for word in re.findall(r'[^\s]+', line)]
        article = Article(verbis)
        self.compiled_lines = article.run()

    def write_file(self):
        with open(self.output_path, "w") as fout:
            for line in self.compiled_lines:
                fout.write(line + "\n")

    def run(self):
        self.read_file()
        self.write_file()

if __name__ == "__main__":
    input_path = sys.argv[1]
    preprocessor = Preprocessor()
    preprocessor.set_file_path(input_path)
    preprocessor.run()
