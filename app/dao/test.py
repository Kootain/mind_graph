from gremlin_python.driver import client
import os

username = os.getenv('gdb_username')
password = os.getenv('gdb_password')
print(username, password)
host = 'gds-t4n023gomp5sfjyj81850pub.graphdb.singapore.rds.aliyuncs.com'
port = '3734'
client = client.Client(f'ws://{host}:{port}/gremlin', 'g', username=username, password=password)


if __name__ == '__main__':

    callback = client.submit("g.V().limit(1)").all().result()
    for result in callback:
        print(result)
    client.close()