from django.http import HttpResponse

def index(request, name, age, interests):
    return HttpResponse(f"""
           <h1>ФИО: {name}<h1>
           <h2>Возраст: {age}<h2>
           <h3>Интересы: {interests}<h3>
""")

def abaut(request, where, academic, like):
    return HttpResponse(f"""
           <p>Откуда приехал: {where} <p>
           <p>Успеваемость в школе: {academic}<p>
           <p>Любите/не любите учится: {like}<p>
""")

def contacts(request, telephone):
    return HttpResponse(f"""
           <p>Номер телефона: {telephone} <p>            
""")