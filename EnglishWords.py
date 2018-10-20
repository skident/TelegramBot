import random


class WordList:
    def __init__(self):
        self.file_name = 'Resources/words.txt'
        self.array = []
        self.__open()

    def __nonblank_lines(self, f):
        for l in f:
            line = l.rstrip()
            if line:
                yield line

    def __open(self):
        with open(self.file_name, "r") as f_in:
            for line in self.__nonblank_lines(f_in):
                if line != "\n" and line != "" and "Day #" not in line:
                    self.array.append(line)
                    # print (line)

    def get_random(self):
        array_size = len(self.array)
        # print ("size: ", array_size)
        index = random.randint(0, array_size)
        # return index
        return self.array[index]


# word_list = WordList()
# print (word_list.get_random())