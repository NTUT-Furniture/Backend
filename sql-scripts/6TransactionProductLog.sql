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

INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('abc123-8998-11ee-bb92-42010aae0002', '1a234567-8998-11ee-bb92-42010aae0002', 2);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('abc123-8998-11ee-bb92-42010aae0002', '2b345678-8998-11ee-bb92-42010aae0002', 1);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('def456-8998-11ee-bb92-42010aae0002', '3c456789-8998-11ee-bb92-42010aae0002', 3);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('def456-8998-11ee-bb92-42010aae0002', '4d567890-8998-11ee-bb92-42010aae0002', 1);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('ghi789-8998-11ee-bb92-42010aae0002', '5e678901-8998-11ee-bb92-42010aae0002', 2);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('ghi789-8998-11ee-bb92-42010aae0002', '6f789012-8998-11ee-bb92-42010aae0002', 4);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('jkl012-8998-11ee-bb92-42010aae0002', '7g890123-8998-11ee-bb92-42010aae0002', 1);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('jkl012-8998-11ee-bb92-42010aae0002', '8h901234-8998-11ee-bb92-42010aae0002', 3);
