# Asynchronous Tasks with Flask and Celery for Proccess Syngenta DB_Grower

### Quick Start

Up the containers:

```sh
$ docker-compose up -d --build
```

Run the Redis(if up the containers):

```sh
$ docker run -p 6379:6379 --name some-redis -d redis
```

To test if Redis is up and running, run:

```sh
$ docker exec -it some-redis redis-cli ping
```

Adding news Workers:

```sh
$ docker-compose up -d --build --scale worker=3
```

Open your browser to [http://localhost:5000](http://localhost:5000)

Exec tests:

```sh
$ docker-compose exec web python -m pytest
```

Exec tests individually:

```sh
$ docker-compose exec web python -m pytest -k "test_task and not test_home"
```
or
```sh
$ docker-compose exec web python -m pytest -k "test_mock_task"
```

Execute Task in bash:

```sh
$ curl http://localhost:5000/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```
