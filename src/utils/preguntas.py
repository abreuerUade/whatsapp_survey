class Preguntas:
    def __init__(self):
        self.preguntas = [
            "¿Pregunta 1?",
            "¿Pregunta 2?",
            "¿Pregunta 3?",

        ]

    def get_preguntas(self):
        return self.preguntas

    def get_pregunta(self, index):
        return self.preguntas[index]
