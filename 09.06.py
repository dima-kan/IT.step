from redis import  Redis

host = "localhost"
port = 6379

server = Redis(
    host="localhost",
    port=6379,
    db=0,
)

user_name = server.get("NAME")
print(user_name)
