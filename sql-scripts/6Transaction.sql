create table Transaction
(
    transaction_uuid varchar(64)                         not null
        primary key,
    account_uuid     varchar(64)                         not null,
    shop_uuid        varchar(64)                         not null,
    coupon_code      varchar(16)                         null,
    receive_time     datetime                            null,
    status           ENUM('Ordered', 'Delivering', 'Arrived', 'Cancelled') not null,
    order_time       timestamp default CURRENT_TIMESTAMP not null,
    update_time      timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint Transaction_ibfk_2
        foreign key (account_uuid) references Account (account_uuid),
    constraint Transaction_ibfk_3
        foreign key (shop_uuid) references Shop (shop_uuid),
    constraint Receive_after_arrive_check
        check ((`receive_time` is null) or (`status` = 'Arrived'))
);

INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_code, receive_time, status, order_time, update_time) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', null, '2023-12-26 17:20:47', 'Arrived', '2023-12-26 09:21:01', '2023-12-26 09:29:24');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_code, receive_time, status, order_time, update_time) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '4001309d-8f2f-11ee-8b4f-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002', null, null, 'Ordered', '2023-12-26 09:18:58', '2023-12-26 09:28:38');
