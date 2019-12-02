module.exports={
    url:'http://192.168.254.128:8080',
    // doubanUrl:'https://api.douban.com/v2/book/isbn/',
    doubanUrl:'https://douban.uieee.com/v2/book/isbn/',
    appKey:'wx9695f00d6f1463a2',
    appID:'wx9695f00d6f1463a2',
    appSecret:'70c8318ee9efef3d1ecda53cf31199b9',
    showSuccessTime:1000,
    clubApi:{
        // put:'https://api.wxappclub.com/put',
        // del:'https://api.wxappclub.com/del',
        // match:'https://api.wxappclub.com/match',
        get:'http://192.168.254.128:8080/api/get/borrow',
        list:'http://192.168.254.128:8080/api/list',
        register:'http://192.168.254.128:8080/api/register',
        borrow:'http://192.168.254.128:8080/api/books/borrow',
        img:'http://192.168.254.128:8080/static/uploads/',
        // wxUser:'https://api.wxappclub.com/wxUser',
    }
}
