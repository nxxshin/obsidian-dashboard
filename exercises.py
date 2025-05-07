# Obsidian Vault Analytics – Guided Exercise Track
# ==================================================
# Purpose: Hands‑on pathway (easy → savage) to level‑up
# your pandas, plotting, and data‑thinking skills using
# your own note corpus.  Solve each bullet, wire it into
# your Streamlit app, commit, push, flex.
# --------------------------------------------------
# HOW TO USE
# 1. Read a prompt ➜ write the code in a separate cell/file.
# 2. Keep the order; each step assumes the previous is done.
# 3. When stuck, RTFM/Python docs before asking ChatGPT.
# 4. After solving, jot reflections directly in your vault.
# --------------------------------------------------

# ---------- LEVEL 0: SANITY CHECK ------------------
# 0. 🔍 *Hello, DataFrame*
#    • Load 'note_stats.csv' into pandas.
#    • Print df.info() and the first 5 rows.
#    • Assert there are >0 rows and required cols exist.

# ---------- LEVEL 1: FUNDAMENTALS ------------------
# 1. 📈 *Daily Pulse*
#    Generate a line chart of notes **created per day** for the last 90 days.
#    👉 Hint: groupby(created_date).size()
#
# 2. 🔢 *Top‑N Tags*
#    Build a horizontal bar chart of the 15 most‑used tags ordered by count.
#    Use explode() on the tag list column.
#
# 3. 📊 *Words vs. Backlinks Scatter*
#    Scatter‑plot word_count (x‑axis) vs. backlink count (y‑axis).
#    Add a trendline; interpret the correlation.

# ---------- LEVEL 2: DATA HYGIENE ------------------
# 4. 🧼 *Duplicate Title Detector*
#    Find notes with identical H1/title lines and list their paths.
#
# 5. 🦴 *Missing Meta Audit*
#    Count how many notes lack any tags OR backlinks.
#    Display them in a Streamlit data_editor for clean‑up.

# ---------- LEVEL 3: DESCRIPTIVE ANALYTICS ----------
# 6. 🔥 *Creation Heatmap*
#    Calendar heatmap: weekdays on y, hour of day on x, cell = note count.
#
# 7. 🌊 *Tag Velocity Stack*
#    Stacked area chart of monthly frequency for the top 5 tags over the past year.
#
# 8. 💎 *Lorenz Curve of Word Counts*
#    • Sort notes by ascending word_count.
#    • Plot cumulative % of notes vs. cumulative % of words.
#    • Compute the Gini coefficient.

# ---------- LEVEL 4: NETWORK ANALYSIS ---------------
# 9. 🕸️ *Link Graph Basics*
#    Build a directed NetworkX graph where nodes = notes, edges = wiki‑links.
#    Render with pyvis inside Streamlit.
#
# 10. 🏰 *Orphan & Hub Finder*
#     Identify (a) orphans = in‑degree==0 AND out‑degree==0,
#     (b) hubs = top 5% by PageRank score.  Show counts + lists.
#
# 11. 🔍 *Community Detection*
#     Apply the Louvain algorithm to find clusters.  Colour the graph by cluster.

# ---------- LEVEL 5: NLP & SEMANTIC LAYER -----------
# 12. 🗺️ *TF‑IDF Mini‑Search*
#     Build a TF‑IDF matrix of note content and implement a simple text query box.
#     Return top 5 note titles + similarity score.
#
# 13. 🧠 *Embedding Explorer*
#     • Generate sentence‑transformer embeddings for each note.
#     • Use PCA or UMAP to 2‑D and plot an interactive scatter.
#
# 14. 📰 *Topic Modeling*
#     Run BERTopic or LDA on the corpus and show top terms per topic.

# ---------- LEVEL 6: PREDICTIVE & GENERATIVE --------
# 15. 📅 *Output Forecast*
#     Fit an ARIMA (or Prophet) model to weekly note creation counts.
#     Forecast the next 4 weeks and plot confidence intervals.
#
# 16. 🤖 *LLM Summarizer Agent*  (Boss Fight)
#     Draft an agent that, given a set of selected note IDs, returns a
#     one‑paragraph synthesis using an open LLM (e.g. OpenAI, llama‑cpp‑python).
#     Include streaming output in the Streamlit UI.

# ---------- EPILOGUE -------------------------------
# • After completing Level 6, refactor the whole app:
#   multi‑page layout, dark/light theme, user preferences.
# • Share a public demo link and tweet the repo.
# • Celebrate with espresso or synthwave—your choice.
