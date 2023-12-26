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

DELIMITER //
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
//
DELIMITER ;
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '5e678901-8998-11ee-bb92-42010aae0002', 23);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '6f789012-8998-11ee-bb92-42010aae0002', 213121);
INSERT INTO NFT.TransactionProductLog (transaction_uuid, product_uuid, quantity) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 34);
