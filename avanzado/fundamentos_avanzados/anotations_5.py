from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Unit especifica que nos puede regresar varios tipos de variable especificados
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)