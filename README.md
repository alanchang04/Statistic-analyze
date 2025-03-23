# 📊 Social Media & Relationship Analysis — Statistics Final Project

This repository contains all files and code related to our final project in the statistics course, focusing on the **relationship between social media usage and interpersonal satisfaction**.

---

## 🧠 Project Topic

**"Social Media Usage Habits and Their Impact on Interpersonal Relationships"**

---

## 🗂️ Folder Structure

```
social-media-statistics/
├── data/
│   └── survey_data.csv                 # Cleaned dataset (Google Form exported)
├── report/
│   └── written_report.pdf              # Formal report (booklet style)
├── slides/
│   └── final_presentation.pptx        # Final presentation slides
├── scripts/
│   └── analysis_code.R                # R script used for statistical testing
├── questionnaire/
│   └── survey_questions.pdf           # List of grouped questions by category
├── README.md
```

---

## 📄 Included Materials

| 類別 | 說明 |
|------|------|
| 📋 問卷 | Google 表單設計，涵蓋 6 大類心理與社交面向（如：依賴感、孤獨感、分享欲等） |
| 📂 資料集 | 共回收 339 份，清理後有效樣本數為 304 份（CSV 格式） |
| 📊 統計分析程式碼 | 使用 R 語言撰寫，包含卡方檢定、Fisher 檢定、ANOVA、線性回歸等分析 |
| 📝 書面報告 | PDF 格式，包含動機、方法、研究問題、統計檢定、解釋與結論 |
| 📽️ 簡報 | 用於期末報告展示的投影片（PowerPoint 格式） |

---

## 🔍 Research Highlights

### 🎯 Research Objectives
- Explore whether **age, gender** affect social media usage time and platform preference
- Examine how **usage behavior** relates to **online relationship satisfaction**
- Investigate the **dependency-loneliness** link via regression

### 🧪 Tests Conducted
- ✅ Fisher’s Exact Test
- ✅ Chi-Square Test of Independence
- ✅ One-Way ANOVA
- ✅ Linear Regression Analysis

### 📌 Key Findings
- Age and gender have **no significant** effect on usage time or preferred platform
- Usage time **does** influence online satisfaction
- Higher dependence on social media is **positively correlated** with online satisfaction — but also with **loneliness**

---

## 📈 Example Visuals (from report)
- Histogram: Age distribution
- Pie charts: Social media preference for chatting/sharing/making friends
- ANOVA summary table for time vs satisfaction
- Regression plots: dependency → satisfaction; loneliness ← dependency

> 🧠 *Conclusion: Social media boosts perceived satisfaction, but may increase loneliness if overused.*

---

## 📬 Contact

Group Members: 張耀仁、方敬棠、王勢全、徐薇安、廖柏任、黃程宥、梁妤榛  
Email: zy84946@gmail.com (代表人)

---

## 📌 Next Steps (if expanded as a research project)
- Incorporate **personality variables** (e.g., MBTI)
- Build a **prediction model** for satisfaction level based on survey responses
- Explore cross-cultural comparisons or time-series surveys
