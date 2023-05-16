class Image:

    def __init__(
            self,
            resolution: str,
            title: str,
            extension: str):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def __str__(self):
        return f'<Image object at {hex(id(self))} {self.__dict__}>'

    def resize(self, resolution: str):
        self.resolution = resolution


image_1 = Image(
    '3840x2160',
    'Обои для рабочего стола',
    'PNG'
)

image_2 = Image(
    '3000x1000',
    'Обложка страницы Твиттера',
    'JPG'
)

print(image_1)
print(image_2)

image_1.resize('2560x1440')
image_2.resize('1500x500')

print(image_1)
print(image_2)
