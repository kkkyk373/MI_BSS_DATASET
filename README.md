使い方
```python
nohup .venv/bin/python src/collect_citibike_status.py > citibike_status.log 2>&1 &
nohup .venv/bin/python src/collect_citibike_information.py > citibike_information.log 2>&1 &

nohup .venv/bin/python src/collect_hellocycle_status.py > hellocycle_status.log 2>&1 &
nohup .venv/bin/python src/collect_hellocycle_information.py > hellocycle_information.log 2>&1 &

# 止めるとき
ps
kill [プロセスID]
```

出力先はリポジトリ直下の `datasets/` 配下:
- Citi Bike ステータス: `datasets/citibike/station_status/`
- Citi Bike インフォメーション: `datasets/citibike/station_information/`
- HELLO CYCLING ステータス: `datasets/hellocycle/hellocycling_status/`
- HELLO CYCLING インフォメーション: `datasets/hellocycle/hellocycling_information/`

クレジット
- Citi Bike: GBFS `station_status.json` / `station_information.json` (https://gbfs.citibikenyc.com/)
- HELLO CYCLING: odpt / GBFS `station_status.json` / `station_information.json` (https://api-public.odpt.org/)

ライセンス
- MIT License (see `LICENSE`)
