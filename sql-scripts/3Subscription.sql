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

INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', '6f54c6e7-51f2-4582-ba33-6223a7cf58ca');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'c4f8d1b0-8d24-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'c90a780a-8974-4507-9f57-032e5324f18f');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'c90a780a-8974-4507-9f57-032e5324f18f');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'c90a780a-8974-4507-9f57-032e5324f18f');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'c90a780a-8974-4507-9f57-032e5324f18f');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'e31b3d02-2995-4e2c-9481-93a63403c7af');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'e31b3d02-2995-4e2c-9481-93a63403c7af');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'e31b3d02-2995-4e2c-9481-93a63403c7af');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'e31b3d02-2995-4e2c-9481-93a63403c7af');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150a4b3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150a4b3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150acb3-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150af72-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b096-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b186-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'f150b368-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002');
INSERT INTO NFT.Subscription (account_uuid, shop_uuid) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'f150b368-8998-11ee-bb92-42010aae0002');
