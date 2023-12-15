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
    is_active    int       default 1                 null,
    update_time  timestamp default CURRENT_TIMESTAMP null,
    constraint Product_ibfk_1
        foreign key (shop_uuid) references Shop (shop_uuid)
);

INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('094527b3-f8f1-4dfc-82cb-066a48d29caa', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002', 'TTTTable', 5, 111, 'TABLE', null, 1, '2023-11-30 17:00:56');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('1a234567-8998-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002', 'Product 1', 100, 25, 'Tag1', 'Description for Product 1', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('2b345678-8998-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002', 'Product 2', 50, 50, 'Tag2', 'Description for Product 2', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('3c456789-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', 'Product 3', 75, 30, 'Tag3', 'Description for Product 3', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('4d567890-8998-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002', 'Product 4', 120, 40, 'Tag4', 'Description for Product 4', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('5e678901-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', 'Product 5', 80, 60, 'Tag5', 'Description for Product 5', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('6f789012-8998-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002', 'Product 6', 200, 20, 'Tag6', 'Description for Product 6', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('7g890123-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', 'Product 7', 60, 35, 'Tag7', 'Description for Product 7', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('8h901234-8998-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002', 'Product 8', 90, 45, 'Tag8', 'Description for Product 8', 1, '2023-11-23 08:49:12');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('9802e81f-eabb-43d0-8317-79ff9e1fdda8', 'f150af72-8998-11ee-bb92-42010aae0002', 'SOFA?', 101, 101, 'SOFA', 'is sofa?', 1, '2023-11-30 16:41:32');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('9ad60764-5834-44ee-b328-e34714659212', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 'BEDDDD', 66, 10000, 'BED', null, 1, '2023-11-30 21:58:51');
INSERT INTO NFT.Product (product_uuid, shop_uuid, name, stock, price, tags, description, is_active, update_time) VALUES ('fdf706e4-1cca-43c4-89dd-1cd8f01c69ed', 'f150af72-8998-11ee-bb92-42010aae0002', 'TABLEEEE', 555, 1000, 'TABLE', null, 1, '2023-11-30 20:00:30');
