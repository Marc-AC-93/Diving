class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    bar_ini = int(input("Bares iniciales: "))
except:
    print("[Error] Los bares deben ser un número entero")
    exit()

try:
    bar_fin = int(input("Bares finales: "))
except:
    print("[Error] Los bares deben ser un número entero")
    exit()

try:
    tankL = int(input("Litros del tanque: "))
except:
    print("[Error] Los litros del tanque deben ser un número entero")
    exit()

try:
    divingTime = int(input("Tiempo de inmersión (minutos): "))
except:
    print("[Error] El tiempo total debe ser un número entero")
    exit()

try:
    divingDeepAvg = (float(input("Profundidad media de la inmersión (metros): ")))/ 10 + 1
except:
    print("[Error] La profundidad media debe ser un número decimal expresado con punto (no usar coma)")
    exit()

total= str(round(float((((bar_ini - bar_fin) * tankL) / divingDeepAvg ) / divingTime), 2))

color = bcolors.GREEN if 20 > float(total) > 0 else bcolors.RED
print(f"{color}-------------{bcolors.ENDC}\n{color}|{bcolors.ENDC} "
      f"{bcolors.BOLD}RESULTADO{bcolors.ENDC} {color}|{bcolors.ENDC}\n{color}-------------{bcolors.ENDC}"
      f"\nConsumo de aire: {color}{total}{bcolors.ENDC} bares / minuto")