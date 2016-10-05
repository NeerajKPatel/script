from cassandra.cluster import Cluster

#import ssl
#
#hosts = ['127.0.0.1']
#port = 9042
#ssl_options = {
#                  'ca_certs': '/path/to/cassandra_cert.crt',
#                  'ssl_version': ssl.PROTOCOL_TLSv1
#              }
#
#self.cluster = Cluster(
#    hosts,
#    port=port,
#    ssl_options=ssl_options
#)

def getCredential(self):
    return {'username': '<username>', 'password':'<password>'}


def getResults(session, query):
    try:
        future = session.execute_async(query)
        for row in future.results():
            print row

    except Exception:
        print "Operation failed:"


node_ips = ['cassandra_node_name']
cluster = Cluster(node_ips, protocol_version=1, auth_provider=getCredential)
session = cluster.connect()
session.set_keyspace('cassandra_keyspace')
## or you can do this instead
#session.execute('USE users')

getResults(session, "SELECT * FROM users limit 10")

#user_lookup_stmt = session.prepare("SELECT * FROM users WHERE screen_name='NeerajKPatel'")
#user1 = session.execute(user_lookup_stmt, 'NeerajKPatel')
#getResults(user1)

cluster.shutdown()
