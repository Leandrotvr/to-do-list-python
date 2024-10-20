import json
import os

# Archivo donde se guardarán las tareas
TASKS_FILE = 'tasks.json'

# Función para cargar tareas desde el archivo
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Función para guardar tareas en el archivo
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Función para mostrar tareas
def show_tasks(tasks):
    if not tasks:
        print("No hay tareas en la lista.")
        return
    print("Tareas:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}: {task}")

# Función para agregar una tarea
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea '{task}' añadida.")

# Función para eliminar una tarea
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tarea '{removed}' eliminada.")
    else:
        print("Índice inválido.")

# Función principal
def main():
    tasks = load_tasks()

    while True:
        print("\nOpciones:")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Escribe la tarea: ")
            add_task(tasks, task)
        elif choice == '3':
            show_tasks(tasks)
            try:
                index = int(input("Escribe el número de la tarea a eliminar: ")) - 1
                remove_task(tasks, index)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif choice == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
