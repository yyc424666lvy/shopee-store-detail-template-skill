# 快速上手（中文）

这个 skill 只做一件事：**把一份「通用产品详情」套进指定店铺的格式，变成能直接粘贴的英文详情。**

它不改产品事实、不改卖点措辞、不译成塔加洛语，只替换店铺的开头块、结尾块和槽位结构。28 家店铺模板与团队在用的那套一致。

仓库地址：https://github.com/yyc424666lvy/shopee-store-detail-template-skill

---

## 一、安装（从 GitHub 装，选一种）

### 方式 A · 下载 ZIP（不需要 git，推荐）

1. 打开这个链接，浏览器会直接下载压缩包：

   https://github.com/yyc424666lvy/shopee-store-detail-template-skill/archive/refs/heads/main.zip

2. 解压后，里面有一层 `shopee-store-detail-template-skill-main` 文件夹。
3. 把它**改名**为 `shopee-store-detail-template`，然后整个放到：

   ```text
   C:\Users\<你的用户名>\.workbuddy\skills\shopee-store-detail-template
   ```

   > 关键：文件夹名必须正好是 `shopee-store-detail-template`，并且在这一层就能看到 `SKILL.md`。

4. 重启 WorkBuddy，输入 `/skills`，列表里出现 `shopee-store-detail-template` 就是装好了。

### 方式 B · 用 git

```powershell
git clone https://github.com/yyc424666lvy/shopee-store-detail-template-skill.git
cd shopee-store-detail-template-skill
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

> 如果目标位置已经有一份旧的，`install.ps1` 会把它改名成 `.bak-时间戳` 留在旁边，**不会删你的东西**。确认新版没问题后自己删掉备份即可。想直接覆盖就加 `-Force`。

装完可以自检（离线，不联网）：

```powershell
cd C:\Users\<你的用户名>\.workbuddy\skills\shopee-store-detail-template
python scripts\doctor.py
```

看到 `status=PASS` 和 `store_count=28` 就对了。

---

## 二、怎么用

直接把「产品详情 + 店铺 ID」发进去就行，三种说法都认：

```text
把下面这份详情替换到 sp16
```

```text
这份详情交叉上架到 sp07、sp09、3pf01
```

```text
用 3pf05 的店铺模板替换这份详情，产品内容不要改
```

一次可以给多个店铺，它会**一家一个文件**，不会合并成一份。

---

## 三、输入长什么样

输入是「通用正文」，结构固定，产品内容随便换：

```text
[开头钩子块]  ← 替换时会整块丢弃，换成目标店铺的
😘 😘😘Welcome to our store😘😘😘
💕💕💕Click to follow and receive more surprises💕💕💕

✔️Brand new and of high quality
✔️The warehouse is located in Manila
✔️Delivery within 24 hours

💕Product Description:
1.Name: Washing Machine Cleaner
2.Material: Sodium percarbonate, imported enzymes, active oxygen factor
3.Color: White
4.Weight: 375g (125g x 3 Bags)
5.Physical Form: Powder
6.Features: 8x active oxygen / 40% cleaning boost
7.Applications: Front-load / Top-load / Semi-automatic
8.Recommended Dosage: 3 sachets per load
9.Package Included: 1PCS * Washing Machine Cleaner 375g

💕Feature:
【8X OXYGEN POWER】：Eight times industry-standard active oxygen for deep drum descaling.
【40% STRONGER】：Upgraded formula boosts cleaning power by 40%.
【99.9% STERILIZATION】：Kills 99.9% of E. coli, Staph and black mold.

💕Note
1.Please make sure to record a unboxing video when receiving the package.
2.If you have any questions, contact our online service.
3.If you are satisfied, please give us a ⭐⭐⭐⭐⭐ rating.
```

三条格式铁律：

- Product Description 每一项是 `N.标签: 值`，**点后面不留空格**
- Feature 每条一行，写成 `【全大写标签】：说明句`（括号和冒号都是全角）
- `Package Included` 排最后一项，写成 `1PCS * 商品名`

如果手上那份详情格式不规整（没编号、冒号中英混用、卖点前面带 `-`），它会先归一化成上面的样子，**但不会自己编内容**。

---

## 四、支持哪些店

| 类型 | 店 ID | 数量 |
|---|---|---|
| 跨境 3PF | `3pf01` – `3pf11` | 11 |
| 本土 SP | `sp01` – `sp17` | 17 |
| 合计 | | **28** |

每家店的槽位结构不一样，有的三槽（Specification / Features / Package），有的只有两槽甚至一槽，有的没有 Package 槽——**这些差异 skill 会按店处理**，不用你操心。

具体某家店长什么样，看 `references/stores/<店ID>.md`，里面有开头块、槽位标题、结尾块和成品骨架。

---

## 五、产出

- 文件名：`<店ID> <店铺名>_详情.txt`，例如 `sp16 Lvy's HIKE Store_详情.txt`
- 编码：UTF-8 带 BOM，换行 CRLF（Windows 记事本不会把 emoji 显示成乱码）
- 内容：**只有正文**。第一行是店铺开头块，最后一行是店铺结尾块，中间没有标题、没有表格、没有自查清单
- 打开就能 Ctrl+A → Ctrl+C 直接贴到 Shopee 后台

---

## 六、几个坑（踩过）

- **产品事实不许改**。材质、尺寸、数量、赠品、承重，源里没有的绝不自己补。参数表缺材质就留空或找供货商确认，别写"全铜""加厚"这种没依据的词。
- **关联推荐图不是本产品**。抓图时容易混进来别家商品的主图，别把别的产品的卖点写进详情。
- **同一份详情可以喂给多家店，但不要把某家店的成品当下一家的输入**。每次都用最初那份通用正文。
- **别写塔加洛语**，成品是纯英文。

---

## 七、要加新店铺怎么办

1. 在 `references/stores/` 下新建一个 md，照着现有文件的四块结构写：开头块、槽位标题、结尾块、成品骨架
2. 在 `references/store-index.md` 里登记一行
3. 跑一下 `python scripts\doctor.py` 自检

现有文件里，`3pf01.md`（三槽标准款）和 `sp14.md`（单槽最简款）最适合当模板抄。
