create table Transaction
(
    transaction_uuid varchar(64)                         not null
        primary key,
    account_uuid     varchar(64)                         not null,
    coupon_code      varchar(16)                         null,
    receive_time     datetime                            null,
    status           varchar(32)                         null,
    order_time       timestamp default CURRENT_TIMESTAMP null,
    constraint Transaction_ibfk_2
        foreign key (account_uuid) references Account (account_uuid)
);

INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('abc123-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'COUPON1', '2023-12-05 12:30:00', 'ordering', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('def456-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', null, null, 'delivering', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('ghi789-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'DISCOUNT15', '2023-12-10 14:45:00', 'arrived', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('jkl012-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', null, null, 'ordering', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('mno345-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'SAVE25NOW', '2023-12-08 10:00:00', 'delivering', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('pqr678-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'FESTIVE20', '2023-12-12 18:20:00', 'arrived', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('stu901-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', null, null, 'ordering', '2023-11-23 08:57:30');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, coupon_code, receive_time, status, order_time) VALUES ('vwx234-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'HOLIDAY10', '2023-12-07 15:10:00', 'delivering', '2023-11-23 08:57:30');
