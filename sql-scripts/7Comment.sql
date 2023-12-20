create table Comment
(
    transaction_uuid varchar(64)                         not null,
    account_uuid     varchar(64)                         not null,
    text             varchar(512)                        not null,
    likes            int                                 not null,
    dislikes         int                                 not null,
    update_time      timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint Comment_ibfk_1
        foreign key (transaction_uuid) references Transaction (transaction_uuid),
    constraint Comment_ibfk_2
        foreign key (account_uuid) references Account (account_uuid)
);

INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('abc123-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'Great transaction! Fast delivery and excellent service.', 15, 2, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('def456-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'Good experience overall. The product quality is impressive.', 10, 1, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('ghi789-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'The coupon code worked perfectly, and I got a nice discount.', 8, 0, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('jkl012-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'Easy ordering process. Looking forward to shopping again!', 12, 3, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('mno345-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Delivery was a bit late, but the product is in good condition.', 5, 4, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('pqr678-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'The festive coupon made my purchase much more affordable. Thank you!', 20, 1, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('stu901-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Ordered two items, but one was missing. Contacted customer support for a resolution.', 6, 8, '2023-11-23 08:59:25');
INSERT INTO NFT.Comment (transaction_uuid, account_uuid, text, likes, dislikes, update_time) VALUES ('vwx234-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Product quality is not up to expectations. Disappointed with the purchase.', 2, 15, '2023-11-23 08:59:25');
