create table TransactionProductLog
(
    transaction_uuid varchar(64)  not null,
    product_uuid     varchar(64)  not null,
    quantity         int unsigned not null,
    constraint TransactionProductLog_ibfk_1
        foreign key (transaction_uuid) references Transaction (transaction_uuid),
    constraint TransactionProductLog_ibfk_2
        foreign key (product_uuid) references Product (product_uuid)
);


CREATE TRIGGER check_if_product_came_from_same_shop
    BEFORE INSERT
    ON TransactionProductLog
    FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1
                   FROM TransactionProductLog,
                        Product
                   WHERE TransactionProductLog.transaction_uuid = NEW.transaction_uuid
                     and TransactionProductLog.product_uuid = Product.product_uuid
                     and Product.shop_uuid = (SELECT shop_uuid
                                              FROM Product
                                              WHERE product_uuid = NEW.product_uuid))
        AND (SELECT 1
             FROM TransactionProductLog
             WHERE transaction_uuid = NEW.transaction_uuid)
    THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'This product does not belong to the same shop as the transaction';
    END IF;
END;

INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
VALUES ('3dbb0f4f-7e4b-4de4-beed-1179dd9241d0', '4d567890-8998-11ee-bb92-42010aae0002', 213);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
VALUES ('3dbb0f4f-7e4b-4de4-beed-1179dd9241d0', '9802e81f-eabb-43d0-8317-79ff9e1fdda8', 213);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
VALUES ('d5736bee-70c1-4f52-a767-a83a8ec4156b', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 0);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
VALUES ('7ae4c64d-17ac-452d-a965-a52b4b948e91', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 0);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity)
VALUES ('e96af1b3-2407-490d-9930-c76a57fdb97a', '1a234567-8998-11ee-bb92-42010aae0002', 0);
