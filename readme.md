# What is this ?
redmineのactivityをtwitterっぽく表示するcssです

# 導入方法
## firefoxの場合
1. アドオンでStylusを導入します(https://addons.mozilla.org/ja/firefox/addon/styl-us/)
1. アドオンマネージャー　→　Stylus　→　スタイル管理　→　新スタイルを作成
1. twitter_style.cssの内容をコピペ
1. 適用先　→　＋　→　URLから始まる でhttps://redmine.hogehoge/activity を入力(hogehogeは適宜urlを参照)

## chromeの場合
firefoxとだいたい一緒です  
https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne?hl=ja

# 仕様
~~アイコンが同じ画像しかできない~~   
~~あらいさん, かばんちゃん, さーばるちゃん, ボスのbase64は埋め込んであるのでお好みでどうぞ~~  
優秀なcommiterによって, できるようになりました  
自分のuseridに対して, アイコンにしたい画像をbase64でencodeして貼り付ければ変更できます  
以下がテンプレになります
```css
a.user[href="/users/'自分のid'"] {
  background-image: url("base64にencodeした画像");
  display: inline-block;
  height: 75px;
  background-position: 0px 18px;
  background-repeat: no-repeat;
  background-size: 50px
}
```
画像サイズが大きすぎると落ちるので, 100×100ぐらいに縮小してからencodeしてください

# 参考
## 画像
https://togetter.com/li/1088229
## css 
https://3owebcreate.com/web/coding/chat_twitter_css
