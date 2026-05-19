# MI_BSS_DATASET

## macOS 自動実行

```bash
mkdir -p ~/Library/LaunchAgents

cp macos/launchd/mi.bss.citibike.status.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.citibike.information.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.hellocycle.status.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.hellocycle.information.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.divvy.status.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.divvy.information.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.capitalbikeshare.status.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.capitalbikeshare.information.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.docomocycle.status.plist ~/Library/LaunchAgents/
cp macos/launchd/mi.bss.docomocycle.information.plist ~/Library/LaunchAgents/

uid=$(id -u)
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.citibike.status.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.citibike.information.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.hellocycle.status.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.hellocycle.information.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.divvy.status.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.divvy.information.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.capitalbikeshare.status.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.capitalbikeshare.information.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.docomocycle.status.plist
launchctl bootstrap gui/$uid ~/Library/LaunchAgents/mi.bss.docomocycle.information.plist

launchctl list | grep mi.bss
```

再起動:

```bash
uid=$(id -u)
launchctl kickstart -k gui/$uid/mi.bss.citibike.status
launchctl kickstart -k gui/$uid/mi.bss.citibike.information
launchctl kickstart -k gui/$uid/mi.bss.hellocycle.status
launchctl kickstart -k gui/$uid/mi.bss.hellocycle.information
launchctl kickstart -k gui/$uid/mi.bss.divvy.status
launchctl kickstart -k gui/$uid/mi.bss.divvy.information
launchctl kickstart -k gui/$uid/mi.bss.capitalbikeshare.status
launchctl kickstart -k gui/$uid/mi.bss.capitalbikeshare.information
launchctl kickstart -k gui/$uid/mi.bss.docomocycle.status
launchctl kickstart -k gui/$uid/mi.bss.docomocycle.information
```

停止:

```bash
uid=$(id -u)
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.citibike.status.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.citibike.information.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.hellocycle.status.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.hellocycle.information.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.divvy.status.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.divvy.information.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.capitalbikeshare.status.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.capitalbikeshare.information.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.docomocycle.status.plist
launchctl bootout gui/$uid ~/Library/LaunchAgents/mi.bss.docomocycle.information.plist
```

## Ubuntu 管理者権限なし

```bash
cd ~
git clone [REPOSITORY_URL] MI_BSS_DATASET
cd ~/MI_BSS_DATASET

python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install .

nohup .venv/bin/python src/collect_citibike_status.py > citibike_status.log 2>&1 &
nohup .venv/bin/python src/collect_citibike_information.py > citibike_information.log 2>&1 &
nohup .venv/bin/python src/collect_hellocycle_status.py > hellocycle_status.log 2>&1 &
nohup .venv/bin/python src/collect_hellocycle_information.py > hellocycle_information.log 2>&1 &
nohup .venv/bin/python src/collect_divvy_status.py > divvy_status.log 2>&1 &
nohup .venv/bin/python src/collect_divvy_information.py > divvy_information.log 2>&1 &
nohup .venv/bin/python src/collect_capitalbikeshare_status.py > capitalbikeshare_status.log 2>&1 &
nohup .venv/bin/python src/collect_capitalbikeshare_information.py > capitalbikeshare_information.log 2>&1 &
nohup .venv/bin/python src/collect_docomocycle_status.py > docomocycle_status.log 2>&1 &
nohup .venv/bin/python src/collect_docomocycle_information.py > docomocycle_information.log 2>&1 &
```

確認:

```bash
ps aux | grep collect
tail -f citibike_status.log
tail -f hellocycle_status.log
tail -f divvy_status.log
tail -f capitalbikeshare_status.log
tail -f docomocycle_status.log
```

停止:

```bash
ps aux | grep collect
kill [PID]
```
