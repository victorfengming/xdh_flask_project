//logs.js
const util = require('../../utils/util.js')

Page({
  data: {
    logs: []
  },

  // 这个是刚加载完执行的函数
  onLoad: function () {
    console.log("哈哈");
    this.setData({
      logs: (wx.getStorageSync('logs') || []).map(log => {
        return util.formatTime(new Date(log))
      })
    })
  }
});
