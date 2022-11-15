from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import App, client
from app.serializer import AppSerializer, ContainerSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="run",
    )
    def run(self, request, *args, **kwargs):
        app = self.get_object()
        return Response(app.run())

    @action(
        detail=True,
        methods=["get"],
        url_path="containers",
    )
    def containers(self, request, *args, **kwargs):
        app = self.get_object()
        containers = app.containers()
        return Response(ContainerSerializer(containers).serialize())

    @action(
        detail=True,
        methods=["get"],
        url_path="info",
    )
    def info(self, request, *args, **kwargs):
        app = self.get_object()
        return Response(app.info())

    @action(
        detail=True,
        methods=["post"],
        url_path="container/create",
    )
    def create_container(self, request, *args, **kwargs):
        app = self.get_object()
        count = request.data.get("count", 1)
        containers = app.create_container(count)
        return Response(ContainerSerializer(containers).serialize())

    @action(
        detail=True,
        methods=["post"],
        url_path="container/kill",
    )
    def kill_container(self, request, *args, **kwargs):
        app = self.get_object()
        app.kill_container(request.data.get("id", None))
        return Response(status=status.HTTP_204_NO_CONTENT)

