const app = getApp()
Page({
  data: {
    array: ['请选择语言', '汉语', '英语', '西班牙语', '法语', '俄语'],
    index: 0,
    imgurl: '',//选择图片的本地路径
    caption:'',//返回的caption结果
  },
  onLoad: function (options) {

  },
  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value
    })
  },
  chooseImageTap: function (e) {
    var that = this;
    wx.navigateTo({
      url: '../component/cropper/cropper?id=1',
      events: {
        // 为指定事件添加一个监听器，获取被打开页面传送到当前页面的数据
        acceptDataFromOpenedPage: function(emit_img) {
          console.log(emit_img),
          that.setData({
            imgurl: app.globalData.imgSrc
          }),
          that.upImgs(app.globalData.imgSrc)
        },
      },
    })
  },

  // chooseImageTap: function () {
  //   var that = this;
  //   wx.showActionSheet({
  //     itemList: ['从相册中选择', '拍照'],
  //     itemColor: "#00000",
  //     success: function (res) {
  //       if (!res.cancel) {
  //         if (res.tapIndex == 0) {
  //           that.chooseWxImage('album')
  //         }
  //         else if (res.tapIndex == 1) {
  //           that.chooseWxImage('camera')
  //         }
  //       }
  //     }
  //   })
  // },
  // 图片本地路径
  // chooseWxImage: function (type) {
  //   var that = this;
  //   var imgsPaths = that.data.imgs;
  //   wx.chooseImage({
  //     sizeType: ['original', 'compressed'],
  //     sourceType: [type],
  //     success: function (res) {
  //       that.setData({
  //         imgurl: res.tempFilePaths[0]
  //       })
  //       console.log(res.tempFilePaths[0]);
  //       that.upImgs(res.tempFilePaths[0]) //调用上传方法
  //     }
  //   }) 
  // },
  //上传服务器
  
  upImgs: function (imgurl) {
    var that = this;
    wx.uploadFile({
      url: 'http://10.181.57.151:8000/imgcap',
      filePath: imgurl,
      name: 'img',
      method: 'POST',
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      formData: {
        language: that.data.index
      },
      success (res){
        console.log(res), //接口返回网络路径
        that.setData({
          caption: res.data
        })
      }
    })
  },
})
