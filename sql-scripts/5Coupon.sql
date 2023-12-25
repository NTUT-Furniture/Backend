create table Coupon
(
    coupon_uuid varchar(64) not null primary key,
    coupon_code varchar(16) not null,
    discount    int                                 not null,
    expire_time date                                not null,
    update_time timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
);
