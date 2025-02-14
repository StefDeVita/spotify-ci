import os
import subprocess

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

def evaluar_calidad():
    print("\nEvaluando calidad del código...")
    
    # Evaluar calidad del código con pylint
    print("\nEjecutando pylint...")
    pylint_resultado = ejecutar_comando("pylint tests_spotify.py")
    print(pylint_resultado)
    
    # Evaluar complejidad ciclomática con radon
    print("\nEvaluando complejidad ciclomática con radon...")
    radon_cc = ejecutar_comando("radon cc tests_spotify.py -a")
    print(radon_cc)
    
    # Evaluar índice de mantenibilidad con radon
    print("\nEvaluando índice de mantenibilidad con radon...")
    radon_mi = ejecutar_comando("radon mi tests_spotify.py")
    print(radon_mi)

if __name__ == "__main__":
    evaluar_calidad()
