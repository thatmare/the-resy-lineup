from jinja2 import Template, Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.')
)

template = env.get_template('dynamic.html')

def get_data():
    data = []
    data.append(
        {
         "movies": [
             {         
                 "title": 'Terminator',
                 "description": 'One soldier is sent back to protect her from the killing machine. He must find Sarah before the Terminator can carry out its mission.'
             },
             {                 
                 "title": 'Seven Years in Tibet',
                 "description": 'Seven Years in Tibet is a 1997 American biographical war drama film based on the 1952 book of the same name written by Austrian mountaineer Heinrich Harrer on his experiences in Tibet.'
             },
             {               
                 "title": 'The Lion King',
                 "description": 'A young lion prince is born in Africa, thus making his uncle Scar the second in line to the throne. Scar plots with the hyenas to kill King Mufasa and Prince Simba, thus making himself King. The King is killed and Simba is led to believe by Scar that it was his fault, and so flees the kingdom in shame.'
             }
         ]
         })
    return data

# Obtener los datos
data = get_data()

# Renderizar la plantilla con los datos
output = template.render(data=data[0])

# Imprimir o hacer algo con el HTML resultante (output)
print(output, 'aquiii')
print('HOLAAAAAAAAAAAAAAA')
