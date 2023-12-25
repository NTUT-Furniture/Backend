CREATE EVENT delete_expired_rows
    ON SCHEDULE EVERY 1 DAY
    DO
    DELETE FROM Coupon WHERE expire_time < NOW();
