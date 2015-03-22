#!/usr/bin/env bash
createlang plpgsql {{ pillar["postgresql"]["database"] }}
psql -d {{ pillar["postgresql"]["database"] }} -f /usr/share/postgresql/9.3/contrib/postgis-2.1/postgis.sql
psql -d {{ pillar["postgresql"]["database"] }} -f /usr/share/postgresql/9.3/contrib/postgis-2.1/spatial_ref_sys.sql