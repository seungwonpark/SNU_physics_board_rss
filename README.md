# 서울대 물리학부 [게시판](http://physics.snu.ac.kr/xe/underbbs) rss
# SNU physics [board](http://physics.snu.ac.kr/xe/underbbs) rss

![status](https://circleci.com/gh/seungwonpark/SNU_physics_board_rss.svg?style=shield)

Source code of [SNU Physics Board RSS](http://swpark.ddns.net/rss/physics).

Based on Python3.

<img src='./images/example.png'>

## Instruction

```
cd /var/www/html/rss
git clone https://github.com/seungwonpark/SNU_physics_board_rss physics
touch srl_notices.txt
touch srl_general.txt
pip install feedgen
chmod update.sh 755
sudo crontab -e
*/2 * * * * /var/www/html/rss/physics/update.sh
```

Warning! `update_notices.py` should be executed prior to `update_general.py`.
