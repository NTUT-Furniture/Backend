create table Account
(
    account_uuid varchar(64)                         not null
        primary key,
    name         varchar(64)                         not null,
    email        varchar(128)                        not null,
    pwd          varchar(128)                        not null,
    phone        varchar(32)                         null,
    credit_card  varchar(64)                         null,
    birthday     datetime                            null,
    address      varchar(256)                        null,
    is_active    tinyint(1)                          null,
    update_time  timestamp default CURRENT_TIMESTAMP null,
    constraint Account_pk
        unique (email)
);
create table Shop
(
    shop_uuid    varchar(64)                         not null
        primary key,
    account_uuid varchar(64)                         not null,
    name         varchar(64)                         not null,
    description  varchar(512)                        null,
    update_time  timestamp default CURRENT_TIMESTAMP null,
    constraint account_uuid
        unique (account_uuid),
    constraint Shop_ibfk_1
        foreign key (account_uuid) references Account (account_uuid)
);
create table Subscription
(
    account_uuid varchar(64) not null,
    shop_uuid    varchar(64) not null,
    primary key (account_uuid, shop_uuid),
    constraint Subscription_ibfk_1
        foreign key (account_uuid) references Account (account_uuid),
    constraint Subscription_ibfk_2
        foreign key (shop_uuid) references Shop (shop_uuid)
);
create table Product
(
    product_uuid varchar(64)                         not null
        primary key,
    shop_uuid    varchar(64)                         not null,
    name         varchar(64)                         not null,
    stock        int                                 not null,
    price        int                                 not null,
    tags         varchar(32)                         null,
    description  varchar(512)                        null,
    update_time  timestamp default CURRENT_TIMESTAMP null,
    constraint Product_ibfk_1
        foreign key (shop_uuid) references Shop (shop_uuid)
);

create table Transaction
(
    transaction_uuid varchar(64)                         not null
        primary key,
    shop_uuid        varchar(64)                         not null,
    account_uuid     varchar(64)                         not null,
    coupon_code      varchar(16)                         null,
    receive_time     datetime                            null,
    status           varchar(32)                         null,
    order_time       timestamp default CURRENT_TIMESTAMP null,
    constraint Transaction_ibfk_1
        foreign key (shop_uuid) references Shop (shop_uuid),
    constraint Transaction_ibfk_2
        foreign key (account_uuid) references Account (account_uuid)
);
create table TransactionProductLog
(
    transaction_uuid varchar(64) not null,
    product_uuid     varchar(64) not null,
    quantity         int         not null,
    constraint TransactionProductLog_ibfk_1
        foreign key (transaction_uuid) references Transaction (transaction_uuid),
    constraint TransactionProductLog_ibfk_2
        foreign key (product_uuid) references Product (product_uuid)
);
create table Comment
(
    transaction_uuid varchar(64)                         not null,
    account_uuid     varchar(64)                         not null,
    text             varchar(512)                        not null,
    likes            int                                 not null,
    dislikes         int                                 not null,
    update_time      timestamp default CURRENT_TIMESTAMP null,
    constraint Comment_ibfk_1
        foreign key (transaction_uuid) references Transaction (transaction_uuid),
    constraint Comment_ibfk_2
        foreign key (account_uuid) references Account (account_uuid)
);
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


insert into NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, update_time)
values  ('2dba33fc-345c-48e1-bdaa-62665648022b', 'gayrr', 't110590028@gmail.com', '$2b$12$g4aal9QhZbi9I1bepnCQv.IQCTBPiVDl9eX/2C3UOmPABg4EleV5O', 'phone', 'jy;kjr;ggk;lfkdfk;lfwjkrefwjpp', '1933-11-28 00:00:00', null, 1, '2023-11-30 13:56:52'),
        ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'fortesting', 'testing@gmail.com', '$2b$12$Fi/i/rHJ8cRFng01pX4OKum/2QpIgH8fu8Yc/lNvqSgvad.vVfy7i', '123456789', '1234-1234-1234-1234', '2023-12-04 18:33:29', '369 divine St, Taipei', 1, '2023-11-30 11:18:56'),
        ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'fjsdlkjflkds', 'fdafv@gmail.com', '$2b$12$5qitCd5.qoocUYozPp6oleXVNgsJ0jjPH1VfhvJCRRLYKgVP8rdAS', null, null, null, null, 1, '2023-11-30 11:19:19'),
        ('4db0ab33-6b79-48f7-94e4-5db4b1cea8cb', 'jdsklf', 'fjdsklfjdskl@gmail.com', 'fjdsklfjfklsd', null, null, null, null, 1, '2023-12-05 16:54:29'),
        ('51e2609f-2de1-4c42-ac4f-98c2c65cb392', 'i am not Garry', 'aasdg@gmail.com', '$2b$12$8JTsSI1zh2i0l6NDA3tjSOO7m4pFSW8/LPJOvs821VQfPtM12LHsS', null, null, null, null, 1, '2023-11-30 16:59:51'),
        ('60356ee5-4258-4391-a739-11c924b3209a', 'dsjflkj', 'aasdvgg@gmail.com', '$2b$12$HLhbWRJd7gt/F7Hc0fYOxuDDB7Ygxhpm.Ij6Ll5LZHxesSouaMi3q', null, null, null, null, 1, '2023-11-30 11:20:30'),
        ('76eafe7a-8d1d-11ee-bb92-42010aae0002', 'kyyyyyyyyyy', 'asd@gmail.com', '$2b$12$qVG8oV1vpc/mjbN0ol2lYeRFRw4fr2eJbp7Ta8RjARWA5SkHICVqS', '0955222444', null, '2077-07-07 00:00:00', null, 1, '2023-11-27 20:06:58'),
        ('7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'gjfkldgjlkj', 'asdf@gmail.com', '$2b$12$yJ7lpRrM0reofqj98eoJIuFygFzUP5Jy33fr2n5TIkSzW0JgsXUbi', null, null, null, null, 1, '2023-12-01 23:38:15'),
        ('831cd0d0-8916-11ee-bb92-42010aae0002', 'notVincent', 'john.doe@gmail.com', '$2b$12$u0UlZ0Eaq0Y.FmOPiAPQ1ux/Y9KCQrGJMYPGU11hPwHfixb9gwPey', '123-456-7890', '1234-5678-9012-3456', '1990-01-15 00:00:00', '123 Main St, Cityville', 1, '2023-11-22 17:07:07'),
        ('831cdb41-8916-11ee-bb92-42010aae0002', 'gary', 'gjlksjlkdgg32f@gmail.com', '$2b$12$LJNnAlmnPW/QmiOvDGVCUuXHO391NQ5.WbJh00.yo.eLakTrF9ikq', 'ejgklgjdklffl21', 'fkl2lk1rklgnk', '2002-11-28 15:14:45', 'asd', 1, '2023-11-22 17:07:07'),
        ('831cdd39-8916-11ee-bb92-42010aae0002', 'Bob Johnson', 'bob.johnson1@gmail.com', '$2b$12$Shl8PhzNNNt.qamWUWOQtOw0mZW9UOEegYnRnKkCHKw4qPg.gxvty', '555-123-4567', '4321-8765-0987-6543', '1978-03-10 00:00:00', '789 Pine St, Villagetown', 0, '2023-11-22 17:07:07'),
        ('831cde2e-8916-11ee-bb92-42010aae0002', 'Alice Williams', 'alice.williams@gmail.com', '$2b$12$0jaLxH5zkIZcPrLXnAqr4uJE4jdsOSOBya.OTgYzBUL.wiS1rAcBW', '333-999-8888', '8765-4321-5678-9012', '1982-11-05 00:00:00', '567 Elm St, Hamletville', 1, '2023-11-22 17:07:07'),
        ('831cdf1e-8916-11ee-bb92-42010aae0002', 'Charlie Brown', 'charlie.brown@gmail.com', '$2b$12$Ct6e9IR6pH8/uAizZbf93eZ/E3VDSNfbUt6itjf0l1ung1n/ZPlu6', '777-555-1234', '3456-7890-1234-5678', '1995-09-30 00:00:00', '234 Birch St, Riverside', 1, '2023-11-22 17:07:07'),
        ('849c38d1-8916-11ee-bb92-42010aae0002', 'John Doe', 'john.1@gmail.com', '$2b$12$o7YoV1XCBT1aYblWRPJchuoHUcsIpXj.G72rTJhl4pTIfV8NAoy.S', '123-456-7890', '1234-5678-9012-3456', '1990-01-15 00:00:00', '123 Main St, Cityville', 1, '2023-11-22 17:07:10'),
        ('849c3d7c-8916-11ee-bb92-42010aae0002', 'Jane Smith', 'jane.smith@gmail.com', '$2b$12$WVr0/dD5IepeaF7Y5EKWNuOh4ZYHnYdzuZ8lexPdT/OGzylPS.Rau', '987-654-3210', '9876-5432-1098-7654', '1985-07-22 00:00:00', '456 Oak St, Townsville', 1, '2023-11-22 17:07:10'),
        ('849c3e36-8916-11ee-bb92-42010aae0002', 'Bob Johnson', 'bob.johnson@gmail.com', '$2b$12$Shl8PhzNNNt.qamWUWOQtOw0mZW9UOEegYnRnKkCHKw4qPg.gxvty', '555-123-4567', '4321-8765-0987-6543', '1978-03-10 00:00:00', '789 Pine St, Villagetown', 0, '2023-11-22 17:07:10'),
        ('849c3eba-8916-11ee-bb92-42010aae0002', 'Monfjdskl', 'fdjkfldjlk@gmail.com', '$2b$12$Bzk92.wdzsiJSky3X8qrMe4zZuMH/rhVms7ALcM8OkhGuF39pl/TS', '333-999-8888', '8765-4321-5678-9012', '1982-11-05 00:00:00', '567 Elm St, Hamletville', 1, '2023-11-22 17:07:10'),
        ('849c3f2b-8916-11ee-bb92-42010aae0002', 'Dars Veda', '654675@gmail.com', '$2b$12$Bzk92.wdzsiJSky3X8qrMe4zZuMH/rhVms7ALcM8OkhGuF39pl/TS', '777-555-1234', '3456-7890-1234-5678', '1995-09-30 00:00:00', '234 Birch St, Riverside', 1, '2023-11-22 17:07:10'),
        ('a3711878-44ae-4328-ad62-4ed45b57c848', 'dsadsad', 'dasads@gmail.com', '$2b$12$prjeXdsp1tP5cwykE07eXe8lECowYo0huIskmRYTfEHBbPtlfFXh6', null, null, null, null, 1, '2023-12-05 17:08:48'),
        ('ad593cad-96fb-4ebe-a5e4-a0b9101a8d5c', 'hhh', '3r24g@gmail.com', '$2b$12$4h9XTIYXVrNgUBzG394ThuMCopoxgxMG1zlMDa0PuufNN9nKiw0Cm', null, null, null, null, 1, '2023-11-30 10:14:58'),
        ('cde5df65-8e91-11ee-8b4f-42010aae0002', 'fuck Garry', '34t345@gmail.com', '$2b$12$I0MmxEOt73PHGmPu0sMWD.kixGZ5yp9rM/yeT09yQRv4uKOD3L/NG', null, null, null, null, 1, '2023-11-29 16:32:17'),
        ('dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'asdfg', '5g55gh@gmail.com', '$2b$12$ewoORsPFmQsYkVNf1jc6UuE9f.Xi235WeH0m78QVdu2xMUBQ.FdLC', null, null, null, null, 1, '2023-11-30 21:56:05'),
        ('ddaa8cf0-8db0-11ee-bb92-42010aae0002', 'name1', '43h54h@gmail.com', '$2b$12$tnxb7Xi0ol/c7Dv9FBLOkO2ZBnqglci58YZ7GPt3fiBI6ClMdoKt6', null, null, null, null, 1, '2023-11-28 13:42:06'),
        ('f3e433bf-8f2e-11ee-8b4f-42010aae0002', 'fjsdlkjflkds', '3h5h5@gmail.com', '$2b$12$5qitCd5.qoocUYozPp6oleXVNgsJ0jjPH1VfhvJCRRLYKgVP8rdAS', null, null, null, null, 1, '2023-11-30 11:17:11'),
        ('f81672f3-2925-4396-a33e-dd85a4c03ca1', 'fuck', 'email@gmail.com', '$2b$12$34f7VKnl5ea9YZj6/zEH9uTra6a.SK6yWpKrUMyLqS3GlG1GOFklO', '123-456-7890', '1234-5678-9012-3456', '1990-01-15 00:00:00', '123 Main St, Cityville', 1, '2023-12-05 17:21:26');
insert into NFT.Shop (shop_uuid, account_uuid, name, description, update_time)
values  ('6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 'dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'shoppppppppp11111', null, '2023-11-30 21:57:16'),
        ('c4f8d1b0-8d24-11ee-bb92-42010aae0002', '76eafe7a-8d1d-11ee-bb92-42010aae0002', 'kkyy shop', 'description', '2023-11-27 20:59:15'),
        ('c90a780a-8974-4507-9f57-032e5324f18f', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 't', 'fds', '2023-12-05 20:03:18'),
        ('e31b3d02-2995-4e2c-9481-93a63403c7af', '7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'fddfsd', null, '2023-12-01 23:38:31'),
        ('f150a4b3-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'changeed name', 'hi gay shop', '2023-11-23 08:40:47'),
        ('f150acb3-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'Shop 2', 'This is the second shop.', '2023-11-23 08:40:47'),
        ('f150af72-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'Shop 3', 'This is the third shop.', '2023-11-23 08:40:47'),
        ('f150b096-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'Shop 4', 'This is the fourth shop.', '2023-11-23 08:40:47'),
        ('f150b186-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Shop 5', 'This is the fifth shop.', '2023-11-23 08:40:47'),
        ('f150b368-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'Shop 6', 'This is the sixth shop.', '2023-11-23 08:40:47'),
        ('f150b459-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Shop 7', 'This is the seventh shop.', '2023-11-23 08:40:47'),
        ('f150b531-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Shop 8', 'This is the eighth shop.', '2023-11-23 08:40:47'),
        ('f150b624-8998-11ee-bb92-42010aae0002', '849c3eba-8916-11ee-bb92-42010aae0002', 'Shop 9', 'This is the ninth shop.', '2023-11-23 08:40:47'),
        ('f150b708-8998-11ee-bb92-42010aae0002', '849c3f2b-8916-11ee-bb92-42010aae0002', 'Shop 10', 'This is the tenth shop.', '2023-11-23 08:40:47'),
        ('fa82e819-8e92-11ee-8b4f-42010aae0002', 'cde5df65-8e91-11ee-8b4f-42010aae0002', 'fjdsklfjfdjlkfsjklfsjlkfjkdwjlkfwf', 'fuckU ', '2023-11-29 16:40:41');
insert into NFT.Subscription (account_uuid, shop_uuid)
values  ('831cd0d0-8916-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002'),
        ('831cd0d0-8916-11ee-bb92-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002'),
        ('831cdb41-8916-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002'),
        ('831cdb41-8916-11ee-bb92-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002'),
        ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002'),
        ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002'),
        ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b459-8998-11ee-bb92-42010aae0002'),
        ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b531-8998-11ee-bb92-42010aae0002');

insert into NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, update_time)
values  ('094527b3-f8f1-4dfc-82cb-066a48d29caa', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002', 'TTTTable', 5, 111, 'TABLE', null, '2023-11-30 17:00:56'),
        ('1a234567-8998-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002', 'Product 1', 100, 25, 'Tag1', 'Description for Product 1', '2023-11-23 08:49:12'),
        ('2b345678-8998-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002', 'Product 2', 50, 50, 'Tag2', 'Description for Product 2', '2023-11-23 08:49:12'),
        ('3c456789-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', 'Product 3', 75, 30, 'Tag3', 'Description for Product 3', '2023-11-23 08:49:12'),
        ('4d567890-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', 'Product 4', 120, 40, 'Tag4', 'Description for Product 4', '2023-11-23 08:49:12'),
        ('5e678901-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', 'Product 5', 80, 60, 'Tag5', 'Description for Product 5', '2023-11-23 08:49:12'),
        ('6f789012-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', 'Product 6', 200, 20, 'Tag6', 'Description for Product 6', '2023-11-23 08:49:12'),
        ('7g890123-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', 'Product 7', 60, 35, 'Tag7', 'Description for Product 7', '2023-11-23 08:49:12'),
        ('8h901234-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', 'Product 8', 90, 45, 'Tag8', 'Description for Product 8', '2023-11-23 08:49:12'),
        ('9802e81f-eabb-43d0-8317-79ff9e1fdda8', 'f150af72-8998-11ee-bb92-42010aae0002', 'SOFA?', 101, 101, 'SOFA', 'is sofa?', '2023-11-30 16:41:32'),
        ('9ad60764-5834-44ee-b328-e34714659212', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 'BEDDDD', 66, 10000, 'BED', null, '2023-11-30 21:58:51'),
        ('fdf706e4-1cca-43c4-89dd-1cd8f01c69ed', 'f150af72-8998-11ee-bb92-42010aae0002', 'TABLEEEE', 555, 1000, 'TABLE', null, '2023-11-30 20:00:30');

insert into NFT.Transaction (transaction_uuid, shop_uuid, account_uuid, coupon_code, receive_time, status, order_time)
values  ('abc123-8998-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'COUPON1', '2023-12-05 12:30:00', 'ordering', '2023-11-23 08:57:30'),
        ('def456-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', null, null, 'delivering', '2023-11-23 08:57:30'),
        ('ghi789-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'DISCOUNT15', '2023-12-10 14:45:00', 'arrived', '2023-11-23 08:57:30'),
        ('jkl012-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', null, null, 'ordering', '2023-11-23 08:57:30'),
        ('mno345-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'SAVE25NOW', '2023-12-08 10:00:00', 'delivering', '2023-11-23 08:57:30'),
        ('pqr678-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'FESTIVE20', '2023-12-12 18:20:00', 'arrived', '2023-11-23 08:57:30'),
        ('stu901-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', null, null, 'ordering', '2023-11-23 08:57:30'),
        ('vwx234-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'HOLIDAY10', '2023-12-07 15:10:00', 'delivering', '2023-11-23 08:57:30');
insert into NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
values  ('abc123-8998-11ee-bb92-42010aae0002', '1a234567-8998-11ee-bb92-42010aae0002', 2),
        ('abc123-8998-11ee-bb92-42010aae0002', '2b345678-8998-11ee-bb92-42010aae0002', 1),
        ('def456-8998-11ee-bb92-42010aae0002', '3c456789-8998-11ee-bb92-42010aae0002', 3),
        ('def456-8998-11ee-bb92-42010aae0002', '4d567890-8998-11ee-bb92-42010aae0002', 1),
        ('ghi789-8998-11ee-bb92-42010aae0002', '5e678901-8998-11ee-bb92-42010aae0002', 2),
        ('ghi789-8998-11ee-bb92-42010aae0002', '6f789012-8998-11ee-bb92-42010aae0002', 4),
        ('jkl012-8998-11ee-bb92-42010aae0002', '7g890123-8998-11ee-bb92-42010aae0002', 1),
        ('jkl012-8998-11ee-bb92-42010aae0002', '8h901234-8998-11ee-bb92-42010aae0002', 3);
insert into NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time)
values  ('abc123-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'Great transaction! Fast delivery and excellent service.', 15, 2, '2023-11-23 08:59:25'),
        ('def456-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'Good experience overall. The product quality is impressive.', 10, 1, '2023-11-23 08:59:25'),
        ('ghi789-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'The coupon code worked perfectly, and I got a nice discount.', 8, 0, '2023-11-23 08:59:25'),
        ('jkl012-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'Easy ordering process. Looking forward to shopping again!', 12, 3, '2023-11-23 08:59:25'),
        ('mno345-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Delivery was a bit late, but the product is in good condition.', 5, 4, '2023-11-23 08:59:25'),
        ('pqr678-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'The festive coupon made my purchase much more affordable. Thank you!', 20, 1, '2023-11-23 08:59:25'),
        ('stu901-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Ordered two items, but one was missing. Contacted customer support for a resolution.', 6, 8, '2023-11-23 08:59:25'),
        ('vwx234-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Product quality is not up to expectations. Disappointed with the purchase.', 2, 15, '2023-11-23 08:59:25');
insert into NFT.Coupon (shop_uuid, discount, coupon_code, expire_time, update_time)
values  ('f150a4b3-8998-11ee-bb92-42010aae0002', 10, 'COUPON1', '2023-12-31 23:59:59', '2023-11-23 08:54:11'),
        ('f150a4b3-8998-11ee-bb92-42010aae0002', 20, 'COUPON2', '2023-12-15 23:59:59', '2023-11-23 08:54:11'),
        ('f150af72-8998-11ee-bb92-42010aae0002', 15, 'DISCOUNT15', '2023-12-20 23:59:59', '2023-11-23 08:54:11'),
        ('f150af72-8998-11ee-bb92-42010aae0002', 25, 'SAVE25NOW', '2023-12-25 23:59:59', '2023-11-23 08:54:11'),
        ('f150b186-8998-11ee-bb92-42010aae0002', 30, '30OFFSHOP', '2023-12-31 23:59:59', '2023-11-23 08:54:11'),
        ('f150b186-8998-11ee-bb92-42010aae0002', 15, 'WINTER15', '2023-12-20 23:59:59', '2023-11-23 08:54:11'),
        ('f150b368-8998-11ee-bb92-42010aae0002', 10, 'HOLIDAY10', '2023-12-31 23:59:59', '2023-11-23 08:54:11'),
        ('f150b368-8998-11ee-bb92-42010aae0002', 20, 'FESTIVE20', '2023-12-15 23:59:59', '2023-11-23 08:54:11'),
        ('6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 0, 'FREEEEEE', '2023-11-11 11:11:11', '2023-12-05 12:26:44');

