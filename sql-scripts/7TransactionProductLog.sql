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
