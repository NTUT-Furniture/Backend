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


INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('3dbb0f4f-7e4b-4de4-beed-1179dd9241d0', '831cd0d0-8916-11ee-bb92-42010aae0002', null, null, 'Cancelled',
        '2023-12-25 12:33:38', '2023-12-25 13:38:59');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('7ae4c64d-17ac-452d-a965-a52b4b948e91', '831cdf1e-8916-11ee-bb92-42010aae0002', null, null, 'Ordered',
        '2023-12-25 13:36:10', '2023-12-25 13:36:10');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('87db6a4b-d9a5-4313-aef6-b0ed6cacd7f0', '831cdf1e-8916-11ee-bb92-42010aae0002', null, null, 'Ordered',
        '2023-12-25 13:33:46', '2023-12-25 13:33:46');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('d5736bee-70c1-4f52-a767-a83a8ec4156b', '831cdf1e-8916-11ee-bb92-42010aae0002', null, null, 'Ordered',
        '2023-12-25 13:35:53', '2023-12-25 13:35:53');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('e96af1b3-2407-490d-9930-c76a57fdb97a', '831cdf1e-8916-11ee-bb92-42010aae0002', null, null, 'Ordered',
        '2023-12-25 13:37:27', '2023-12-25 13:37:27');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time, update_time)
VALUES ('f9e9ab39-869d-4d0a-adc2-11a148349b0d', '831cdf1e-8916-11ee-bb92-42010aae0002', null, null, 'Ordered',
        '2023-12-25 13:31:49', '2023-12-25 13:31:49');
