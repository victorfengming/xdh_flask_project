module.exports = {
    url: 'http://192.168.61.128:5000',
    // doubanUrl:'https://api.douban.com/v2/book/isbn/',
    doubanUrl: 'https://douban.uieee.com/v2/book/isbn/',
    // TODO 这里没有一个参数没改掉,难道是一样的
  appKey: 'wx9695f00d6f1463a2',
  appID: 'wx9695f00d6f1463a2',
  appSecret: '70c8318ee9efef3d1ecda53cf31199b9',

    showSuccessTime: 1000,
    clubApi: {
        // put:'https://api.wxappclub.com/put',
        // del:'https://api.wxappclub.com/del',
        // match:'https://api.wxappclub.com/match',
        get: 'http://192.168.61.128:5000/api/get/borrow',
        list: 'http://192.168.61.128:5000/api/list',
        register: 'http://192.168.61.128:5000/api/register',
        borrow: 'http://192.168.61.128:5000/api/books/borrow',
        img: 'http://192.168.61.128:5000/static/uploads/',
        // wxUser:'https://api.wxappclub.com/wxUser',
    }
};
