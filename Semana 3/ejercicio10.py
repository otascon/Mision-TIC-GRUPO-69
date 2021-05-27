tareas = {
    '01': {
            'descripcion': 'Ir a mercar',
            'estado': 'pendiente',
            'tiempo': 40
          },
    '02': {
            'descripcion': 'Estudiar',
            'estado': 'pendiente',
            'tiempo': 180
          },
    '03': {
            'descripcion': 'Hacer ejercicio',
            'estado': 'pendiente',
            'tiempo': 50
          }
}

def crear(tareas : dict, i : str, nt : dict):
    tareas[i] = nt
    return tareas

def leer(tareas : dict):
    print('\n Listar las tareas pendientes \n')
    for idd, info in tareas.items():
        print('\n', idd,' - ', end='\n')
        for nombre_a,atributo in info.items():
            print(atributo,', ',end='')

def verificarElemento(identificador, tareas):
    conjuntoIdentificadores = set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

opcion = 0
while opcion != 5:
    print('\n --- Aplicación CRUD tareas pendientes --- \n')
    print('1: Nueva tarea \n')
    print('2: Listar tareas \n')
    print('3: Actualizar tarea \n')
    print('4: Eliminar tarea \n')
    print('5: Salir \n')

    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        print('\n Agregar una nueva tarea \n')

        identificador = str(input('Ingrese el identificador de la tarea '))
        descripcion = str(input('Ingrese la descripcion de la tarea '))
        estado = str(input('Ingrese el estado de la tarea '))
        tiempo = int(input('Ingrese el tiempo de la tarea '))

        nuevaTarea = {
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }

        crear(tareas,identificador,nuevaTarea)

    elif opcion == 2:
        leer(tareas)
    elif opcion == 3:
        print('\n Editar una nueva tarea \n')
        identificador = str(input('Ingrese el identificador de la tarea para modificar: '))
        if verificarElemento(identificador,tareas):
            nuevaDescripcion = str(input('Nueva descripción'))
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado'))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = input('Nuevo tiempo')
            if nuevoTiempo:
                tareas[identificador]['tiempo'] = int(nuevoTiempo)
        else:
            print('No ha sido encontrada la tarea')    
    elif opcion == 4:
        print('\n Elimiar una nueva tarea \n')
        identificador = str(input('Ingrese el identificador de la tarea a eliminar: '))
        if verificarElemento(identificador,tareas):
            tareas.pop(identificador)
        else:
            print('No se encuentra la tarea para eliminar.')

print(tareas)