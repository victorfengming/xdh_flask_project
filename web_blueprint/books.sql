create table wxapp.books
(
    id           int            not null comment '主键'
        primary key,
    title        varchar(255)   null comment '书名',
    author       varchar(255)   null comment '作者',
    pic_url      varchar(255)   null comment '封面图
',
    publisher    varchar(255)   null comment '出版社',
    price        decimal(10, 2) null comment '价格',
    isbn13       varchar(255)   null comment '书号',
    summary      text           null comment '内容推荐',
    catalog      text           null comment '目录
',
    author_intro varchar(255)   null comment '作者介绍',
    pubdate      varchar(255)   null comment '出版日期
',
    status       varchar(255)   null comment '状态 0 ok 1 下架',
    num          int            null comment '可借数量',
    addtime      datetime       null comment '添加时间'
);

