# RabbitMQ-Python


## Install RabbitMQ Locally

- install Erlang
    - https://www.erlang.org/downloads

- install RabbitMQ server
    - https://www.rabbitmq.com/docs/install-windows#downloads

- list of RabbitMQ plugins
    - run RabbitMQ command prompt from start menu 
    - ```
        rabbitmq-plugins.bat list
        ```
    - ```
        rabbitmq-plugins.bat enable rabbitmq_management
        ```

## How to run 

- ```
    pip install pika
    ```

- from start menu, run RabbitMQ service - stop
- from start menu, run RabbitMQ service - start
- login to RabbitMQ from the browser: `localhost:15672`
    - user: `guest`
    - password: `guest`
- open three different trminals:

    - In consumer1_notify terminal:
        ```
        python consumer1_notify.py
        ```
    - In consumer2_report terminal:
        ```
        python consumer2_report.py
        ```
    - In publisher terminal:
        ```
        python publisher.py
        ```

## How to use RabbitMQ Docker Image

- docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
