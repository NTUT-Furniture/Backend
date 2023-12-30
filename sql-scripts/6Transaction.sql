create table Transaction
(
    transaction_uuid varchar(64)                         not null
        primary key,
    account_uuid     varchar(64)                         not null,
    shop_uuid        varchar(64)                         not null,
    coupon_uuid      varchar(16)                         null,
    receive_time     datetime                            null,
    status           ENUM('Ordered', 'Delivering', 'Arrived', 'Cancelled') not null,
    order_time       timestamp default CURRENT_TIMESTAMP not null,
    update_time      timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint Transaction_ibfk_2
        foreign key (account_uuid) references Account (account_uuid),
    constraint Transaction_ibfk_3
        foreign key (shop_uuid) references Shop (shop_uuid),
    constraint Transaction_ibfk_4
        foreign key (coupon_uuid) references Coupon (coupon_uuid),
    constraint Receive_after_arrive_check
        check ((`receive_time` is null) or (`status` = 'Arrived'))
);

INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_uuid, receive_time, status, order_time, update_time) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', 'def123', '2023-12-26 17:20:47', 'Arrived', '2023-12-26 09:21:01', '2023-12-30 13:43:38');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_uuid, receive_time, status, order_time, update_time) VALUES ('a8d3276c-71ac-4e7c-9d28-7426515dfed9', '831cdb41-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', null, null, 'Cancelled', '2023-12-28 11:00:00', '2023-12-30 14:23:01');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_uuid, receive_time, status, order_time, update_time) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '4001309d-8f2f-11ee-8b4f-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002', 'def123', null, 'Ordered', '2023-12-26 09:18:58', '2023-12-30 13:43:38');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_uuid, receive_time, status, order_time, update_time) VALUES ('f0234cf1-1f47-4b3c-8777-5fe72a94e510', '2dba33fc-345c-48e1-bdaa-62665648022b', 'f150af72-8998-11ee-bb92-42010aae0002', null, '2023-12-28 10:00:00', 'Arrived', '2023-12-28 09:30:00', '2023-12-30 14:23:01');
INSERT INTO NFT.Transaction (transaction_uuid, account_uuid, shop_uuid, coupon_uuid, receive_time, status, order_time, update_time) VALUES ('f3765e89-2826-46ee-97da-126fa81ee280', '4001309d-8f2f-11ee-8b4f-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002', null, '2023-12-30 13:50:42', 'Arrived', '2023-12-30 13:59:45', '2023-12-30 14:00:29');
