# docker-in-celery

Proof-of-Concept of controlling docker processes from within Celery.

    >>> docker-compose up -d
    Creating dockerincelery_rabbitmq_1 ... done
    Creating dockerincelery_rabbitmq_1 ...
    Creating dockerincelery_celery_1   ... done
    >>> docker-compose run celery celery shell
    Starting dockerincelery_rabbitmq_1 ... done
    Python 3.6.4 (default, Jan 10 2018, 05:26:33)
    [GCC 5.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> import tasks
    >>> tasks.run_container.delay("nginx:alpine", "foo1")
    <AsyncResult: f03f269a-2798-4d18-b2bb-9ab1f2c5b99e>
    >>> exit()
    >>> docker ps
    CONTAINER ID        IMAGE                   COMMAND                  CREATED              STATUS              PORTS                                                   NAMES
    4bb866ae218c        nginx:alpine            "nginx -g 'daemon of…"   55 seconds ago       Up 54 seconds       80/tcp                                                  foo1
    661bd11787bd        celery_tasks:latest     "celery -A tasks wor…"   About a minute ago   Up About a minute                                                           dockerincelery_celery_1
    e726232d3e93        rabbitmq:3.7.3-alpine   "docker-entrypoint.s…"   About a minute ago   Up About a minute   4369/tcp, 5671/tcp, 25672/tcp, 0.0.0.0:5672->5672/tcp   dockerincelery_rabbitmq_1
    >>> docker-compose run celery celery shell
    Starting dockerincelery_rabbitmq_1 ... done
    Python 3.6.4 (default, Jan 10 2018, 05:26:33)
    [GCC 5.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> import tasks
    >>> tasks.stop_container.delay("foo1")
    <AsyncResult: 1425fa0a-a4cc-44ae-b1fe-96dd6dee9dd8>
    >>> exit()
    >>> docker ps
    CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                                                   NAMES
    661bd11787bd        celery_tasks:latest     "celery -A tasks wor…"   2 minutes ago       Up 2 minutes                                                                dockerincelery_celery_1
    e726232d3e93        rabbitmq:3.7.3-alpine   "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        4369/tcp, 5671/tcp, 25672/tcp, 0.0.0.0:5672->5672/tcp   dockerincelery_rabbitmq_1
    >>> docker-compose down
    Stopping dockerincelery_celery_1   ... done
    Stopping dockerincelery_rabbitmq_1 ... done
    Removing dockerincelery_celery_run_2 ... done
    Removing dockerincelery_celery_run_1 ... done
    Removing dockerincelery_celery_1     ... done
    Removing dockerincelery_rabbitmq_1   ... done
    Removing network dockerincelery_default