show databases;

use wxapp;

show tables;

select *
from borrow;



create table wxapp.borrow
(
    id        int comment '主键' AUTO_INCREMENT primary key,
    book_isbn varchar(255) null comment '书号',
    user_id   int          null comment '可借数量',
    addtime   datetime     null comment '添加时间',
    status    int(10)      null comment '状态 0 ok 1 下架'

);

drop table wxapp.borrow;


