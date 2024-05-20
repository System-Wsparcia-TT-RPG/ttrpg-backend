from typing import List, Final, Optional

from django.db.models import Model

from rest_framework.serializers import ModelSerializer

MIN_JOIN_DEPTH: Final[int] = 0
MAX_JOIN_DEPTH: Final[int] = 10


def _bound_depth(depth: Optional[int]) -> int:
    if depth is None:
        return MIN_JOIN_DEPTH

    if depth < MIN_JOIN_DEPTH:
        return MIN_JOIN_DEPTH

    if depth > MAX_JOIN_DEPTH:
        return MAX_JOIN_DEPTH

    return depth


def _get_basic_serializer(
        data_model: type[Model],
        data_fields: List[str] | str,
        data_depth: Optional[int]
) -> type[ModelSerializer]:
    """
    Creates a basic serializer class with assigned
    """

    data_depth = _bound_depth(data_depth)

    class SerializerWrapper(ModelSerializer):
        class Meta:
            model = data_model
            fields = data_fields
            depth = data_depth

    return SerializerWrapper


def get_id_serializer(data_model: type[Model], depth: Optional[int]) -> type[ModelSerializer]:
    return _get_basic_serializer(data_model, ['id'], depth)


def get_all_serializer(data_model: type[Model], depth: Optional[int]) -> type[ModelSerializer]:
    return _get_basic_serializer(data_model, '__all__', depth)
