create table Coupon
(
    shop_uuid   varchar(64)                         not null,
    discount    int                                 not null,
    coupon_code varchar(16)                         not null,
    expire_time date                                not null,
    update_time timestamp default CURRENT_TIMESTAMP null,
    constraint Coupon_ibfk_1
        foreign key (shop_uuid) references Shop (shop_uuid)
);

INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('30OFFSHOP', 20, '2024-12-31', '2023-12-22 10:13:45');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('45y54tgfs21', 11, '2024-12-22', '2023-12-22 10:10:48');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('45y54tgfs21ss', 11, '2024-12-22', '2023-12-22 10:11:58');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('COUPON1', 10, '2024-12-31', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('HOLIDAY10', 10, '2024-12-31', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('NEWCODE', 33, '2023-12-11', '2023-12-22 10:13:09');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE100NOW', 10, '2024-12-25', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE125NOW', 15, '2024-12-25', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE25NOW', 25, '2024-12-25', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE50NOW', 50, '2024-12-25', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (coupon_code, discount, expire_time, update_time) VALUES ('SAVE75NOW', 75, '2024-12-25', '2023-11-23 08:54:11');
