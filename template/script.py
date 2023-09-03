from jinja2 import Template, Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.')
)

template = env.get_template('email-template.html')

def get_data():
    data = [
        {
        "contact": {
            "user_id": "5077035",
            "recommended_ids": ["19416626","19407734"]
            },
        "lookups": {
            "recommended_restaurants":
            {
            "19416626":
                {
                    "name": "Frenchette",
                    "url": "https://resy.com/cities/ny/frenchette",
                    "thumbnail": "https://image.resy.com/3/003/2/1946/6b5a2e03692b6079da3caf09d55ba393e5be2dbd/jpg/1:1/400"
                },
            "19407734":
                {
                    "name": "Golden Diner",
                    "url": "https://resy.com/cities/ny/golden-diner",
                    "thumbnail": "https://image.resy.com/3/003/2/9520/775230f7cc2862c86eb97d45dbdc74fe18c1fe87/jpg/1:1/400"	      
                }
            }
        }
        }
    ]
    return data

data = get_data()

output = template.render(contact=data[0]["contact"], lookups=data[0]["lookups"])

print(output)

with open("../dynamic_[Marissa Vargas].html", "w", encoding="utf-8") as f:
    f.write(output)