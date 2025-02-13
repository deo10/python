# create function image_info with one param type dict
# fucntion looking for dict where should be two keys - image_id and image_title
# function should return string f"Image {image_title} has id {image_id}"

# my proposal
def image_info(**dict1):
    if 'image_title' not in dict1:
        raise TypeError("image_title key not found")
    if 'image_id' not in dict1:
        raise TypeError("image_id key not found")
    
    image_title = dict1['image_title']
    image_id = dict1['image_id']
    
    return f"Image {image_title} has id {image_id}"


try:
    # executing code block
    print(image_info(image_id = 1009, image_title = 'caty'))
    print(image_info(image_id1 = 1009, image_title1 = 'caty'))
except TypeError as e:
    print(e)
    
    
# from tutor
def image_info(img1):
    if ('image_title' not in img1) or ('image_id' not in img1):
        raise TypeError("required key not found")
    return f"Image {img1['image_title']} has id {img1['image_id']}"

try:
    # executing code block
    print(image_info({'image_id': 1009, 'image_title': 'caty'}))
    print(image_info({'image_id1': 1009, 'image_title': 'caty'}))
except TypeError as e:
    print(e)
    
