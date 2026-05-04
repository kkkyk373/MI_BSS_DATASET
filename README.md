使い方
## 使い方

### 事前設定（初回のみ）
```bash
# AC接続時はシステムスリープを無効化
sudo pmset -c sleep 0
```

### 起動（AC電源接続必須）
```bash
# スリープしたら止まる
nohup .venv/bin/python src/collect_citibike_status.py > citibike_status.log 2>&1 &
nohup .venv/bin/python src/collect_citibike_information.py > citibike_information.log 2>&1 &
nohup .venv/bin/python src/collect_hellocycle_status.py > hellocycle_status.log 2>&1 &
nohup .venv/bin/python src/collect_hellocycle_information.py > hellocycle_information.log 2>&1 &

# スリープ対応
caffeinate -s nice -n 0 .venv/bin/python src/collect_citibike_status.py > citibike_status.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_citibike_information.py > citibike_information.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_hellocycle_status.py > hellocycle_status.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_hellocycle_information.py > hellocycle_information.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_divvy_status.py > divvy_status.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_divvy_information.py > divvy_information.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_capitalbikeshare_status.py > capitalbikeshare_status.log 2>&1 &
caffeinate -s nice -n 0 .venv/bin/python src/collect_capitalbikeshare_information.py > capitalbikeshare_information.log 2>&1 &
```
**注意**: `caffeinate -s` はAC電源接続時のみ有効。バッテリー駆動では蓋を閉じると停止する。

### 停止
```bash
ps aux | grep collect  # プロセスID確認
kill [プロセスID]
```

### ログ確認
```bash
tail -f citibike_status.log
tail -f hellocycle_status.log
```

## そのほか
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

スリープさせない（macOS）
- 実行中は別ターミナルで `caffeinate -dimsu` を動かしておくとスリープしません。終了は `Ctrl+C`。

再起動しても自動起動させる（macOS launchd の例）
1. プロジェクト内のサンプル plist をホームの LaunchAgents に配置  
   `mkdir -p ~/Library/LaunchAgents`  
   `cp macos/launchd/mi.bss.citibike.status.plist ~/Library/LaunchAgents/`  
   `cp macos/launchd/mi.bss.hellocycle.status.plist ~/Library/LaunchAgents/`
2. 読み込んで常駐開始  
   `launchctl load -w ~/Library/LaunchAgents/mi.bss.citibike.status.plist`  
   `launchctl load -w ~/Library/LaunchAgents/mi.bss.hellocycle.status.plist`
3. 停止するとき  
   `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/mi.bss.citibike.status.plist`  
   `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/mi.bss.hellocycle.status.plist`

※ `.venv` は `/Users/hideki/projects/MI_BSS_DATASET/.venv` にある前提です。別の場所を使う場合は plist 内のパスを修正してください。
