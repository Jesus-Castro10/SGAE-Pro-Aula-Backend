from rest_framework import serializers

class DynamicModelSerializer(serializers.Serializer):
    """
    Serializador genérico para clases de Python.
    """

    def __init__(self, instance, *args, **kwargs):
        """
        El serializador infiere los atributos de la clase directamente.
        """
        if not hasattr(instance, '__dict__'):
            raise ValueError("La instancia debe ser un objeto de clase de Python con atributos.")

        fields = {key: value for key, value in instance.__dict__.items()}
        self._dynamic_fields = fields
        super().__init__(instance, *args, **kwargs)

    def to_representation(self, instance):
        """
        Representación de los datos del objeto en formato serializado.
        """
        representation = {field: getattr(instance, field) for field in self._dynamic_fields}
        return representation

    def to_internal_value(self, data):
        """
        Convierte los datos deserializados en una instancia de clase de Python.
        """
       
        validated_data = {field: data.get(field) for field in self._dynamic_fields}
        return validated_data
