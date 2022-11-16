# BAZAARの開発
**基本的に、「mainブランチ」「developブランチ」は触らない**

**もし触る場合は、必ずメンバー全員に相談する事。**

開発する際には、このリポジトリを「Fork」して、自分が担当するブランチで開発を進める。

開発を進める際には、「feature/xxx」という名前のブランチを自分で切り、そこで開発する。「xxx」の部分は何の実装をしたのかが分かりやすい名前にすること

（例）

自分が「ユーザー機能の中のログイン機能」を実装するなら、

このリポジトリをForkし、Forkしたリポジトリを自分の環境にcloneして、「userブランチ」に移動する。

そこで「feature/login」というブランチを切り、そのブランチで開発を始める。

開発が完了したら、add して、commit して、「userブランチ」からマージして、「git push origin user」でpush して「プルリクエスト」を送る

## それぞれのブランチの説明
### userブランチ
 - ユーザー機能の実装
	
### compブランチ
 - 事業者機能の実装
	
### topブランチ
 - 共通部分の機能の実装

### adminブランチ
 - 管理者機能の実装


## 開発の具体的流れ
### 開発環境
 - このリポジトリをForkし、自分のリモートリポジトリに反映されているかを確認
 - 自分のリモートリポジトリからローカルにcloneする
 - 「templates/comp」「templates/top」「templates/user」の中にある「sampleファイル」を削除  
 - manage.pyと同じ階層に「local_settings.py」を作成し記述
 - 自分が作業を行うブランチに移動  
   (例)ユーザー側の何かしらの機能を実装したいなら「git checkout user」でuserブランチに移動
 - 「feature/xxx」という形でブランチを切り、「xxx」の部分は親のブランチとどんな機能を実装したかが分かるような名前にする **(あくまでも任意の名前で可)**   
   (例)userブランチから、「ユーザーのログイン機能」を実装したい場合、「git checkout -b feature/user_login」で「feature/user_login」というブランチを切り、移動
 - runserverで「Hello User」が赤文字で表示されれば開発環境の導入は成功

## よく使うコマンド
 - リモートリポジトリから、ローカルにコードをコピー  
 	`git clone https://github.com/xxxxx/xxxxxx.git`  
	
 - 現在位置するブランチを確認する  
	`git branch`  
	
 -  ブランチの作成  
 	`git branch 任意のブランチ名`  

 -  ブランチの削除  
 	`git branch -D ブランチ名`  
	
 -  push済みのブランチの削除  
 	`git branch -d ブランチ名`  
	
 -  ブランチの移動  
 	`git checkout ブランチ名`  
	
 -  ブランチの作成 & 移動  
 	`git checkout -b ブランチ名`  
	
 - ステージング  
 	`git add ファイル名`  
	
 - コミット  
 	`git commit -m "メッセージ"`  

 - プッシュ  
 	`git push origin ブランチ名`  
