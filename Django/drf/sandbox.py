from rest_framework.viewsets import ModelViewSet


class MyViewSet(ModelViewSet):
    def perform_create(self, serializer):
        # bla bla bla do what I want
        super().perform_create(serializer)
