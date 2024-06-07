def add_create[T: HasCreate](
        data_model: Type[Model],
        permissions:List[Type],
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class Create(APIView):
                serializer_class = get_all_serializer(data_model, None)
                serializer_id_class = get_id_serializer(data_model, None)
                permission_classes = permissions['create']

                def post(self, request: HttpRequest) -> JsonResponse:
                    serializer = self.serializer_class(data=loads(request.body))

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(self.serializer_id_class(instance).data, status=201)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )
                    
        return CRUDWrapper
    return inner
