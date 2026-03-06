from typing import List, Tuple, Dict, Union, Optional

def analizar_notas(alumnos: List[Tuple[str, float]]) -> Dict[str, Union[float, Optional[str]]]:
    """
    Analiza una lista de alumnos y sus notas para calcular estadísticas básicas.
    Lanza ValueError si alguna nota no está en el rango [0, 10].
    """
    # 1. Manejo del caso de lista vacía [cite: 85]
    if not alumnos:
        return {
            "nota_maxima": None,
            "nota_minima": None,
            "nota_media": 0.0,
            "mejor_alumno": None
        }

    # 2. Validación de rangos (Nueva mejora sugerida) [cite: 113, 114]
    for nombre, nota in alumnos:
        if not (0 <= nota <= 10):
            raise ValueError(f"Nota inválida para {nombre}: {nota}. Debe estar entre 0 y 10.")

    # 3. Extraemos solo las notas para cálculos numéricos [cite: 92]
    notas = [alumno[1] for alumno in alumnos]

    # 4. Calculamos las estadísticas [cite: 94, 95, 96]
    nota_maxima = max(notas)
    nota_minima = min(notas)
    nota_media = sum(notas) / len(notas)

    # 5. Buscamos al alumno con la nota máxima [cite: 98]
    mejor_alumno = max(alumnos, key=lambda x: x[1])[0]

    return {
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima,
        "nota_media": round(nota_media, 2), # Redondeo para legibilidad [cite: 103, 111]
        "mejor_alumno": mejor_alumno
    }

if __name__ == "__main__":
    # Datos de ejemplo
    lista_alumnos = [
        ("Ana", 8.5),
        ("Luis", 9.2),
        ("Marta", 7.0),
        ("Juan", 4.5)
    ]

    try:
        resultado = analizar_notas(lista_alumnos)
        print("--- Resultados del Análisis ---")
        for clave, valor in resultado.items():
            print(f"{clave.replace('_', ' ').capitalize()}: {valor}")
    except ValueError as e:
        print(f"Error: {e}")