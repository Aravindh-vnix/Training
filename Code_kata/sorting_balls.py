#sorting balls program in kata11. http://codekata.com/kata/kata11-sorting-it-out/
class Rack:
    global myset
    myset = []

    def add(item):
        if item not in myset:
            myset.append(item)

    def balls(self):
        return sorted(myset, key=int)
