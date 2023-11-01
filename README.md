# 即刻收藏同步到 cubox 🔄

 我有个不好的习惯，使用任务 App 都会滥用他们的收藏和 Like，导致各种资料分散在各地。于是就有了这个项目。

 这是我第一次尝试使用 GPT-4 写代码帮助我解决一些问题。

 功能还有很多缺陷，会持续更新。

## 计划 🚀

**已实现:**

- [x] 同步最新的 5 条（未去重）收藏的动态到你的 Cubox
- [x] 手动执行

**未实现:**

- [ ] 首次自动同步全部动态（分页获取数据）
- [ ] 更新时去重，只同步最新数据.并定时执行

**未来的计划:**

- 输入端
  - Jike 收藏、动态等；
  - Twitter
  - Telegram
  - ...
- 输出端
  - Cubox
  - Notion
  - Obsidian/Logseq
  - Telegram
  - ...
- 更多形态
  - 插件
  - 网页
  - 快捷指令
  - ...

## 使用指南 👨‍💻

1. fork 到你的仓库
2. 获取 [Cubox API](https://cubox.pro/) 和[即刻网页版](https://web.okjike.com/) Cookie。
3. 前往 Github 上仓库设置，secrets，设置变量名如下
    - JIKE_COOKIE
    - CUBOX_API_KEY
4. 前往你 fork 的仓库----> "Actions" ---->"JikeSync"---->"Run workflow"
5. 检查你的 Cubox

欢迎向此 action 贡献，让其更加完善！

## 许可 ⚖️

此项目采用 MIT 许可 - 查看 [LICENSE.md](LICENSE.md) 文件以获取详细信息。
