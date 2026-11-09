# esquema de red del ejercicio 5: equipos con su tipo y conexiones con su peso

equipos = [
    {"nombre": "Red Hat", "tipo": "notebook"},
    {"nombre": "Debian", "tipo": "notebook"},
    {"nombre": "Arch", "tipo": "notebook"},
    {"nombre": "Manjaro", "tipo": "pc"},
    {"nombre": "Parrot", "tipo": "pc"},
    {"nombre": "Fedora", "tipo": "pc"},
    {"nombre": "Ubuntu", "tipo": "pc"},
    {"nombre": "Mint", "tipo": "pc"},
    {"nombre": "Guaraní", "tipo": "servidor"},
    {"nombre": "MongoDB", "tipo": "servidor"},
    {"nombre": "Router 1", "tipo": "router"},
    {"nombre": "Router 2", "tipo": "router"},
    {"nombre": "Router 3", "tipo": "router"},
    {"nombre": "Switch 1", "tipo": "switch"},
    {"nombre": "Switch 2", "tipo": "switch"},
    {"nombre": "Impresora", "tipo": "impresora"},
]

conexiones = [
    {"origen": "Switch 1", "destino": "Debian", "peso": 17},
    {"origen": "Switch 1", "destino": "Ubuntu", "peso": 18},
    {"origen": "Switch 1", "destino": "Impresora", "peso": 22},
    {"origen": "Switch 1", "destino": "Mint", "peso": 80},
    {"origen": "Switch 1", "destino": "Router 1", "peso": 29},
    {"origen": "Router 1", "destino": "Router 2", "peso": 37},
    {"origen": "Router 1", "destino": "Router 3", "peso": 43},
    {"origen": "Router 2", "destino": "Red Hat", "peso": 25},
    {"origen": "Router 2", "destino": "Guaraní", "peso": 9},
    {"origen": "Router 2", "destino": "Router 3", "peso": 50},
    {"origen": "Router 3", "destino": "Switch 2", "peso": 61},
    {"origen": "Switch 2", "destino": "Manjaro", "peso": 40},
    {"origen": "Switch 2", "destino": "Parrot", "peso": 12},
    {"origen": "Switch 2", "destino": "MongoDB", "peso": 5},
    {"origen": "Switch 2", "destino": "Arch", "peso": 56},
    {"origen": "Switch 2", "destino": "Fedora", "peso": 3},
]
