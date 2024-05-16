#!/bin/sh

DATABASE='sales'
TABLE='sales_data'

echo "Pulling database: This may take a minutes"

backupfolder='/home/project'

keep_day=30

sqlfile=$backupfolder/sales_data.sql

#Create backup

if mysqldump -u root -pODkxMC1yb2NrZXRt $DATABASE $TABLE > $sqlfile; then
    echo "SQL dump created"
else
    echo 'No backup was created'
fi

