create table Shop
(
    shop_uuid    varchar(64)                         not null
        primary key,
    account_uuid varchar(64)                         not null,
    name         varchar(64)                         not null,
    description  varchar(512)                        null,
    is_active    int       default 1                 null,
    update_time  timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint account_uuid
        unique (account_uuid),
    constraint Shop_ibfk_1
        foreign key (account_uuid) references Account (account_uuid)
);

INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('6f54c6e7-51f2-4582-ba33-6223a7cf58ca', 'dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'Quantum Emporium', 'Step into a space where cutting-edge technology meets timeless elegance. Discover futuristic gadgets', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('c4f8d1b0-8d24-11ee-bb92-42010aae0002', '76eafe7a-8d1d-11ee-bb92-42010aae0002', 'Enchanted Finds Boutique', 'Unearth the magic within. This whimsical shop invites you to explore a world of spellbinding treasures', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('c90a780a-8974-4507-9f57-032e5324f18f', 'f81672f3-2925-4396-a33e-dd85a4c03ca1', 'Celestial Creations Outlet', 'Reach for the stars at this outlet', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('e31b3d02-2995-4e2c-9481-93a63403c7af', '7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'Urban Oasis Marketplace', 'Find sanctuary in the heart of the city. This eco-friendly haven offers sustainable goods', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150a4b3-8998-11ee-bb92-42010aae0002', '831cd0d0-8916-11ee-bb92-42010aae0002', 'Mystic Treasures Emporium', 'Embark on a journey of wonder. Uncover ancient artifacts', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150acb3-8998-11ee-bb92-42010aae0002', '831cdb41-8916-11ee-bb92-42010aae0002', 'Vintage Charm Bazaar', 'Timeless elegance meets nostalgia. Browse through carefully curated vintage finds', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150af72-8998-11ee-bb92-42010aae0002', '831cdd39-8916-11ee-bb92-42010aae0002', 'Many product Shop', 'Immerse yourself in the vibrant world of. This artistic oasis showcases handmade crafts', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b096-8998-11ee-bb92-42010aae0002', '831cde2e-8916-11ee-bb92-42010aae0002', 'Starlight Trinkets Gallery', 'Illuminate your life with the treasures at. Discover a curated collection of exquisite jewelry', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b186-8998-11ee-bb92-42010aae0002', '831cdf1e-8916-11ee-bb92-42010aae0002', 'Serendipity Souvenirs Co.', 'Embrace the joy of discovery at. This delightful shop offers charming souvenirs', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b368-8998-11ee-bb92-42010aae0002', '849c38d1-8916-11ee-bb92-42010aae0002', 'Velvet Twilight Emporium', 'Dive into the luxurious ambiance of. This boutique indulges your senses with plush fabrics', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b459-8998-11ee-bb92-42010aae0002', '849c3d7c-8916-11ee-bb92-42010aae0002', 'Luminous Artisan Collective', 'Illuminate your surroundings with the brilliance of the. Explore handcrafted luminaries', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b531-8998-11ee-bb92-42010aae0002', '849c3e36-8916-11ee-bb92-42010aae0002', 'Mirage Mercantile', 'Experience the allure of', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b624-8998-11ee-bb92-42010aae0002', '849c3eba-8916-11ee-bb92-42010aae0002', 'Pinnacle Curiosities Corner', 'Ascend to new heights of curiosity at. This eclectic shop features an assortment of oddities', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('f150b708-8998-11ee-bb92-42010aae0002', '849c3f2b-8916-11ee-bb92-42010aae0002', 'Harmonic Haven Emporium', 'Find harmony in every purchase at. This holistic store offers wellness products', 1, '2023-12-28 03:57:18');
INSERT INTO NFT.Shop (shop_uuid, account_uuid, name, description, is_active, update_time) VALUES ('fa82e819-8e92-11ee-8b4f-42010aae0002', 'cde5df65-8e91-11ee-8b4f-42010aae0002', 'Whimsy Wonders Shoppe', 'Step into a world of whimsy at. Playful and eccentric', 1, '2023-12-28 03:57:18');
