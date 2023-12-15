create table Coupon
(
    shop_uuid   varchar(64)                         not null,
    discount    int                                 not null,
    coupon_code varchar(16)                         not null,
    expire_time datetime                            not null,
    update_time timestamp default CURRENT_TIMESTAMP null,
    constraint Coupon_ibfk_1
        foreign key (shop_uuid) references Shop (shop_uuid)
);

INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150a4b3-8998-11ee-bb92-42010aae0002', 10, 'COUPON1', '2023-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150a4b3-8998-11ee-bb92-42010aae0002', 20, 'COUPON2', '2023-12-15 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150af72-8998-11ee-bb92-42010aae0002', 15, 'DISCOUNT15', '2023-12-20 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150af72-8998-11ee-bb92-42010aae0002', 25, 'SAVE25NOW', '2023-12-25 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150b186-8998-11ee-bb92-42010aae0002', 30, '30OFFSHOP', '2023-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150b186-8998-11ee-bb92-42010aae0002', 15, 'WINTER15', '2023-12-20 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150b368-8998-11ee-bb92-42010aae0002', 10, 'HOLIDAY10', '2023-12-31 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('f150b368-8998-11ee-bb92-42010aae0002', 20, 'FESTIVE20', '2023-12-15 23:59:59', '2023-11-23 08:54:11');
INSERT INTO NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time) VALUES ('6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 0, 'FREEEEEE', '2023-11-11 11:11:11', '2023-12-05 12:26:44');
