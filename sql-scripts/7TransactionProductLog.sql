create table TransactionProductLog
(
    transaction_uuid varchar(64)  not null,
    product_uuid     varchar(64)  not null,
    quantity         int unsigned not null,
    constraint TransactionProductLog_ibfk_1
        foreign key (transaction_uuid) references Transaction (transaction_uuid),
    constraint TransactionProductLog_ibfk_2
        foreign key (product_uuid) references Product (product_uuid),
    constraint Check_ProductQuantity
        check (quantity > 0)
);

INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '5e678901-8998-11ee-bb92-42010aae0002', 10);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '6f789012-8998-11ee-bb92-42010aae0002', 10);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 10);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('f3765e89-2826-46ee-97da-126fa81ee280', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 2);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('f0234cf1-1f47-4b3c-8777-5fe72a94e510', '0044af9a-bb9d-4c32-87c9-1ae99c9299eb', 2);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('f0234cf1-1f47-4b3c-8777-5fe72a94e510', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 1);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('a8d3276c-71ac-4e7c-9d28-7426515dfed9', '1a234567-8998-11ee-bb92-42010aae0002', 3);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('a8d3276c-71ac-4e7c-9d28-7426515dfed9', '20c5e309-6f0f-4f8c-a5b5-2f82a8e61a09', 1);
