from datetime import date

def procesar_pedidos(pedidos):
    # Si la lista está vacía, devolvemos una lista vacía de inmediato
    if not pedidos:
        return []

    hoy = date.today()
    pedidos_procesados = []

    for pedido in pedidos:
        # 1. Extraer datos básicos
        cantidad = pedido.get('cantidad', 0)
        precio_unitario = pedido.get('precio_unitario', 0.0)
        fecha_caducidad = pedido.get('fecha_caducidad')
        
        # 2. Inicializar precio final
        precio_final = 0.0
        
        # 3. Regla: Productos caducados no se cobran (precio 0)
        # Solo calculamos si la cantidad es > 0 y no está caducado
        if cantidad > 0 and fecha_caducidad >= hoy:
            subtotal = precio_unitario * cantidad
            
            # 4. Aplicar descuentos por tramos
            if subtotal > 200:
                descuento = 0.15
            elif subtotal > 100:
                descuento = 0.10
            else:
                descuento = 0.0
            
            precio_final = subtotal * (1 - descuento)

        # Crear una copia del pedido original para no mutar los datos de entrada
        nuevo_pedido = pedido.copy()
        nuevo_pedido['precio_final'] = round(precio_final, 2)
        pedidos_procesados.append(nuevo_pedido)

    return pedidos_procesados

# --- Ejemplo de uso y casos límite ---

lista_pedidos = [
    {
        "id": 1, 
        "precio_unitario": 50.0, 
        "cantidad": 3, 
        "fecha_caducidad": date(2026, 12, 31)
    }, # Total 150 -> -10% = 135
    {
        "id": 2, 
        "precio_unitario": 100.0, 
        "cantidad": 3, 
        "fecha_caducidad": date(2026, 12, 31)
    }, # Total 300 -> -15% = 255
    {
        "id": 3, 
        "precio_unitario": 20.0, 
        "cantidad": 0, 
        "fecha_caducidad": date(2026, 12, 31)
    }, # CASO LÍMITE: Cantidad 0 -> 0€
    {
        "id": 4, 
        "precio_unitario": 80.0, 
        "cantidad": 10, 
        "fecha_caducidad": date(2023, 1, 1)
    }   # CASO LÍMITE: Caducado -> 0€
]

resultados = procesar_pedidos(lista_pedidos)

for r in resultados:
    print(f"Pedido {r['id']}: Precio Final = {r['precio_final']}€")