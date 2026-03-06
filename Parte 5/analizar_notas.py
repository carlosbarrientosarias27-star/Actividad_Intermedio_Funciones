from typing import List, Tuple, Dict, Union, Optional

def analizar_notas(alumnos: List[Tuple[str, float]]) -> Dict[str, Union[float, Optional[str]]]:
    """
    Analiza una lista de alumnos y sus notas para calcular estadísticas básicas.

    Args:
        alumnos: Una lista de tuplas donde cada tupla contiene (nombre, nota).

    Returns:
        Un diccionario con la nota máxima, mínima, media y el nombre del mejor alumno.
        Si la lista está vacía, devuelve valores nulos o cero.

    Ejemplo:
        >>> alumnos = [("Ana", 8.5), ("Luis", 9.2), ("Marta", 7.0)]
        >>> analizar_notas(alumnos)
        {'nota_maxima': 9.2, 'nota_minima': 7.0, 'nota_media': 8.23, 'mejor_alumno': 'Luis'}
    """
    
    # Manejo del caso de lista vacía
    if not alumnos:
        return {
            "nota_maxima": None,
            "nota_minima": None,
            "nota_media": 0.0,
            "mejor_alumno": None
        }

    # Extraemos solo las notas para cálculos numéricos
    notas = [alumno[1] for alumno in alumnos]
    
    # Calculamos las estadísticas
    nota_maxima = max(notas)
    nota_minima = min(notas)
    nota_media = sum(notas) / len(notas)
    
    # Buscamos al alumno con la nota máxima
    # En caso de empate, max() con key devolverá el primero encontrado
    mejor_alumno = max(alumnos, key=lambda x: x[1])[0]

    return {
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima,
        "nota_media": round(nota_media, 2),
        "mejor_alumno": mejor_alumno
    }

# --- Ejemplo de uso práctico ---
lista_clase = [("Carlos", 6.5), ("Sofía", 9.8), ("Jorge", 4.2), ("Elena", 8.9)]
resultado = analizar_notas(lista_clase)
print(resultado)