from sshtunnel import SSHTunnelForwarder
import psycopg2 as pg

with SSHTunnelForwarder(
    ('ssh_address', 22),
    ssh_username='ssh_username',
    ssh_pkey='ssh_pkey',
    ssh_private_key_password='ssh_paraphrase',
    remote_bind_address=('rds_address', 5432),
    local_bind_address=('localhost', 10022)
) as tunnel:
    print(tunnel.is_active)
    conn = pg.connect(user='db_username',
                      password='db_password',
                      dbname='db_name',
                      host='localhost',
                      port=10022)
    conn.close()