class Item(object):

    index = ''
    left = 0
    top = 0
    right = 0
    bottom = 0

    def __init__(self, index, left, top, width, height):
        self.index = index
        self.left = left
        self.top = top
        self.right = left + width
        self.bottom = top + height


if __name__ == '__main__':
    lines = tuple(open('./input', 'r'))
    items = []
    for line in lines:
        parts = line.split(' ')
        coordinates = [int(i) for i in parts[2][:-1].split(',')]
        size = [int(i) for i in parts[3].split('x')]
        items.append(Item(parts[0], coordinates[0], coordinates[1], size[0], size[1]))

    for item1 in items:
        overlap = 0
        for item2 in items:
            if item1.index == item2.index:
                continue
            if item1.left < item2.right and item1.right > item2.left and item1.top < item2.bottom and item1.bottom > item2.top:
                overlap = 1
                break
        if overlap == 0:
            print(item1.index)
