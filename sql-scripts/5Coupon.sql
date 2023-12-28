create table Coupon
(
    coupon_uuid varchar(64)                         not null
        primary key,
    coupon_code varchar(16)                         not null,
    discount    int                                 not null,
    expire_time timestamp                           not null,
    update_time timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    check ((`discount` >= 0) and (`discount` <= 100))
);

INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('abc123', 'SAVE20', 20, '2024-12-31 23:59:59', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('abc890', 'NEWYEAR50', 50, '2024-12-31 23:59:59', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('def123', 'MEMORIAL20', 20, '2024-05-31 18:30:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('def456', 'GET50OFF', 50, '2024-06-30 18:30:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('ghi456', 'LABORDAY15', 15, '2024-09-30 12:00:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('ghi789', 'FREESHIP', 100, '2024-12-15 12:00:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('jkl012', 'HOLIDAY25', 25, '2024-12-25 23:59:59', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('jkl789', 'EASTER10', 10, '2024-04-15 23:59:59', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('mno345', 'BIGSALE', 30, '2024-07-31 18:30:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('pqr678', 'WINTERSALE', 40, '2024-08-28 12:00:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('stu901', 'SUMMERDEAL', 15, '2024-08-31 23:59:59', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('vwx234', 'FLASHSALE', 50, '2024-12-10 18:30:00', '2023-12-28 02:45:25');
INSERT INTO NFT.Coupon (coupon_uuid, coupon_code, discount, expire_time, update_time) VALUES ('yzu567', 'SPRINGSALE', 35, '2024-04-30 12:00:00', '2023-12-28 02:45:25');
