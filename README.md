# 🗺️ Pub Crawl Router: Graph-Based Route Optimizer

An intelligent, graph-based routing system designed to find and optimize the perfect "Bar Crawl" itinerary. Built using **Python**, this project takes Pelotas city(Brazil - RS) bars map as an adjacency list (Directed Graph) and utilizes a **Depth-First Search (DFS)** algorithm with custom heuristics to discover the highest-rated route given specific constraints.

---

## 🚀 Features

* **Graph Representation:** Bars are treated as vertices (nodes), and walking distances/times between them are weighted edges.
* **Constraint-Satisfaction Search:** Filters valid paths using real-time user inputs:
    * Start and end times (calculates total available time).
    * Maximum number of venues to visit.
    * Specific amenities (e.g., whether the bar must have a **pool table**).
* **Heuristic Optimization:** Out of all valid paths found, the system calculates and recommends the single best route based on the **highest average user rating** ($\sum \text{ratings} / \text{total bars}$).

---

## 🧠 How the Algorithm Works

The core of this application relies on a **Depth-First Search (DFS)** with backtracking.