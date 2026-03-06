from typing import List, Tuple, Dict, Union, Optional

def analizar_notas(alumnos: List[Tuple[str, float]]) -> Dict[str, Union[float, Optional[str]]]:
    """
    Analiza una lista de alumnos y sus notas para calcular estadísticas básicas. [cite: 72]
    """
    # 1. Manejo del caso de lista vacía 
    if not alumnos:
        return {
            "nota_maxima": None,
            "nota_minima": None,
            "nota_media": 0.0,
            "mejor_alumno": None
        }

    # 2. Validación de rangos [cite: 82, 83]
    for nombre, nota in alumnos:
        if not (0 <= nota <= 10): # Error corregido: paréntesis y dos puntos 
            raise ValueError(f"Nota inválida para {nombre}: {nota}. Debe estar entre 0 y 10.")

    # 3. Extraemos solo las notas para cálculos numéricos 
    notas = [alumno[1] for alumno in alumnos]

    # 4. Calculamos las estadísticas 
    nota_maxima = max(notas)
    nota_minima = min(notas)
    nota_media = sum(notas) / len(notas)

    # 5. Buscamos al alumno con la nota máxima 
    mejor_alumno = max(alumnos, key=lambda x: x[1])[0]

    return {
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima,
        "nota_media": round(nota_media, 2), # Redondeo para legibilidad 
        "mejor_alumno": mejor_alumno
    }

# Corregido: Uso de __name__ con doble guion bajo 
if __name__ == "__main__":
    lista_alumnos = [
        ("Ana", 8.5),
        ("Luis", 9.2),
        ("Marta", 7.0),
        ("Juan", 4.5)
    ]
    
    try:
        # Error corregido: Asignación correcta del resultado 
        resultado = analizar_notas(lista_alumnos)
        
        print("--- Resultados del Análisis ---") 
        # Ahora resultado.items() no fallará porque es un diccionario 
        for clave, valor in resultado.items():
            nombre_limpio = clave.replace('_', ' ').capitalize()
            print(f"{nombre_limpio}: {valor}") 
            
    except ValueError as e:
        print(f"Error: {e}") 