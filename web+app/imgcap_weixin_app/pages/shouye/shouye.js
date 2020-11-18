Page({
  data: {
    array: []
  },
  onLoad: function (options) {
    var array = this.initData();
    this.setData({ array: array});
  },
  initData: function () {
    var array = [];

    var object1 = new Object();
    object1.img = '../images/666.jpg';
    object1.title = '祝郭总公司早日上市';
    object1.type = '1002贺电';
    object1.liulan = '999浏览';
    object1.pinglun = '999评论';
    array[0] = object1;

    var object2 = new Object();
    object2.img = '../images/666.jpg';
    object2.title = '祝郭总公司早日上市';
    object2.type = '1002贺电';
    object2.liulan = '999浏览';
    object2.pinglun = '999评论';
    array[1] = object2;

    var object3 = new Object();
    object3.img = '../images/666.jpg';
    object3.title = '祝郭总公司早日上市';
    object3.type = '1002贺电';
    object3.liulan = '999浏览';
    object3.pinglun = '999评论';
    array[2] = object3;

    var object4 = new Object();
    object4.img = '../images/666.jpg';
    object4.title = '祝郭总公司早日上市';
    object4.type = '1002贺电';
    object4.liulan = '999浏览';
    object4.pinglun = '999评论';
    array[3] = object4;

    var object5 = new Object();
    object5.img = '../images/666.jpg';
    object5.title = '祝郭总公司早日上市';
    object5.type = '1002贺电';
    object5.liulan = '999浏览';
    object5.pinglun = '999评论';
    array[4] = object5;

    var object6 = new Object();
    object6.img = '../images/666.jpg';
    object6.title = '祝郭总公司早日上市';
    object6.type = '1002贺电';
    object6.liulan = '999浏览';
    object6.pinglun = '999评论';
    array[5] = object6;

    var object7 = new Object();
    object7.img = '../images/666.jpg';
    object7.title = '祝郭总公司早日上市';
    object7.type = '1002贺电';
    object7.liulan = '999浏览';
    object7.pinglun = '999评论';
    array[6] = object7;

    var object8 = new Object();
    object8.img = '../images/666.jpg';
    object8.title = '祝郭总公司早日上市';
    object8.type = '1002贺电';
    object8.liulan = '999浏览';
    object8.pinglun = '999评论';
    array[7] = object8;

    return array;
  }

  
})