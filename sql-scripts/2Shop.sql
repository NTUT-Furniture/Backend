create table Shop
(
    shop_uuid    varchar(64)                         not null
        primary key,
    account_uuid varchar(64)                         not null,
    name         varchar(64)                         not null,
    description  varchar(512)                        null,
    is_active    int       default 1                 null,
    update_time  timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint account_uuid
        unique (account_uuid),
    constraint Shop_ibfk_1
        foreign key (account_uuid) references Account (account_uuid)
);

INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 'dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'shoppppppppp11111', null, 1, '2023-11-30 21:57:16');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('c4f8d1b0-8d24-11ee-bb92-42010aae0002', '76eafe7a-8d1d-11ee-bb92-42010aae0002', 'kkyy shop', 'description', 1, '2023-11-27 20:59:15');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('c90a780a-8974-4507-9f57-032e5324f18f', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 't', 'fds', 1, '2023-12-05 20:03:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'fddfsd', null, 1, '2023-12-01 23:38:31');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150a4b3-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'changeed name', 'hi gay shop', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150acb3-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'Shop 2', 'This is the second shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150af72-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'Shop 3', 'This is the third shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b096-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'Shop 4', 'This is the fourth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b186-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Shop 5', 'This is the fifth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b368-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'Shop 6', 'This is the sixth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b459-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Shop 7', 'This is the seventh shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b531-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Shop 8', 'This is the eighth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b624-8998-11ee-bb92-42010aae0002', '849c3eba-8916-11ee-bb92-42010aae0002', 'Shop 9', 'This is the ninth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b708-8998-11ee-bb92-42010aae0002', '849c3f2b-8916-11ee-bb92-42010aae0002', 'Shop 10', 'This is the tenth shop.', 1, '2023-11-23 08:40:47');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('fa82e819-8e92-11ee-8b4f-42010aae0002', 'cde5df65-8e91-11ee-8b4f-42010aae0002', 'fjdsklfjfdjlkfsjklfsjlkfjkdwjlkfwf', 'fuckU ', 1, '2023-11-29 16:40:41');
