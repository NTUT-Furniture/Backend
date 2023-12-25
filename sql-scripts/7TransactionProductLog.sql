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
