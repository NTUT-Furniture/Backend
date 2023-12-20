create table Coupon
(
    coupon_code varchar(16)                         not null
        primary key,
    discount    int                                 not null check (discount between 0 and 100),
    expire_time datetime                            not null,
    update_time timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);

INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('30OFFSHOP', 30, '2024-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('COUPON1', 10, '2024-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('HOLIDAY10', 10, '2024-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE25NOW', 25, '2024-12-25 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE50NOW', 50, '2024-12-25 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE75NOW', 75, '2024-12-25 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE100NOW', 10, '2024-12-25 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE125NOW', 15, '2024-12-25 23:59:59', '2023-11-23 08:54:11');
