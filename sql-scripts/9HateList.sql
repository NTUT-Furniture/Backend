create table HateList
(
    account_uuid varchar(64) not null,
    comment_uuid varchar(64) not null,
    if_hates     tinyint(1)  not null,
    primary key (account_uuid, comment_uuid),
    constraint HateList_ibfk_1
        foreign key (account_uuid) references Account (account_uuid),
    constraint HateList_ibfk_2
        foreign key (comment_uuid) references Comment (comment_uuid)
);

create index comment_uuid
    on HateList (comment_uuid);

INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('5f0f6adf-4fde-42c0-bc75-6d51a670924c', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('5f0f6adf-4fde-42c0-bc75-6d51a670924c', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('76eafe7a-8d1d-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('76eafe7a-8d1d-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('7f4d7718-9df9-48d5-92e2-678cfbf09a7b', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('7f4d7718-9df9-48d5-92e2-678cfbf09a7b', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cd0d0-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cd0d0-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdb41-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdb41-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdf1e-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('831cdf1e-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c38d1-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c38d1-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3d7c-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3d7c-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3e36-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3e36-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3eba-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3eba-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3f2b-8916-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('849c3f2b-8916-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('a3711878-44ae-4328-ad62-4ed45b57c848', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('a3711878-44ae-4328-ad62-4ed45b57c848', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('ad593cad-96fb-4ebe-a5e4-a0b9101a8d5c', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('ad593cad-96fb-4ebe-a5e4-a0b9101a8d5c', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('cde5df65-8e91-11ee-8b4f-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('cde5df65-8e91-11ee-8b4f-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('ddaa8cf0-8db0-11ee-bb92-42010aae0002', '0dbc5975-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('ddaa8cf0-8db0-11ee-bb92-42010aae0002', '0dbc6283-9f28-11ee-9df2-0242ac140002', 1);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('f81672f3-2925-4396-a33e-dd85a4c03ca1', '0dbc5975-9f28-11ee-9df2-0242ac140002', 0);
INSERT INTO NFT.HateList (account_uuid, comment_uuid, if_hates) VALUES ('f81672f3-2925-4396-a33e-dd85a4c03ca1', '0dbc6283-9f28-11ee-9df2-0242ac140002', 0);
