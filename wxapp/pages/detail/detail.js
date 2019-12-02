var app = getApp();
var url = app.url;
var util = require('../../utils/util');
var config = require('../../utils/config');
var db = require('../../utils/db');
var isbn13;
var qty;
var empno = 'FE717';//暂时hard code，应该是从登陆用户找到对应的工号

Page({
    data: {
        bookMsg: {},
        isLoading: true, //是否正在读取数据
        windowWidth: '',
        windowHeight: '',
        pixelRatio: '',
        showBorrowBtn: false, //是否显示 借阅 按钮
        showBookBtn: false, //是否显示 预约 按钮
        showAddBook: false, //是否显示 录入 按钮
        addBookQty: 1 //默认的录入数量
    },
    inputChange: function (e) {
        this.data.addBookQty = e.detail.value;
        //book["qty"] = e.detail.value;
        //that.bookMsg.qty=e.detail.value;
    },
    onLoad: function (options) {
        // 页面初始化 options为页面跳转所带来的参数

        var that = this;


        //1.动态获取设备屏幕的高度，然后计算scroll view的高度
        wx.getSystemInfo({
            success: function (res) {
                that.setData({
                    windowWidth: res.windowWidth,
                    windowHeight: res.windowHeight,
                    pixelRatio: res.pixelRatio
                });
            }
        });

        // 2, 接受页面传递过来的书籍信息
        var book = JSON.parse(options.bookinfo);
        that.setData({
            bookMsg: book,
        });

        // 3,判断当前的书籍数量
        if (book.num > 0) {
            that.setData({
                isLoading: true,
                showBorrowBtn: true,
                showBookBtn: false
            });
        } else if (book.num == 0) {
            that.setData({
                isLoading: true,
                showBorrowBtn: false,
                showBookBtn: true
            });
        }


    },

    borrowBook: function () {

        var that = this;
        //借书
        // 1, 检查用户是否已经登录
        // 获取userid
        wx.getStorage({
            key: 'userid',
            success(res) {
                // 已经登录
                var userid = res.data;
                var book_isbn = that.data.bookMsg.isbn13;
                // console.log(userid)
                // console.log(book_isbn)
                // 2,请求服务器 发送数据 完成借阅
                // 发送到服务器
                var options = {
                    url: config.clubApi.borrow,
                    data: {
                        book_isbn: book_isbn,
                        user_id: userid,
                    }
                };

                util.request(options, (res, err) => {
                    // console.log(res)
                    if (res.data.error == 0) {
                        // 成功借阅,跳转到个人的借阅中心
                        // /bookList/bookList
                        util.showSuccess('借阅成功!', config.showSuccessTime, () => {
                            // wx.navigateBack();
                            wx.navigateTo({
                                url: '../bookList/bookList'
                            });
                        })
                    } else {
                        // 失败
                        util.showSuccess('借阅失败，请联系管理员！', config.showSuccessTime, () => {
                            wx.navigateBack();
                        })

                    }
                });

            }, fail: function () {
                //未 登录
                wx.showToast({
                    title: '请先登录',
                    icon: 'none',
                    duration: 2000,
                    success: function () {
                        // 跳转到注册页面
                        wx.switchTab({
                            url: '/pages/me/me'
                        })
                    }
                })
            }
        })


    },
    addBook: function (e) {


        var that = this;
        //var bookMsg = this.data.bookMsg;
        // this.data.bookMsg.qty = this.data.addBookQty;

        //1.查询是否已经录入过这本书
        var option1 = {
            url: config.clubApi.get,
            data: {
                appkey: config.appKey,
                key: isbn13,
                type: 'bookLibrary'
            }
        };

        //var nowTimestamp = new Date().getTime();
        util.request(option1, res => {
            if (typeof (res.data.result) !== 'undefined') {
                this.data.bookMsg.qty += parseInt(this.data.addBookQty) - 0;
                //this.data.bookMsg.borrowDate =nowTimestamp;
                var options = {
                    url: config.clubApi.put,
                    method: 'POST',
                    header: {
                        'content-type': 'application/x-www-form-urlencoded'//'application/json'
                    },
                    data: {
                        appkey: config.appKey,
                        type: 'bookLibrary',
                        key: isbn13,
                        value: JSON.stringify(this.data.bookMsg)
                        // columns: ['id', 'isbn13', 'title']
                    }
                };

                util.request(options, (res, err) => {
                    if (res.data.success) {

                        util.showSuccess('录入成功!', config.showSuccessTime, () => {
                            wx.navigateBack();
                        })
                    }
                });
            } else {
                this.data.bookMsg.qty = parseInt(this.data.addBookQty) - 0;
                //this.data.bookMsg.borrowDate =nowTimestamp;
                var options = {
                    url: config.clubApi.put,
                    method: 'POST',
                    header: {
                        'content-type': 'application/x-www-form-urlencoded'//'application/json'
                    },
                    data: {
                        appkey: config.appKey,
                        type: 'bookLibrary',
                        key: isbn13,
                        value: JSON.stringify(this.data.bookMsg)
                    }
                };

                util.request(options, (res, err) => {
                    if (res.data.success) {

                        util.showSuccess('录入成功!', config.showSuccessTime, () => {
                            wx.navigateBack();
                        })
                    }
                });

            }
        });


    }
});