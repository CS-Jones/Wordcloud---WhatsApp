# Wordcloud - WhatsApp

A data-processing and visualization script written in **Python** that parses exported text logs from WhatsApp, cleans structural multi-line messages, handles regex-based user tokenization, and transforms conversational patterns into customized, masked word clouds.

## 🚀 Features

* **Multi-line Log Parsing:** Uses structural data buffering to seamlessly capture and reconstitute multi-line text entries under their primary timestamps.
* **Regex Message Classification:** Embeds precise DateTime and author identification regex patterns to separate timestamps, usernames, and content body blocks.
* **DataFrame Structuring:** Maps extracted conversational strings natively into a structured tabular `pandas.DataFrame` format for immediate metric summaries.
* **Custom Masked Word Clouds:** Processes texts while omitting boilerplate noise (e.g., *"image omitted"*, *"deleted message"*) and wraps words visually using structural image matrices (`PIL`/`WordCloud`).

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:**
  * `numpy` & `pandas` - Tabular data structuring, matrices handling, and quick dataset summaries (`df.describe()`).
  * `matplotlib` - Image subplot plotting grid control and rendering layers.
  * `pillow` (PIL) - Native image asset matrix read/write workflows.
  * `wordcloud` - Frequency analysis rendering mechanics and text layout coloring components.

## ⚙️ Project File Requirements

To run this tool, ensure the following directory layout and physical file requirements are met inside your folder:

```text
📁 whatsapp-wordcloud/
│
├── 📄 main.py               # The script code you provided
├── 🖼️ tor.png               # Required masking image (Determines the silhouette of the cloud)
└── 📄 _chat.txt             # Your exported WhatsApp history text file (UTF-8)
```

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Install all required operational dependencies:**
   ```bash
   pip install numpy pandas matplotlib pillow wordcloud
   ```

3. **Configure File Paths:**
   Open the script and locate line 51 to supply your text file source target name variable:
   ```python
   # Replace the empty string configuration with your real log path filename
   conversationPath = '_chat.txt' 
   ```

## 💻 Running the Script

Execute the analyzer application code directly through your command line context window:
```bash
python main.py
```

### Visual Renders & Output Matrix
* **Console Summary:** Displays data metrics framework columns (`Date`, `Time`, `Author`, `Message`) along with head indexes.
* **Matplotlib Subplots Display:** Generates a window displaying three columns: the plain word cloud, the dynamically re-colored structural image layout cloud, and the original target silhouette map side-by-side.
* **File Export:** Automatically saves your finished stylized design block into the project folder under the filename `torcloud.png`.

## 🗺️ Roadmap & Unfinished Bugs

* [ ] **Dynamic Export Path Isolation:** Add command line interface hooks using `argparse` to pass file targets dynamically without modification inside the code blocks.
* [ ] **Fix Floating Loop Contexts:** Adjust the final un-appended message buffer block at line 66 to make sure the last message array item gets correctly committed when exiting the file while loop context.
* [ ] **Advanced Text Visualizations:** Expand analysis parameters beyond word clouds to capture frequency graphs tracking messaging spikes by author or hourly distributions.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
























Uses https://github.com/amueller/word_cloud to produce word clouds from the sorted whats app
messages. For examples on how the wordclouds look check out the above link for many examples and explanation on how it works
and can be used.
