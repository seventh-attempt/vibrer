# Vibrer

## Online audio distribution platform and music sharing website


Installation Docker and its dependencies:
1) [Install Docker][1]
2) [Install Docker Compose][2]

Build container:
1) Enter project folder.
    ```bash
    cd vibrer
    # (you should get to the same level with Dockerfile)
    ```
2) Build container.
    ```
    sudo docker-compose build
    ```
3) Run container.
    ```
    sudo docker-compose run --service-ports web
    ```

Note:<br>
To update pip dependencies, run Django model migrations and start server execute following:
```
sudo docker-compose -f docker-compose.yaml -f docker-compose.setup.yaml up
```
To show running containers run following:
```bash
sudo docker ps
```
To stop concrete container run following:
```bash
sudo docker stop <container_name>
```

[1]: https://docs.docker.com/install/linux/docker-ce/ubuntu/
[2]: https://docs.docker.com/compose/install/
