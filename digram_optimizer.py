"""
    We are given a string S consisting of N lowercase letters. A sequence of
    two adjacent letters inside a sting is called a digram. The distance
    between two digrams is the distance between the first letter of the first
    digram and the first letter of the second digram. For example, in sting
    S = 'akcmz' the distance between digrams 'kc' and 'mz' is 2.

    We want to find the distance between the furthest identical digrams inside
    string S.

    Write a function:

        def solution(S)

    that, given a string S consisting of N letters, returns the distance
    between the two identical digrams in the string that lie furthest away
    from each other. If there are no two identical digrams inside S, your
    function should return -1.

    Examples:

    1. Given S = 'aakmaakmakda' you function should return 7. The furthest
    identical digrams are 'ak's, starting in positions 2 and 9 (enumerating
    from 1): 'aakmaakmakda'

    2. Given S = 'aaa' your function should return 1. The furthest identical
    digrams are 'aa's starting at positions 1 and 2.

    3. Given S = 'codility' your function should return -1. These are no two
    identical digrams in S.

    Write an efficient algorithm for the following assumptions:

        - N is an integer within the range [2...300,000].
        - String S is made only of lowercase letters (a-z).
"""
import sys
from typing import Dict, Optional, Tuple


def find_max_digram_distance(str_var: str) -> int:
    """
        Encuentra la distancia máxima entre digramas idénticos
        Args:
            str_var: String de entrada (solo letras minúsculas)
        Returns:
            Distancia máxima entre digramas idénticos, o -1 si no existen
    """
    # Validación básica
    if len(str_var) < 2:
        return -1

    # Diccionario para almacenar la primera aparición de cada digrama
    first_occurrence: Dict[str, int] = dict()
    max_distance = 0

    # Recorre el string generando digramas
    for idx in range(len(str_var) - 1):
        digram = str_var[idx:idx + 2]

        if digram in first_occurrence:
            # Calcula distancia desde la primera aparición
            distance = idx - first_occurrence[digram]
            max_distance = max(max_distance, distance)
        else:
            # Almacena la primera aparición
            first_occurrence[digram] = idx

    return max_distance if max_distance > 0 else -1


def validate_input(str_var: str) -> Tuple[bool, Optional[str]]:
    """
        Valida el input del usuario
        Args:
            str_var: String de entrada (solo letras minúsculas)
        Returns:
            (es_valido, mensaje_error)
    """
    if not str_var:
        return False, "El string no puede estar vacío"

    if not str_var.isalpha():
        return False, "El string solo puede contener letras"

    if not str_var.islower():
        return False, "El string debe estar en minúsculas"

    if len(str_var) > 300_000:
        return False, "El string excede el tamaño máximo (300,000 caracteres)"

    return True, None


def format_result(str_var: str, result: int) -> str:
    """
        Formatea el resultado de forma legible
    """
    if result == -1:
        return f" - No hay digramas repetidos en '{str_var}'"

    # Encuentra cuáles son los digramas con máxima distancia
    first_occurrence: Dict[str, int] = dict()
    matching_digrams = list()

    for idx in range(len(str_var) - 1):
        digram = str_var[idx:idx + 2]

        if digram in first_occurrence:
            distance = idx - first_occurrence[digram]
            if distance == result:
                pos1 = first_occurrence[digram] + 1
                pos2 = idx + 1
                matching_digrams.append((digram, pos1, pos2))
        else:
            first_occurrence[digram] = idx

    # Formatea output
    output = [f"Distancia máxima: {result}"]

    if matching_digrams:
        output.append("\nDigramas encontrados:")
        for digram, pos1, pos2 in matching_digrams:
            output.append(f" • '{digram}' en posiciones {pos1} y {pos2}")

    return "\n".join(output)


def run_tests():
    """
        Ejecuta tests del algoritmo
    """
    test_cases = [
        ("aakmaakmakda", 7, "Caso básico con 'ak'"),
        ("aaa", 1, "Múltiples 'aa' consecutivos"),
        ("codility", -1, "Sin digramas repetidos"),
        ("aa", -1, "String mínimo sin repetición"),
        ("aaaa", 2, "Cuatro letras iguales: 'aa' en pos 1, 2, 3"),
        ("abcabc", 3, "Patrón repetido 'ab'"),
        ("abab", 2, "Patrón 'ab' repetido inmediato"),
        ("", -1, "String vacío"),
        ("a", -1, "Un solo carácter"),
        ("abcdefgh", -1, "Sin digramas repetidos"),
        ("xyzxyz", 3, "Múltiples digramas repetidos")
    ]

    print("\nEjecutando tests...\n")
    passed = 0
    failed = 0

    for str_var, expected, description in test_cases:
        result = find_max_digram_distance(str_var)
        status = "✓" if result == expected else "✗"

        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"{status} '{str_var}' -> {result} (esperado: {expected}) - {description}")
    
    print(f"\n{'=' * 50}")
    print(f"Tests: {passed} pasados, {failed} fallidos")
    print(f"{'=' * 50}\n")


def interactive_mode():
    """
        Modo interactivo para probar el algoritmo
    """
    print("\n" + "=" * 50)
    print("BUSCADOR DE DIGRAMAS")
    print("=" * 50)
    print("\nComandos:")
    print(" • Ingresa un string para analizar")
    print(" • 'test' para ejecutar tests")
    print(" • 'q' para salir\n")

    while True:
        try:
            user_input = input("String a analizar: ").strip()
            if not user_input:
                continue

            if user_input.lower() == 'q':
                print("\nProceso finalizado!\n")
                sys.exit(0)

            if user_input.lower() == 'test':
                run_tests()
                continue

            # Normaliza a minúsculas
            str_var = user_input.lower()

            # Valida input
            is_valid, error_msg = validate_input(str_var)
            if not is_valid:
                print(f"\n[WARNING] - {error_msg}\n")
                continue

            # Calcula resultado
            result = find_max_digram_distance(str_var)

            # Muestra resultado formateado
            print(f"\n{format_result(str_var, result)}\n")

        except KeyboardInterrupt:
            print("\n\nProceso interrumpido!\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n[ERROR] - Error inesperado: {e}\n")


def main():
    """
        Función principal
    """
    if len(sys.argv) > 1:
        # Modo CLI: python digram_optimizer.py "string"
        str_var = sys.argv[1].lower()
        result = find_max_digram_distance(str_var)
        print(format_result(str_var, result))
    else:
        # Modo interactivo
        interactive_mode()


if __name__ == '__main__':
    main()
