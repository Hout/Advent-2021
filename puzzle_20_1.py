from collections import Counter


class Image:
    def __init__(self, init_image=None, width=None, height=None, init_background=None):
        image = init_image or (["." * (width or 0)] * (height or 0))
        self.hashes = set()
        for y, row in enumerate(image):
            for x, ch in enumerate(row):
                if ch == "#":
                    self.hashes.add((x, y))
        xs, ys = zip(*self.hashes)
        min_x = min(xs)
        min_y = min(ys)
        max_x = max(xs)
        max_y = max(ys)
        self.width = max_x - min_x + 1
        self.height = max_y - min_y + 1

        self.background = init_background or "."

        # align image to origin (0, 0)
        if min_x == 0 or min_y == 0:
            return

        new_hashes = set()
        for x, y in self.hashes:
            new_hashes.add((x - min_x, y - min_y))
        self.hashes = new_hashes

    def value(self, x, y) -> str:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.background
        return "#" if (x, y) in self.hashes else "."

    def get_square_value(self, x: int, y: int, length: int) -> int:
        s = ""
        for y_i in range(y - length // 2, y + length // 2 + 1):
            for x_i in range(x - length // 2, x + length // 2 + 1):
                s += self.value(x_i, y_i)
        return int(s.replace(".", "0").replace("#", "1"), 2)

    def apply_algorithm(self, algorithm: str):
        new_image = []
        for y in range(-1, self.height + 2):
            new_row = ""
            for x in range(-1, self.width + 2):
                algorithm_index = self.get_square_value(x, y, 3)
                new_row += algorithm[algorithm_index]
            new_image.append(new_row)

        new_background = algorithm[0] if self.background == "." else algorithm[-1]
        return Image(init_image=new_image, init_background=new_background)

    def hash_count(self):
        return len(self.hashes)

    def __str__(self) -> str:
        edge_size = 5
        str_image = [self.background * (self.width + 2 * edge_size)] * edge_size
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += "#" if (x, y) in self.hashes else "."
            str_image += [
                (self.background * edge_size) + row + (self.background * edge_size)
            ]
        str_image += [self.background * (self.width + 2 * edge_size)] * edge_size

        return "\n".join([row for row in str_image])


lines = [line.strip() for line in open("input_20.txt")]
i = 0
algorithm = ""
while lines[i] != "":
    algorithm += lines[i]
    i += 1

print("algorithm")
print(algorithm)

images = []

images.append(Image(lines[i + 1 :]))
for i in range(1, 51):
    images.append(images[-1].apply_algorithm(algorithm))
    # print(f"image after {i} cycle")
    # print(image)
    print(f"pixels lit after {i} cycles = {images[-1].hash_count()}")
