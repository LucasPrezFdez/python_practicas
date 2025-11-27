class Usuario:
    def __init__(self, nombre, apellido1, apellido2, teléfono, email, dirección):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.teléfono = teléfono
        self.email = email
        self.dirección = dirección

    def __str__(self):
        return (
            "El usuario se llama "
            + self.nombre
            + " "
            + self.apellido1
            + " "
            + self.apellido2
            + " su telefono es: "
            + self.teléfono
            + " email: "
            + self.email
            + " direccion: "
            + self.dirección
        )

    def nombreCompleto(self):
        print(self.nombre.upper() + " " + self.apellido1.upper())


user = Usuario("Oscar", "Mongol", "Pipa", "7246218", "email@gmail.com", "hispanidad 33")

print(user)
user.nombreCompleto()
