#!/bin/bash
mysql -uroot -e "CREATE USER 'qa'@'localhost' IDENTIFIED BY 'qa'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'qa'@'localhost'"
mysql -uroot -e "FLUSH PRIVILEGES"
