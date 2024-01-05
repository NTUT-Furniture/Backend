until nc -z -v -w30 "nftbackend-mysql-1.nftbackend_default" 3306
do
  echo "Waiting a second until the database is receiving connections..."
  # wait for a second before checking again
  sleep 1
done
