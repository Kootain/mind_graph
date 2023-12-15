from gremlin_python.driver import client
import os

username = os.getenv('gdb_username')
password = os.getenv('gdb_password')
print(username, password)
host = 'gds-t4n023gomp5sfjyj81850pub.graphdb.singapore.rds.aliyuncs.com'
port = '3734'
client = client.Client(f'ws://{host}:{port}/gremlin', 'g', username=username, password=password)


def call(q):
    callback = client.submit(q).all().result()
    for result in callback:
        print(result)


if __name__ == '__main__':

    # 建立点, 点类型 gdb_sample_person, 属性 {id, name}
    create_points = [
        "g.addV('gdb_sample_person').property(id, 'gdb_sample_alice').property('name', 'Alice');"
        "g.addV('gdb_sample_person').property(id, 'gdb_sample_bob').property('name', 'Bob');"
        "g.addV('gdb_sample_person').property(id, 'gdb_sample_carol').property('name', 'Carol');"
    ]
    for g in create_points:
        call(g)

    # 建立边, 边类型 gdb_sample_knows, 属性 {weight}
    create_edge = [
        "g.addE('gdb_sample_knows').from(V('gdb_sample_alice')).to(V('gdb_sample_bob')).property('weight', 0.5f);",
        "g.addE('gdb_sample_knows').from(V('gdb_sample_bob')).to(V('gdb_sample_carol')).property('weight', 0.5f);"
    ]
    for g in create_edge:
        call(g)

    onehop_query = "g.V('gdb_sample_alice').out('gdb_sample_knows').toList();"
    call(onehop_query)

    update_edge_property = "g.E().hasLabel('gdb_sample_knows').where(outV().has(id, 'gdb_sample_alice')).where(inV().has(id, 'gdb_sample_bob')).property('weight', 0.6f);"
    call(update_edge_property)

    drop_point = "g.V('gdb_sample_carol').drop().iterate();"
    call(drop_point)

    drop_edge = "g.V('gdb_sample_alice').outE('gdb_sample_knows').where(inV().has(id, 'gdb_sample_bob')).drop().iterate();"
    call(drop_edge)
