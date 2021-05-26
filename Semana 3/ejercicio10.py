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
        print('\n Agregar una nueva tarea')

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
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass

print(tareas)