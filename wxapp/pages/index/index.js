//index.js
//获取应用实例
var app = getApp();
var config = require('../../utils/config');
var url = config.url;
var util = require('../../utils/util');
var db = require('../../utils/db');

Page({
  data: {
    bookList: [],
    inputValue: ''
  },
  inputChange: function (e) {
    this.data.inputValue = e.detail.value;
  },
  //事件处理函数
  bindViewTap: function () {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    //console.log('onload index')
    var that = this;
  },
  queryBooks: function (e) {
    var that = this;

    var inputMsg = that.data.inputValue;
    var options = {
      url: config.clubApi.list,
      data: {
        appkey: config.appKey,
        type: 'bookLibrary',
        // columns:'title',
        keywords: inputMsg
        //columns: ['id', 'isbn13', 'title']
      }
    };

    util.request(options, (res, err) => {

        // 判断是否查询到了书籍信息
        if (res.data.length == 0) {
            // 设置提醒信息,
            // console.log('没有查询到相关书籍信息')
            wx.showToast({
              title: '没有查询到相关书籍信息',
              icon: 'none',
              duration: 2000
            })
            return;
        }
      
        // 处理图片地址
        for (var i = 0; i < res.data.length; i++) {
            res.data[i].pic_url = config.clubApi.img+res.data[i].pic_url
        }
        // 设置书籍的数据
        that.setData({
            bookList: res.data
        });
    });

  },
  goToDetailPage: function (e) {

    var isbn13 = e.currentTarget.id;
    var book = {}
    for (var i = 0; i < this.data.bookList.length; i++) {
        if(this.data.bookList[i].isbn13 == isbn13){
            book = this.data.bookList[i]
        }
    }

    wx.navigateTo({
      url: '../detail/detail?bookinfo='+JSON.stringify(book)
    });

  },
  onShow: function () {
    // 页面显示
    //console.log('onshow');
    this.queryAllBooks();
    // this.queryBooks();
  },
  queryAllBooks: function () {

    var that = this;
    var options = {
      url: config.clubApi.list,
      data: {
        appkey: config.appKey,
        type: 'bookLibrary'
      }
    };

    util.request(options, function (res) {
        // 处理图片地址
        for (var i = 0; i < res.data.length; i++) {
            res.data[i].pic_url = config.clubApi.img+res.data[i].pic_url
        }
        that.setData({
            bookList: res.data
        })
    });
    


  }

})
