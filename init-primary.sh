#!/bin/bash
echo "host replication all all 0.0.0.0/0 trust" >> "$PGDATA/pg_hba.conf"
echo "wal_level = replica" >> "$PGDATA/postgresql.conf"
echo "max_wal_senders = 10" >> "$PGDATA/postgresql.conf"
echo "wal_keep_size = 64" >> "$PGDATA/postgresql.conf"
echo "listen_addresses = '*'" >> "$PGDATA/postgresql.conf"
