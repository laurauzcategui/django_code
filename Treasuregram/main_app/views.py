from django.shortcuts import render


def index(request):
    name = 'Gold Ring'
    value = 5000.0
    context = {'treasure_name': name,
               'treasure_val': value
               }
    return render(request, 'index.html', {'treasures':treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

site_img = "https://goo.gl/kLkulC"

treasures = [
    Treasure('Gold Ring', 500.0, 'Plastic', 'California',site_img),
    Treasure('Bronze Ring', 0.0, 'Gummy Bear', 'Thailand',site_img),
    Treasure('Platinum Statue', 5000.0, 'Salt', 'New Zealand',site_img),
    Treasure('Silver Mom', 4500.0, 'Sugar', 'China',site_img)
]
