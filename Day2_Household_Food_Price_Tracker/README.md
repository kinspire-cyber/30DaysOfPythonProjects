# Day 2 — Household Food Price Tracker (Nigeria Edition)

A friendly Python CLI that helps Nigerian households track basic food prices, calculate totals and averages, and identify cheapest/most expensive items — using simple built-ins and the naira symbol (₦).

## 🌍 Problem Background

In Nigeria, food prices change frequently due to inflation, fuel prices, transportation costs, and seasonal scarcity. Most households buy weekly without tracking changes or explaining rising costs. This project raises awareness with a simple, local, Python-first tool.

## 👥 Who This Helps

- Nigerian households
- Students learning budgeting
- Small food vendors
- Anyone managing feeding costs
- Python beginners learning real-world programming

## ❗ Why This Problem Matters

- Food inflation hits low-income families hardest
- Measuring change supports better financial decisions
- Builds digital + financial literacy with approachable tooling

## 🧠 Python Concepts (Day 2)

- Variables, built-in functions
- `input()`, `print()`, `int()`, `float()`, `type()`
- Aggregation: `sum()`, `len()`
- Insights: `min()`, `max()`
- No loops or conditionals yet — deliberately simple

## ⚙️ Core Features

- Inputs: household name, market name, and prices for 5 items
  - Rice (per kg), Beans, Garri, Tomatoes, Cooking Oil
- Calculations: total cost, average price, cheapest and most expensive item
- Output: clean summary printed in naira (₦)

## 🧱 Step-by-Step Plan

1. Collect household info: name, market
2. Enter prices for 5 common foods
3. Store values in variables:
   - `rice_price`, `beans_price`, `garri_price`, `tomatoes_price`, `oil_price`
4. Use built-ins:
   - `sum()` → total cost
   - `len()` → number of items
   - `max()` → most expensive
   - `min()` → cheapest
5. Display a clean report with ₦

## 🚀 How To Run

Prerequisite: Python 3.8+ installed.

Windows (from repo root):
```bash
python 