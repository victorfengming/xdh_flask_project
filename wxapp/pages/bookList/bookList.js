var config = require('../../utils/config');
var url = config.url;
var util = require('../../utils/util');
var db = require('../../utils/db');
var empno = 'FE717';//暂时hard code，应该是从登陆用户找到对应的工号

Page({
  data: {
    bookList: []
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
    this.queryAllBorrowBooks();
  },
  queryAllBorrowBooks: function () {
    var that = this;

    wx.getStorage({
      key: 'userid',
      success(res) {
         var options = {
           url: config.clubApi.get,
           data: {
             userid: res.data,
           }
         };
         util.request(options, function (res) {
           // console.log(res)



           for (var i = 0; i < res.data.length; i++) {
             res.data[i].pic_url = config.clubApi.img+res.data[i].pic_url
             res.data[i].addtime = util.formDateTime(res.data[i].addtime)


      
           }

           that.setData({
            bookList:res.data
           })

         });
      }
    })


   

  
  },
  queryOneBook: function (key) {
    var that = this;

    var inputMsg = that.data.inputValue;
    var options = {
      url: config.clubApi.list,
      data: {
        appkey: config.appKey,
        type: 'bookLibrary',
        key: key
      }
    };

    util.request(options, (res, err) => {
      var books = [];
      for (var i = 0; i < res.data.result.length; i++) {
        books.push(res.data.result[i].value);
      }
      that.setData({
        bookList: books
      });
    });

  }
})