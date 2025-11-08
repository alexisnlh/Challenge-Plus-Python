# 🔍 Digram Distance Finder

> **Code Extra Challenge Python 2022** - Retos extra para practicar Python.

Como primer reto: Algoritmo optimizado para encontrar la distancia máxima entre digramas idénticos en una cadena de texto.

## 📋 Descripción del Problema

Un **digrama** es una secuencia de dos letras adyacentes dentro de un string. La **distancia** entre dos digramas es la diferencia de posición entre el primer carácter del primer digrama y el primer carácter del segundo digrama.

### Ejemplo

En el string `'aakmaakmakda'`:
- Los digramas `'ak'` aparecen en las posiciones **2** y **9**
- La distancia entre ellos es: `9 - 2 = 7`

## 🎯 Objetivo

Encontrar la **distancia máxima** entre dos digramas idénticos en un string. Si no existen digramas repetidos, devolver `-1`.

## 🚀 Casos de Ejemplo

| Input | Output | Explicación |
|-------|--------|-------------|
| `'aakmaakmakda'` | `7` | Digramas `'ak'` en posiciones 2 y 9 |
| `'aaa'` | `1` | Digramas `'aa'` en posiciones 1 y 2 |
| `'codility'` | `-1` | No hay digramas repetidos |
| `'abcabc'` | `3` | Digramas `'ab'` en posiciones 1 y 4 |
| `'aa'` | `-1` | Solo existe un digrama |

## ⚙️ Instalación

### Requisitos
- Python 3.10 o superior
- No requiere dependencias externas (solo librerías estándar)

### Clonar repositorio
```bash
git clone https://github.com/alexisnlh/Challenge-Plus-Python.git
cd challenge_plus_python
```

## 💻 Uso

### Modo Interactivo
```bash
python digram_optimizer.py
```

```
🔍 BUSCADOR DE DIGRAMAS
==================================================

Comandos:
  • Ingresa un string para analizar
  • 'test' para ejecutar tests
  • 'q' para salir

String a analizar: aakmaakmakda

✓ Distancia máxima: 7

Digramas encontrados:
  • 'ak' en posiciones 2 y 9
```

### Modo CLI
```bash
python digram_optimizer.py "aakmaakmakda"
```

### Ejecutar Tests
```bash
python digram_optimizer.py
> test
```

O desde Python:
```python
from digram_optimizer import find_max_digram_distance

result = find_max_digram_distance("aakmaakmakda")
print(result)     # Output: 7
```

## 🧪 Tests Incluidos

El script incluye 11 test cases que validan:
- ✅ Casos básicos con digramas repetidos
- ✅ Múltiples digramas consecutivos
- ✅ Strings sin digramas repetidos
- ✅ Edge cases (strings vacíos, un carácter, etc.)
- ✅ Patrones repetidos

```bash
🧪 Ejecutando tests...

✓ 'aakmaakmakda' -> 7 (esperado: 7) - Caso básico con 'ak'
✓ 'aaa' -> 1 (esperado: 1) - Múltiples 'aa' consecutivos
✓ 'codility' -> -1 (esperado: -1) - Sin digramas repetidos
✓ 'aa' -> -1 (esperado: -1) - String mínimo sin repetición
✓ 'aaaa' -> 2 (esperado: 2) - Cuatro letras iguales: 'aa' en pos 1, 2, 3
✓ 'abcabc' -> 3 (esperado: 3) - Patrón repetido 'ab'
✓ 'abab' -> 2 (esperado: 2) - Patrón 'ab' repetido inmediato
✓ '' -> -1 (esperado: -1) - String vacío
✓ 'a' -> -1 (esperado: -1) - Un solo carácter
✓ 'abcdefgh' -> -1 (esperado: -1) - Sin digramas repetidos
✓ 'xyzxyz' -> 3 (esperado: 3) - Múltiples digramas repetidos

==================================================
Tests: 11 pasados, 0 fallidos
==================================================
```

## 🏗️ Estructura del Código

```python
digram_optimizer.py
├── find_max_digram_distance()      # Algoritmo principal
├── validate_input()      # Validación de entrada
├── format_result()     # Formateo de salida
├── run_tests()     # Suite de tests
├── interactive_mode()      # Modo interactivo
└── main()      # Punto de entrada
```

## 🛡️ Validaciones

El script valida automáticamente:
- ✅ String no vacío
- ✅ Solo caracteres alfabéticos
- ✅ Límite máximo de 300,000 caracteres
- ✅ Conversión automática a minúsculas

## 🔧 Funciones Principales

### `find_max_digram_distance(str_var: str) -> int`
Encuentra la distancia máxima entre digramas idénticos.

**Args:**
- `str_var`: String de entrada (solo letras minúsculas)

**Returns:**
- Distancia máxima entre digramas idénticos, o `-1` si no existen digramas repetidos

### `validate_input(str_var: str) -> Tuple[bool, Optional[str]]`
Valida el input del usuario.

**Returns:**
- `(True, None)` si es válido
- `(False, mensaje_error)` si no es válido

### `format_result(str_var: str, result: int) -> str`
Formatea el resultado mostrando los digramas encontrados y sus posiciones.

## 🎨 Características Adicionales

- 🎯 **Output detallado** - Muestra qué digramas se encontraron y en qué posiciones
- 🧪 **Suite de tests integrada** - Valida el algoritmo con múltiples casos
- 🖥️ **Modo CLI y modo interactivo** - Flexibilidad de uso
- ✅ **Type hints completos** - Mejor documentación y autocompletado

## 📚 Ejemplos de Uso Avanzados

### Integración en otro script
```python
from digram_optimizer import find_max_digram_distance

# Lista de strings a procesar
strings = ['aakmaakmakda', 'codility', 'abcabc']

for s in strings:
    result = find_max_digram_distance(s)
    print(f"{s}: {result}")
```

### Procesamiento batch
```python
from digram_optimizer import find_max_digram_distance

# Leer desde archivo
with open('strings.txt', 'r') as f:
    for line in f:
        s = line.strip().lower()
        result = find_max_digram_distance(s)
        print(f"{s}: {result}")
```

## 📄 Licencia

Proyecto educativo sin licencia específica.

## 👨‍💻 Autor

Desarrollado como parte de **Code Extra Challenge Python 2022**

---

⭐ Si te resultó útil, dale una estrella al repositorio!
