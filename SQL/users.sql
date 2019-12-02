show databases;

use wxapp;


show tables;

select *
from users;



create table user
(
    id   INT         NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

create table if not exists wxapp.users
(
    id        int auto_increment comment '主键'
        primary key,
    nikeName  varchar(255) null,
    avatarUrl varchar(255) null,
    username  varchar(255) null,
    bumen     varchar(255) null,
    phone     varchar(11)  null,
    addtime   datetime
);


drop table wxapp.users;


insert into users
values (null,
        "Victor",
        "https://wx.qlogo.cn/mmopen/vi_32/iaIzMeic5IhT1mSy3uccEjHNyy30KrsXXIlCtTj3KRBiaXgz2CJ13EIAsia7Bx8WQT83u7g0iadEibTOicPZ0z46DK9ow/132",
        "小麦粉",
        "xdh",
        "13940206091",
        "2019-12-02 22:44:26");



insert into users
values (null,
        "Victor",
        "https://wx.qlogo.cn/mmopen/vi_32/iaIzMeic5IhT1mSy3uccEjHNyy30KrsXXIlCtTj3KRBiaXgz2CJ13EIAsia7Bx8WQT83u7g0iadEibTOicPZ0z46DK9ow/132",
        "小米",
        "Java",
        "13940209812",
        "2019-12-02 22:47:56");

