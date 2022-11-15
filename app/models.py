from django.db import models
from django.contrib.postgres.fields import ArrayField
import docker

client = docker.from_env()


# TODO: container can be a model
class App(models.Model):
    name = models.CharField(null=False, max_length=128)
    image = models.CharField(null=False, max_length=512)
    envs = ArrayField(models.JSONField(), default=[])
    command = models.CharField(null=True, max_length=256)

    def run(self):
        from app.serializer import ContainerSerializer
        container = client.containers.run(image=self.image, command=self.command, environment=self.envs, detach=True)
        return ContainerSerializer([container]).serialize()

    def create_container(self, count: int = 1):
        containers = []
        for _ in range(count):
            container = client.containers.create(image=self.image, command=self.command, environment=self.envs)
            containers.append(container)
        return containers

    def containers(self):
        return client.containers.list(all=True, filters={"ancestor": self.image})

    def info(self):
        return client.images.get(name=self.image).attrs

    def kill_container(self, container_id: str):
        if container_id:
            container = client.containers.get(container_id)
            assert self.image == container.image.tags[0]
            container.kill()

