create table Coupon
(
    coupon_uuid varchar(64)                         not null primary key,
    coupon_code varchar(16)                         not null,
    discount    int                                 not null,
    expire_time timestamp                           not null,
    update_time timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    check (discount >= 0 and discount <= 100)
);


DELIMITER //

CREATE TRIGGER check_coupon_code
    BEFORE INSERT
    ON Coupon
    FOR EACH ROW
BEGIN
    IF NEW.coupon_code IS NOT NULL THEN
        IF EXISTS (SELECT 1
                   FROM Coupon
                   WHERE coupon_code = NEW.coupon_code
                     and expire_time >= convert_tz(now(), 'UTC', 'Asia/Taipei')) THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'There is a same coupon code that is not expired yet.';
        END IF;
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER check_coupon_expire_time
    BEFORE INSERT
    ON Coupon
    FOR EACH ROW
BEGIN
    IF NEW.coupon_code IS NOT NULL THEN
        IF New.expire_time < convert_tz(now(), 'UTC', 'Asia/Taipei') THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'The coupon has already expired.';
        END IF;
    END IF;
END;
//
DELIMITER ;
