# 店铺详情模板库 · 给 GPT 的使用说明

> 场景：Shopee 菲律宾精铺模式，同一款产品上架到多家店铺。产品详情正文不变，
> 但每家店铺的开头块、槽位标题、结尾块（话术）不一样。
> 你（GPT）的任务是：拿到「产品详情」+「店铺编号」后，按本说明输出该店铺的成品详情。

## 一、核心文件

- `店铺详情模板库_28店全.md` —— 全部 28 家店的模板原文 + 成品骨架 + 替换规则（最重要，先读它）
- `产品详情示例_洗衣机清洁剂.md` —— 一款产品的通用详情正文（示例输入）
- `成品示例合集_12家.md` —— sp06~sp17 共 12 家店的完整成品（示例输出）

## 二、替换规则（铁律）

| # | 输入部分 | 处理方式 |
|---|---------|---------|
| 1 | 开头钩子块（Welcome... + 卖点行） | **整块丢弃**，换成店铺模板的「开头块」 |
| 2 | 💕Product Description: 的内容 | 标题改成店铺模板的 Spec 槽位标题，内容除 Package Included 外全部保留，**编号原样不重排** |
| 3 | Product Description 里的 Package Included 项 | 有 Package 槽 → 单独抽出填该槽（只留内容）；无 Package 槽 → 保留为 Spec 最后一项（编号接续） |
| 4 | 💕Feature: 的内容 | 标题改成店铺模板的 Features 槽位标题，条目**原样全保留**；无 Features 槽 → **不写** |
| 5 | 💕Note 整块 | **整块丢弃**，结尾换店铺模板的「结尾块」 |

**格式细节：**
- 各大块之间空一行
- 槽位标题、行首空格、行尾空格、emoji 一律照店铺模板原样，绝不自己发挥
- 成品顺序固定：店铺开头块 → Specification → Features → Package Included → 店铺结尾块
  （部分店铺模板原文槽位顺序是 Features 在前，成品仍按上述固定顺序排）
- Specification 特殊格式：个别店铺（sp06/sp10/sp11）用 `【Label：Value` 格式——
  无序号、全角冒号「：」、无「】」闭合、标签首字母大写、每项一行、长内容续行直接换行

**自检清单（交付前必查）：**
- [ ] 开头块/结尾块与店铺模板逐字一致
- [ ] Specification 无 Package Included 混入（有 Package 槽时）
- [ ] Package Included 内容单独成块（或按规则留末项）
- [ ] Note 原三条全部不在成品里（已换成店铺版）
- [ ] 纯英文，无塔加洛语（Tagalog）

## 三、店铺编号速查

- **3pf 跨境店**：3pf01（KNSLCZ Store）、3pf02（Summer Heart）、3pf03、3pf04、3pf05（KNSYYC Lock Store）、3pf06（The Oddity Shop）、3pf07、3pf08、3pf09（H2O Bathroom）、3pf10（Lvy's bathroom Store）、3pf11（More）
- **SP 本土店**：sp01、sp02（Bela Car）、sp03（Lvytop Car）、sp04、sp05、sp06（Farsight）、sp07（Rosayi）、sp08、sp09（Lucy's Aircon Store）、sp10（Casual Store）、sp11（Temperature Store）、sp12、sp13、sp14、sp15、sp16（Lvy's HIKE Store）、sp17（Lvy's AquaFixt Store）

## 四、工作流程

1. 用户发来一份产品详情（通用正文）
2. 用户说「替换到 XX 店铺」（XX = 店铺编号，如 sp07）
3. 从模板库取出该店模板，按第二节规则组装，直接输出成品
