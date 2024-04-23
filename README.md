# 海关报关资料解析
## 项目介绍

本项目旨在最大程度的减少报关员录入报关资料的时间，降本增效。

[项目主页](www.bgd.faship.cn)

#### 1.智能的解析报关资料，包括报关草单，装箱单，发票，申报要素等报关资料，转换为json格式。
    基于大语言模型开发的报关资料智能识别软件，一键识别报关资料中的报关草单、装箱单、发票、申报要素等报关资料。不限文档格式，准确率95%以上。目前支持word、excel、图片、压缩包、eml等文件格式。
    如果一票资料有多个文件，请把资料打成一个压缩包后上传。

 2.给没有归类的商品智能地归类
    如果报关资料只有品名，没有hscode，系统会自动推荐一个hscode。


## 客户端
提供一个客户端展示解析结果。安装包在client目录下，安装后，无需注册，上传报关资料即可识别。客户端支持把识别后的结果导入单一窗口。 
[客户端下载地址](www.bgd.faship.cn)

客户端使用方式请查看[客户端使用说明](www.bgd.faship.cn/how-to)

![avatar](res\img1.png)

## 接口
提供报关单资料解析的接口。上传报关资料，返回json格式的解析结果。结果包括识别的字段和位置，以及报关资料转换成的PDF文件。

获取token请发邮件到gaojie@faship.cn说明意图和联系方式。

#### 接口URL:  http://www.api.bgd.faship.cn:8000/api/parse_async

#### 接口类型：POST; application/json;chatset=utf-8

#### 说明：

    由于上传的资料较长时，解析的时间可能比较长，此接口结果的返回需要提供一个回调的URL，结果会上传到这个URL。通过ID去匹配单据和结果。

#### 接口参数：

| 字段         | 类型        | 描述    |
| ----------- | ----------- | ------- |
| token_id      | string       |用户的token id。获取token请发邮件到gaojie@faship.cn说明意图和联系方式。 |
| document   | string        | Base64编码的文件内容，和document_url 二选一 |
| document_url   | string        | 文件的URL地址，和document 二选一 |
| ext   | string        | 文件后缀，如pdf, png, zip, doc,  目前支持的文件格式包括pdf, 压缩包，email，图片， word, excel |
| callback_url   | string        |  结果回调URL；接口类型POST，返回json格式结果:{‘id’:请求ID,‘status’:解析状态,‘error’:错误信息，‘result’:解析结果}。 回调接口的响应:{‘error’:  ‘OK’#错误信息，OK表示接收成功}|


#### 返回结果：

| 字段         | 类型        | 描述    |
| ----------- | ----------- | ------- |
|id	|string	|请求ID|
|error|	string|	错误信息，’OK’表示没有错误|


#### 回调结果说明，样例参考interface/result_sample.json：

| 字段         | 类型        | 描述    |
| ----------- | ----------- | ------- |
|id	|string	|请求ID|
|status|	string|	解析状态。“解析完成”，“解析失败”|
|result| json | 解析结果|

#### 回调结果result字段说明:
| 字段         | 类型        | 描述    |
| ----------- | ----------- | ------- |
|     TradeCode| dict |  境内发货人海关10位编码 |
|     TradeCoScc|  dict | 境内发货人18位编码|
|    TradeCoName|  dict | 境内发货人名称|
|    OwnerCode|  dict |生产销售单位海关10位编码|
|    OwnerCodeScc|  dict |生产销售单位18位编码|
|    OwnerName|   dict |生产销售单位名称|
|    OverseasConsignorEname| dict | 境外收货人|
|    ContrNo|  dict |合同协议号| 
|    IEPort|   dict |出境关别编码
|    IEPortName|  dict |出境关别中文
|    TrafMode|  dict |运输方式编码| 
|    TrafModeName|  dict |运输方式中文| 
|    VoyNo|  dict |航次号| 
|    TrafName|  dict |运输工具名称| 
|    BillNo|  dict |提运单号| 
|    TradeMode|  dict |监管方式编码| 
|    TradeModeName|  dict |监管方式编码名称| 
|    CutMode|  dict |征免性质| 
|    CutModeName|  dict |征免性质名称| 
|    TradeAreaCode|  dict |贸易国编码| 
|    TradeAreaName| dict | 贸易国名称| 
|    TradeCountry|  dict |运抵国编码| 
|    TradeCountryName| dict | 运抵国名称| 
|    DistinatePort|  dict | 指运港编码| 
|    DistinatePortName|  dict | 指运港名称| 
|    WrapType|  dict |包装种类编码| 
|    WrapTypeName| dict | 包装种类名称| 
|    entyPortCode| dict | 离境口岸编码| 
|    PackNo|  dict |件数| 
|    GrossWet|  dict |毛重（千克）| 
|    NetWt|  dict |净重（千克）| 
|    FeeRate|  dict |运费| 
|    InsurRate|  dict |保费| 
|    OtherRate|  dict |杂费| 
|    TransMode|  dict |成交方式编码| 
|    TransModeName|  dict |成交方式名称| 
|    AttachNo|  dict |随附单证及编号| 
|    NoteS|  dict |标记唛头及备注| 
|    ManualNo|  dict |备案号| 
|    tDocLists|  list |表体| 
|    GNo|  dict |项号| 
|    CodeTS|  dict |商品编码| 
|    GUnit|  dict |成交单位编码| 
|    GUnitName|  dict |成交单位名称| 
|    GQty|  dict |成交数量| 
|    unit1|  dict |第一法定成交单位编码| 
|    unit1Name|  dict |第一法定成交单位名词| 
|    qty1|  dict |第一法定成交数量| 
|    unit2|  dict |第二法定成交单位| 
|    unit2Name|  dict |第二法定成交单位| 
|    qty2| dict | 第二法定成交数量| 
|    DeclPrice|  dict |单价| 
|    DeclTotal|  dict |总价| 
|    TradeCurr|  dict |币制编码| 
|    TradeCurrName|  dict |币制名称| 
|    CusOriginCountry| dict | 原产国（地区）编码| 
|    CusOriginCountryName|  dict |原产国（地区）名称| 
|    DestinationCountry| dict | 最终目的国编码| 
|    DestinationCountryName| dict | 最终目的国名称| 
|    OrigPlaceCode| dict | 境内货源地编码| 
|    OrigPlaceName| dict | 境内货源地名称| 
|    DutyMode| dict | 征免编码| 
|    DutyModeName| dict | 征免名称| 
|    GName|  dict |商品名称| 
|    GModel| list |申报要素|

