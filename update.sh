cd /var/www/html/rss/physics
{ time python3 update_notices.py 2> command.err ; } &>> log.txt
{ time python3 update_general.py 2> command.err ; } &>> log.txt
