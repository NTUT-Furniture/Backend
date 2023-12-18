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

INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cd0d0-8916-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cd0d0-8916-11ee-bb92-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdb41-8916-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdb41-8916-11ee-bb92-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b459-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b531-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('849c3d7c-8916-11ee-bb92-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('849c38d1-8916-11ee-bb92-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('76eafe7a-8d1d-11ee-bb92-42010aae0002', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
