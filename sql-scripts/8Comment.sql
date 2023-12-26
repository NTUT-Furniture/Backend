create table Comment
(
    comment_uuid varchar(64)                         not null
        primary key,
    product_uuid varchar(64)                         not null,
    account_uuid varchar(64)                         not null,
    text         varchar(512)                        not null,
    update_time  timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint Comment_ibfk_1
        foreign key (product_uuid) references Product (product_uuid),
    constraint Comment_ibfk_2
        foreign key (account_uuid) references Account (account_uuid)
);

INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0724e9e8-58aa-48a6-a5b9-1443a1062601', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 'agvebreabae', '2023-12-26 08:43:12');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc5975-9f28-11ee-9df2-0242ac140002', '094527b3-f8f1-4dfc-82cb-066a48d29caa', '2dba33fc-345c-48e1-bdaa-62665648022b', 'Great product!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6283-9f28-11ee-9df2-0242ac140002', '1a234567-8998-11ee-bb92-42010aae0002', '325ea530-8f2f-11ee-8b4f-42010aae0002', 'Awesome features!', '2023-12-20 11:08:59');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6458-9f28-11ee-9df2-0242ac140002', '2b345678-8998-11ee-bb92-42010aae0002', '4001309d-8f2f-11ee-8b4f-42010aae0002', 'I love it!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6534-9f28-11ee-9df2-0242ac140002', '3c456789-8998-11ee-bb92-42010aae0002', '5f0f6adf-4fde-42c0-bc75-6d51a670924c', 'Could be better.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc65e8-9f28-11ee-9df2-0242ac140002', '4d567890-8998-11ee-bb92-42010aae0002', '76eafe7a-8d1d-11ee-bb92-42010aae0002', 'Not impressed.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc66a7-9f28-11ee-9df2-0242ac140002', '5e678901-8998-11ee-bb92-42010aae0002', '7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'Good value for money, yaaa.', '2023-12-20 11:09:12');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6788-9f28-11ee-9df2-0242ac140002', '6f789012-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'Impressive design!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6918-9f28-11ee-9df2-0242ac140002', '7g890123-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'User-friendly interface.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc69fd-9f28-11ee-9df2-0242ac140002', '8h901234-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'Satisfied customer.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6aa5-9f28-11ee-9df2-0242ac140002', '9802e81f-eabb-43d0-8317-79ff9e1fdda8', '831cde2e-8916-11ee-bb92-42010aae0002', 'Highly recommended!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6b56-9f28-11ee-9df2-0242ac140002', '9ad60764-5834-44ee-b328-e34714659212', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Great buy!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6bf1-9f28-11ee-9df2-0242ac140002', 'fdf706e4-1cca-43c4-89dd-1cd8f01c69ed', '849c38d1-8916-11ee-bb92-42010aae0002', 'Quality product.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6c9a-9f28-11ee-9df2-0242ac140002', '094527b3-f8f1-4dfc-82cb-066a48d29caa', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Impressed with the performance.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6d1d-9f28-11ee-9df2-0242ac140002', '1a234567-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Not bad.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6dcd-9f28-11ee-9df2-0242ac140002', '2b345678-8998-11ee-bb92-42010aae0002', '849c3eba-8916-11ee-bb92-42010aae0002', 'Fast shipping!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6f3c-9f28-11ee-9df2-0242ac140002', '3c456789-8998-11ee-bb92-42010aae0002', '849c3f2b-8916-11ee-bb92-42010aae0002', 'Disappointed.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc6fc2-9f28-11ee-9df2-0242ac140002', '4d567890-8998-11ee-bb92-42010aae0002', 'a3711878-44ae-4328-ad62-4ed45b57c848', 'Could use some improvements.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc7058-9f28-11ee-9df2-0242ac140002', '5e678901-8998-11ee-bb92-42010aae0002', 'ad593cad-96fb-4ebe-a5e4-a0b9101a8d5c', 'Excellent customer service!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc7112-9f28-11ee-9df2-0242ac140002', '6f789012-8998-11ee-bb92-42010aae0002', 'cde5df65-8e91-11ee-8b4f-42010aae0002', 'Happy with my purchase.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc71ca-9f28-11ee-9df2-0242ac140002', '7g890123-8998-11ee-bb92-42010aae0002', 'dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'Not recommended.', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc727f-9f28-11ee-9df2-0242ac140002', '8h901234-8998-11ee-bb92-42010aae0002', 'ddaa8cf0-8db0-11ee-bb92-42010aae0002', 'Great value!', '2023-12-20 11:08:07');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('0dbc727f-9f28-11ee-9df2-0242ac145697', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 'i think mine product is awesome!', '2023-12-25 20:31:56');
INSERT INTO NFT.Comment (comment_uuid, product_uuid, account_uuid, text, update_time) VALUES ('77c0adc9-dc73-4fb9-9b07-c9a57827c2aa', '094527b3-f8f1-4dfc-82cb-066a48d29caa', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 'agvebreabaesdasdsad', '2023-12-26 08:43:19');
