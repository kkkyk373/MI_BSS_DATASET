# あくまで見本です。実行しないでください。　
# 同じファイルが armageddon:/home/hayashi/datasets/hello_cycle/ にもあります。
# そちらは現在進行形で動いています。(2025-10-04 22:00JST)

#!/usr/bin/env python3
import requests
import pandas as pd
import datetime as dt
import time
from pathlib import Path

# 保存先ディレクトリ（リポジトリ直下の datasets 配下）
DATA_DIR = Path(__file__).resolve().parent.parent / "datasets/hellocycle/hellocycling_information"
DATA_DIR.mkdir(parents=True, exist_ok=True)

INFO_URL = "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json"
SESSION = requests.Session()
TIMEOUT = 60

def fetch_information():
    r = SESSION.get(INFO_URL, timeout=TIMEOUT)
    r.raise_for_status()
    data = r.json()["data"]["stations"]
    df = pd.DataFrame(data)
    df["collected_at"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df

def save_csv(df):
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = DATA_DIR / f"hellocycling_information_{ts}.csv"
    df.to_csv(out, index=False)
    print(f"[{dt.datetime.now()}] Saved {out}", flush=True)

def main():
    while True:
        try:
            df = fetch_information()
            save_csv(df)
        except Exception as e:
            print(f"[{dt.datetime.now()}] Error: {e}", flush=True)

        # 7日(=604800秒)待機
        time.sleep(604800)

if __name__ == "__main__":
    main()
