//login.js
var config = require('../../utils/config');
var url = config.url;
var util = require('../../utils/util');
//获取应用实例
var app = getApp()
Page({
  data: {
    userInfo: {}
  },

  onLoad: function (options) {
    var that = this
    that.setData({
      userInfo:JSON.parse(options.userinfo)
    })
  },
  formSubmit:function(e){
    // 接收表单提交的数据
    // console.log('form发生了submit事件，携带数据为：', e.detail.value)

    // 准备提交的数据
    // var formdata = {}
    var formdata = e.detail.value
    formdata['nikeName'] = this.data.userInfo.nickName
    formdata['avatarUrl'] = this.data.userInfo.avatarUrl
    // console.log(formdata)

    // 获取用户的 code

    wx.login({
      success(res) {
        if (res.code) {
          // 发起网络请求
          // 发送到服务器
          var options = {
            url: config.clubApi.register+'?code='+res.code,
            data: {
              method:'POST',
              userinfo : formdata
            }
          };

          util.request(options, (res, err) => {
            // 把返回 用户标识 存入 小程序中
            wx.setStorage({
              key: 'userid',
              data: res.data.code,
              success:function(){
                // 跳转到me页面
                wx.navigateBack({
                  delta: 1
                })
              }
            })
          });
   
        } else {
          console.log('登录失败！' + res.errMsg)
        }
      }
    })

    

  }
  
})
