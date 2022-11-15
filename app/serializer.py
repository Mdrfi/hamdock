from rest_framework import serializers

from app.models import App


class AppSerializer(serializers.ModelSerializer):
    envs = serializers.ListSerializer(child=serializers.JSONField())

    class Meta:
        model = App
        fields = (
            'id',
            'name',
            'image',
            'envs',
            'command'
        )


class ContainerSerializer:
    def __init__(self, containers: list):
        self.containers = containers

    def serialize(self):
        data = []
        for container in self.containers:
            data.append({
                "id": container.id,
                "image": container.image.tags,
                "name": container.name,
                "status": container.attrs.get("State", {}),

            })
        return data
