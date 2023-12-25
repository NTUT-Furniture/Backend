create table Transaction
(
    transaction_uuid varchar(64)                         not null
        primary key,
    account_uuid     varchar(64)                         not null,
    shop_uuid varchar(64) not null,
    coupon_code      varchar(16)                         null,
    receive_time     datetime                            null,
    status           varchar(32)                         null,
    order_time       timestamp default CURRENT_TIMESTAMP not null,
    update_time      timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint Transaction_ibfk_2
        foreign key (account_uuid) references Account (account_uuid),
    constraint Transaction_ibfk_3
        foreign key (shop_uuid) references Shop (shop_uuid),
    constraint Transaction_status_check
        check (status in ('Ordered', 'Delivering', 'Arrived', 'Cancelled')),
    constraint Receive_after_arrive_check
        check (receive_time is null or status = 'Arrived')
);
DELIMITER //

CREATE TRIGGER check_transaction_coupon_code
    BEFORE INSERT
    ON Transaction
    FOR EACH ROW
BEGIN
    IF NEW.coupon_code IS NOT NULL THEN
        IF NOT EXISTS (SELECT 1 FROM Coupon WHERE coupon_code = NEW.coupon_code) THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Invalid coupon code';
        END IF;
    END IF;
END;
//

DELIMITER ;
DELIMITER //

CREATE TRIGGER check_transaction_coupon_code_on_update
    BEFORE UPDATE
    ON Transaction
    FOR EACH ROW
BEGIN
    IF NEW.coupon_code IS NOT NULL THEN
        IF NOT EXISTS (SELECT 1 FROM Coupon WHERE coupon_code = NEW.coupon_code) THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Invalid coupon code';
        END IF;
    END IF;
END;
//

DELIMITER ;
