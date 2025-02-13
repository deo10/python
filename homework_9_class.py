# create class named Image

# each instance of the Image class should have 3 own attributes
# - resolution
# - title
# - extension

# class should have method resize, that should able to change resolition value

# create few instance of the Image class and invoke resize method


class Image:
  def __init__(self, resolution, title, extension): # Use the words mysillyobject and abc instead of self
    self.resolution = resolution
    self.title = title
    self.extension = extension

  def resize(self, new_resolution):
    self.resolution = new_resolution
   
  def __str__(self):
      return f"{self.title}.{self.extension}"    

    
image_1 = Image('1980x1024', 'cat', 'gif')
print(image_1)
print(image_1.resolution)
print(image_1.title)
print(image_1.extension)

image_1.resize('1024x768')
print(image_1.resolution)

image_2 = Image('1440x1024', 'dog', 'jpeg')
print(image_2) # dog.jpeg
print(image_2.resolution) # 1440x1024
print(image_2.title) # dog
print(image_2.extension) # jpeg

image_2.resize('1280x768')
print(image_2.resolution) # 1280x768

