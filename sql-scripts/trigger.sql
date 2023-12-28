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


DELIMITER //
CREATE TRIGGER check_if_product_came_from_same_shop
    BEFORE INSERT
    ON TransactionProductLog
    FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1
                   FROM TransactionProductLog,
                        Product
                   WHERE TransactionProductLog.transaction_uuid = NEW.transaction_uuid
                     and TransactionProductLog.product_uuid = Product.product_uuid
                     and Product.shop_uuid = (SELECT shop_uuid
                                              FROM Product
                                              WHERE product_uuid = NEW.product_uuid))
        AND (SELECT 1
             FROM TransactionProductLog
             WHERE transaction_uuid = NEW.transaction_uuid)
    THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'This product does not belong to the same shop as the transaction';
    END IF;
END;
//
