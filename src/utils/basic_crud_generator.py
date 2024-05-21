from json import loads
from typing import Protocol, Optional, Callable, Type

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView

from web.api.serializers import get_all_serializer, get_id_serializer


class HasGetAll(Protocol):
    class GetAll(APIView):
        def get(self, request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
            ...


class HasGetId(Protocol):
    class GetId(APIView):
        def get(self, request: HttpRequest, identifier: Optional[int] = None, depth: Optional[int] = None
                ) -> JsonResponse:
            ...


class HasModifyId(Protocol):
    class ModifyId(APIView):
        def patch(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
            ...

        def put(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
            ...

        def delete(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
            ...


class HasCreate(Protocol):
    class Create(APIView):
        def post(self, request: HttpRequest) -> JsonResponse:
            ...


def add_basic_crud[T: (HasGetAll, HasGetId, HasModifyId, HasCreate)](
        data_model: type[Model]
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class GetAll(APIView):
                def get(self, request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
                    all_objects = data_model.objects.all()
                    serializer = get_all_serializer(data_model, depth)

                    return JsonResponse(serializer(all_objects, many=True).data, safe=False, status=200)

            class GetId(APIView):
                def get(self, request: HttpRequest, identifier: Optional[int] = None, depth: Optional[int] = None
                        ) -> JsonResponse:
                    try:
                        instance = data_model.objects.get(id=identifier)
                        serializer = get_all_serializer(data_model, depth)

                        return JsonResponse(serializer([instance], many=True).data, safe=False, status=200)
                    except ObjectDoesNotExist as error:
                        return JsonResponse(
                            {
                                "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
                                "details": {
                                    "message": str(error),
                                },
                            },
                            safe=False,
                            status=404,
                        )

            class ModifyId(APIView):
                def patch(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    try:
                        instance = data_model.objects.get(id=identifier)
                    except ObjectDoesNotExist as error:
                        return JsonResponse(
                            {
                                "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
                                "details": {
                                    "message": str(error),
                                },
                            },
                            safe=False,
                            status=404,
                        )

                    serializer_class = get_all_serializer(data_model, None)
                    serializer_id_class = get_id_serializer(data_model, None)
                    serializer = serializer_class(instance, data=loads(request.body), partial=True)

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(serializer_id_class(instance).data, status=200)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )

                def put(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    serializer_class = get_all_serializer(data_model, None)
                    serializer_id_class = get_id_serializer(data_model, None)

                    if data_model.objects.filter(id=identifier).exists():
                        instance = data_model.objects.get(id=identifier)
                        serializer = serializer_class(instance, data=loads(request.body))
                        code: int = 200
                    else:
                        serializer = serializer_class(data=loads(request.body))
                        code: int = 201

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(serializer_id_class(instance).data, status=code)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )

                def delete(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    try:
                        count, _ = data_model.objects.get(id=identifier).delete()

                        return JsonResponse({"deleted_objects": count}, safe=False, status=200)
                    except ObjectDoesNotExist as error:
                        return JsonResponse(
                            {
                                "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
                                "details": {
                                    "message": str(error),
                                },
                            },
                            safe=False,
                            status=404,
                        )

            class Create(APIView):
                def post(self, request: HttpRequest) -> JsonResponse:
                    serializer_class = get_all_serializer(data_model, None)
                    serializer_id_class = get_id_serializer(data_model, None)
                    serializer = serializer_class(data=loads(request.body))

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(serializer_id_class(instance).data, status=201)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )

        return CRUDWrapper

    return inner
