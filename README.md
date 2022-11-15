# Endpoint
<h3>create app</h3>
method: **POST**
<br>
endpoint: **/api/v1/apps/**
<br>
payload: **{
"name": "my-app",<br>
"image": "hub.hamdocker.ir/nginx:1.21",<br>
"envs": ["key1": "val1","key2": "val2"],<br>
"command": "sleep 1000"<br>
}**
<br>

<h3>edit app</h3>
method: **PATCH**<br>
endpoint: **/api/v1/apps/{id}**
<br>
payload: **{
"name": "my-app",<br>
"image": "hub.hamdocker.ir/nginx:1.21",<br>
"envs": ["key1": "val1","key2": "val2"],<br>
"command": "sleep 1000"<br>
}**
<br>

<h3>get app</h3>
method: **GET**<br>
endpoint: **/api/v1/apps/{id}**
<br>

<h3>edit image info</h3>
method: **GET**<br>
endpoint: **/api/v1/apps/{id}/info/**
<br>

<h3>run app</h3>
method: **POST**<br>
endpoint: **/api/v1/apps/{id}/run/**
<br>

<h3>list of container</h3>
method: **GET**<br>
endpoint: **/api/v1/apps/{id}/containers/**
<br>

<h3>create container</h3>
method: **POST**<br>
endpoint: **/api/v1/apps/{id}/container/create/**<br>
payload: **{"count": int}**
<br>

<h3>kill container</h3>
method: **POST**<br>
endpoint: **/api/v1/apps/{id}/container/kill/**<br>
payload: **{"id": str}**
<br>