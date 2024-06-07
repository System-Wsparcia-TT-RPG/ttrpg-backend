def add_get_all[T: HasGetAll](
        data_model: Type[Model],
        permissions: List[Type],
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class GetAll(APIView):
                queryset = data_model.objects.all()
                permission_classes = permissions

                def get(self, request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
                    serializer = get_all_serializer(data_model, depth)

                    return JsonResponse(serializer(self.queryset.all(), many=True).data, safe=False, status=200)
                
        return CRUDWrapper
    return inner


def add_get_id[T: HasGetId](
        data_model: Type[Model],
        permissions:List[Type],
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class GetId(APIView):
                queryset = data_model.objects.all()
                permission_classes = permissions

                def get(self, request: HttpRequest, identifier: Optional[int] = None, depth: Optional[int] = None
                        ) -> JsonResponse:
                    try:
                        instance = self.queryset.get(id=identifier)
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
                            status=404,
                            
                        )
        return CRUDWrapper
    return inner


def add_modify_id[T: HasModifyId](
        data_model: Type[Model],
        permissions:List[Type],
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class ModifyId(APIView):
                queryset = data_model.objects.all()
                serializer_class = get_all_serializer(data_model, None)
                serializer_id_class = get_id_serializer(data_model, None)
                permission_classes = permissions

                def patch(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    try:
                        instance = self.queryset.get(id=identifier)
                    except ObjectDoesNotExist as error:
                        return JsonResponse(
                            {
                                "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
                                "details": {
                                    "message": str(error),
                                },
                            },
                            status=404,
                        )

                    serializer = self.serializer_class(instance, data=loads(request.body), partial=True)

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(self.serializer_id_class(instance).data, status=200)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )

                def put(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    if data_model.objects.filter(id=identifier).exists():
                        instance = self.queryset.get(id=identifier)
                        serializer = self.serializer_class(instance, data=loads(request.body))
                        code: int = 200
                    else:
                        serializer = self.serializer_class(data=loads(request.body))
                        code: int = 201

                    if serializer.is_valid():
                        instance = serializer.save()
                        return JsonResponse(self.serializer_id_class(instance).data, status=code)

                    return JsonResponse(
                        {
                            "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
                            "details": serializer.errors
                        },
                        status=400,
                    )

                def delete(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
                    try:
                        count, _ = self.queryset.get(id=identifier).delete()

                        return JsonResponse({"deleted_objects": count}, status=200)
                    except ObjectDoesNotExist as error:
                        return JsonResponse(
                            {
                                "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
                                "details": {
                                    "message": str(error),
                                },
                            },
                            status=404,
                        )
                    
        return CRUDWrapper
    return inner

def add_create[T: HasCreate](
        data_model: Type[Model],
        permissions:List[Type],
) -> Callable[[Type[T]], Type[T]]:
    def inner(cls: Type[T]) -> Type[T]:
        class CRUDWrapper(cls):
            class Create(APIView):
                serializer_class = get_all_serializer(data_model, None)
                serializer_id_class = get_id_serializer(data_model, None)
                permission_classes = permissions

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




# def add_basic_crud[T: (HasGetAll, HasGetId, HasModifyId, HasCreate)](
#         data_model: Type[Model],
#         permissions: Dict[str, List[Type]],
# ) -> Callable[[Type[T]], Type[T]]:
#     def inner(cls: Type[T]) -> Type[T]:
#         class CRUDWrapper(cls):
#             class GetAll(APIView):
#                 queryset = data_model.objects.all()
#                 permission_classes = permissions['get_all']

#                 def get(self, request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
#                     serializer = get_all_serializer(data_model, depth)

#                     return JsonResponse(serializer(self.queryset.all(), many=True).data, safe=False, status=200)

#             class GetId(APIView):
#                 queryset = data_model.objects.all()
#                 permission_classes = permissions['get_id']

#                 def get(self, request: HttpRequest, identifier: Optional[int] = None, depth: Optional[int] = None
#                         ) -> JsonResponse:
#                     try:
#                         instance = self.queryset.get(id=identifier)
#                         serializer = get_all_serializer(data_model, depth)

#                         return JsonResponse(serializer([instance], many=True).data, safe=False, status=200)
#                     except ObjectDoesNotExist as error:
#                         return JsonResponse(
#                             {
#                                 "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
#                                 "details": {
#                                     "message": str(error),
#                                 },
#                             },
#                             status=404,
#                         )

#             class ModifyId(APIView):
#                 queryset = data_model.objects.all()
#                 serializer_class = get_all_serializer(data_model, None)
#                 serializer_id_class = get_id_serializer(data_model, None)
#                 permission_classes = permissions['modify_id']

#                 def patch(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
#                     try:
#                         instance = self.queryset.get(id=identifier)
#                     except ObjectDoesNotExist as error:
#                         return JsonResponse(
#                             {
#                                 "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
#                                 "details": {
#                                     "message": str(error),
#                                 },
#                             },
#                             status=404,
#                         )

#                     serializer = self.serializer_class(instance, data=loads(request.body), partial=True)

#                     if serializer.is_valid():
#                         instance = serializer.save()
#                         return JsonResponse(self.serializer_id_class(instance).data, status=200)

#                     return JsonResponse(
#                         {
#                             "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
#                             "details": serializer.errors
#                         },
#                         status=400,
#                     )

#                 def put(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
#                     if data_model.objects.filter(id=identifier).exists():
#                         instance = self.queryset.get(id=identifier)
#                         serializer = self.serializer_class(instance, data=loads(request.body))
#                         code: int = 200
#                     else:
#                         serializer = self.serializer_class(data=loads(request.body))
#                         code: int = 201

#                     if serializer.is_valid():
#                         instance = serializer.save()
#                         return JsonResponse(self.serializer_id_class(instance).data, status=code)

#                     return JsonResponse(
#                         {
#                             "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
#                             "details": serializer.errors
#                         },
#                         status=400,
#                     )

#                 def delete(self, request: HttpRequest, identifier: Optional[int]) -> JsonResponse:
#                     try:
#                         count, _ = self.queryset.get(id=identifier).delete()

#                         return JsonResponse({"deleted_objects": count}, status=200)
#                     except ObjectDoesNotExist as error:
#                         return JsonResponse(
#                             {
#                                 "error": f"\'{data_model.__class__.__name__}\' with specified id is not found!",
#                                 "details": {
#                                     "message": str(error),
#                                 },
#                             },
#                             status=404,
#                         )

#             class Create(APIView):
#                 serializer_class = get_all_serializer(data_model, None)
#                 serializer_id_class = get_id_serializer(data_model, None)
#                 permission_classes = permissions['create']

#                 def post(self, request: HttpRequest) -> JsonResponse:
#                     serializer = self.serializer_class(data=loads(request.body))

#                     if serializer.is_valid():
#                         instance = serializer.save()
#                         return JsonResponse(self.serializer_id_class(instance).data, status=201)

#                     return JsonResponse(
#                         {
#                             "error": f"Invalid \'{data_model.__class__.__name__}\' data!",
#                             "details": serializer.errors
#                         },
#                         status=400,
#                     )

#         return CRUDWrapper

#     return inner
