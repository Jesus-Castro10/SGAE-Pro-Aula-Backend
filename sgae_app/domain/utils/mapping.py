def mapper(target, source, fields: list[str]):
    """
    Copia atributos seleccionados desde `source` hacia `target`.

    Parámetros:
    - target: objeto a modificar
    - source: objeto de donde se copian los datos
    - fields: lista de atributos a copiar
    """
    for attr in fields:
        if hasattr(source, attr):
            setattr(target, attr, getattr(source, attr))

def person_mapper(target, source):
    fields = [
            'id_card', 'first_name', 'second_name', 'first_lastname', 'second_lastname',
            'birthdate', 'place_of_birth', 'address', 'phone', 'email', 'image'
        ]
    for attr in fields:
        if hasattr(source, attr):
            setattr(target, attr, getattr(source, attr))