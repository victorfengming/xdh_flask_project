//me.js
//获取应用实例
var app = getApp()
Page({
  data: {
    userInfo: {},
    showBadge:false,
    isLogin:false,
    meList:[
      {
        text:'借入的图书',
        icon:'../../assets/img/iconfont-dingdan.png',
        url:'../bookList/bookList'
      },
            {
        text:'借出的图书',
        icon:'../../assets/img/iconfont-help.png',
        url:''
      },
            {
        text:'预约的图书',
        icon:'../../assets/img/iconfont-icontuan.png',
        url:''
      },
            {
        text:'飘流的图书',
        icon:'../../assets/img/iconfont-kefu.png',
        url:''
      },
            {
        text:'曾经拥有的图书',
        icon:'../../assets/img/iconfont-tuihuo.png',
        url:''
      },
    ]
  },

  onLoad: function () {
    var that = this
    
  },
  onShow:function(){
    var that = this
    // 判断当前用户是否已经注册
      wx.getStorage({
        key: 'userid',
        success(res) {
           that.setData({
            userInfo:app.globalData.userInfo,
            isLogin:true
          })
        }
      })
  },
  onGotUserInfo:function(e){
    var that = this
    // 获取用户的基本信息
    that.setData({
      userInfo:e.detail.userInfo,
      isLogin:true
    })

    // 基本信息 存入app对象中
    app.globalData.userInfo = e.detail.userInfo

    // 跳转到注册页面
    wx.navigateTo({
      url: '../login/login?userinfo='+JSON.stringify(e.detail.userInfo)
    });

  }
})
