import random


class WordList:
    def __init__(self):
        self.file_name = 'Resources/words.txt'
        self.array = []
        self.open()

    def open(self):
        with open(self.file_name, "r") as ins:
            # i = 0

            for line in ins:
                # i += 1
                if line != "\n" and line != "" and "Day #" not in line:
                    self.array.append(line)
                    # print (line, len(self.array))

                # if i >= 20:
                #     break

    def get_random(self):
        # for x in range(10):
        array_size = len(self.array)
        print ("size: ", array_size)
        index = random.randint(0, array_size)
        # return index
        return self.array[index]


# word_list = WordList()
# print (word_list.get_random())