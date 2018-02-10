from celery import Celery
import subprocess

app = Celery('tasks', broker="amqp://guest@rabbitmq:5672/")


@app.task
def run_container(container, name):
    cmd = ["docker", "run", "-d", "--name", name, container]
    print(cmd)
    subprocess.run(cmd)


@app.task
def stop_container(name):
    cmd = ["docker", "stop", name]
    subprocess.run(cmd)

