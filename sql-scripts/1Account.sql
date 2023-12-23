create table Account
(
    account_uuid varchar(64)                          not null
        primary key,
    name         varchar(64)                          not null,
    email        varchar(128)                         not null,
    pwd          varchar(128)                         not null,
    phone        varchar(32)                          null,
    credit_card  varchar(64)                          null,
    birthday     date                                 null,
    address      varchar(256)                         null,
    is_active    tinyint(1) default 1                 null,
    role         int        default 0                 null,
    update_time  timestamp  default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint Account_pk
        unique (email)
);

INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('2dba33fc-345c-48e1-bdaa-62665648022b', 'gayrr', 't110590028@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', 'phone', 'jy;kjr;ggk;lfkdfk;lfwjkrefwjpp',
        '1933-11-28 00:00:00', null, 1, 0, '2023-11-30 13:56:52');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('325ea530-8f2f-11ee-8b4f-42010aae0002', 'fortesting', 'testing@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '123456789', '1234-1234-1234-1234',
        '2023-12-04 18:33:29', '369 divine St, Taipei', 1, 0, '2023-11-30 11:18:56');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('4001309d-8f2f-11ee-8b4f-42010aae0002', 'fjsdlkjflkds', 'fdafv@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-11-30 11:19:19');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('5f0f6adf-4fde-42c0-bc75-6d51a670924c', 'asd', 'asd@asd.djlk',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, '456', null, null, 1, 0,
        '2023-12-14 04:24:59');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('76eafe7a-8d1d-11ee-bb92-42010aae0002', 'kyyyyyyyyyy', 'asd@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '0955222444', null, '2077-07-07 00:00:00', null,
        1, 0, '2023-11-27 20:06:58');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('7f4d7718-9df9-48d5-92e2-678cfbf09a7b', 'gjfkldgjlkj', 'asdf@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-12-01 23:38:15');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('831cd0d0-8916-11ee-bb92-42010aae0002', 'notVincent', 'john.doe@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '123-456-7890', '1234-5678-9012-3456',
        '1990-01-15 00:00:00', '123 Main St, Cityville', 1, 0, '2023-11-22 17:07:07');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('831cdb41-8916-11ee-bb92-42010aae0002', 'gary', 'gjlksjlkdgg32f@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', 'ejgklgjdklffl21', 'fkl2lk1rklgnk',
        '2002-11-28 15:14:45', 'asd', 1, 0, '2023-11-22 17:07:07');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('831cdd39-8916-11ee-bb92-42010aae0002', 'Bob Johnson', 'bob.johnson1@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '555-123-4567', '4321-8765-0987-6543',
        '1978-03-10 00:00:00', '789 Pine St, Villagetown', 0, 0, '2023-11-22 17:07:07');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('831cde2e-8916-11ee-bb92-42010aae0002', 'Alice Williams', 'alice.williams@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '333-999-8888', '8765-4321-5678-9012',
        '1982-11-05 00:00:00', '567 Elm St, Hamletville', 1, 0, '2023-11-22 17:07:07');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('831cdf1e-8916-11ee-bb92-42010aae0002', 'Charlie Brown', 'charlie.brown@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '777-555-1234', '3456-7890-1234-5678',
        '1995-09-30 00:00:00', '234 Birch St, Riverside', 1, 0, '2023-11-22 17:07:07');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('849c38d1-8916-11ee-bb92-42010aae0002', 'John Doe', 'john.1@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '123-456-7890', '1234-5678-9012-3456',
        '1990-01-15 00:00:00', '123 Main St, Cityville', 1, 0, '2023-11-22 17:07:10');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('849c3d7c-8916-11ee-bb92-42010aae0002', 'Jane Smith', 'jane.smith@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '987-654-3210', '9876-5432-1098-7654',
        '1985-07-22 00:00:00', '456 Oak St, Townsville', 1, 0, '2023-11-22 17:07:10');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('849c3e36-8916-11ee-bb92-42010aae0002', 'Bob Johnson', 'bob.johnson@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '555-123-4567', '4321-8765-0987-6543',
        '1978-03-10 00:00:00', '789 Pine St, Villagetown', 0, 0, '2023-11-22 17:07:10');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('849c3eba-8916-11ee-bb92-42010aae0002', 'Monfjdskl', 'fdjkfldjlk@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '333-999-8888', '8765-4321-5678-9012',
        '1982-11-05 00:00:00', '567 Elm St, Hamletville', 1, 0, '2023-11-22 17:07:10');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('849c3f2b-8916-11ee-bb92-42010aae0002', 'Dars Veda', '654675@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '777-555-1234', '3456-7890-1234-5678',
        '1995-09-30 00:00:00', '234 Birch St, Riverside', 1, 0, '2023-11-22 17:07:10');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('a3711878-44ae-4328-ad62-4ed45b57c848', 'dsadsad', 'dasads@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-12-05 17:08:48');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('ad593cad-96fb-4ebe-a5e4-a0b9101a8d5c', 'hhh', '3r24g@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-11-30 10:14:58');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('cde5df65-8e91-11ee-8b4f-42010aae0002', 'fuck Garry', '34t345@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-11-29 16:32:17');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('dc7de7cd-22bc-4a45-90bb-74bbc3ff8760', 'asdfg', '5g55gh@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 0,
        '2023-11-30 21:56:05');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('ddaa8cf0-8db0-11ee-bb92-42010aae0002', 'name1', '43h54h@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', null, null, null, null, 1, 1,
        '2023-11-28 13:42:06');
INSERT INTO NFT.Account (account_uuid, name, email, pwd, phone, credit_card, birthday, address, is_active, role,
                         update_time)
VALUES ('f81672f3-2925-4396-a33e-dd85a4c03ca1', 'fuck', 'email@gmail.com',
        '$2b$12$tu4S3wbz1lcwnMZlI8QVTusvZqDx4bBMz5HOyPx0dnZozWTxtjMcC', '123-456-7890', '1234-5678-9012-3456',
        '1990-01-15 00:00:00', '123 Main St, Cityville', 1, 1, '2023-12-05 17:21:26');
